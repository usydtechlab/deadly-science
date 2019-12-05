import os

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
from django.template import RequestContext

from . import models
from . import forms
import hashlib
import datetime
from django.conf import settings
from django.db.models import Q
from django.utils import timezone


# Create your views here.


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    if request.session.get('is_login', None):
        img = models.User.objects.filter(role='teacher')
        unread_message1=models.Appointment.objects.filter(student_id=request.session['user_id'])
        unread_message = unread_message1.filter(student_message_status='unread')
        print(unread_message)
        print(request.session['user_id'])
        return render(request, 'pages/index_copy.html', {'unread_message': unread_message,'img': img})
    else:
        img = models.User.objects.filter(role='teacher')
        return render(request, 'pages/index_copy.html', {'img': img})

def index_home(request):
    return render(request, 'pages/index_copy.html')

def index_manageapp_current(request):

    from .models import Appointment


    unread_message1=models.Appointment.objects.filter(student_id=request.session['user_id'])
    unread_message = unread_message1.filter(student_message_status='unread')

    order = Appointment.objects.order_by('date')
    current_user = order.filter(student_id=request.session['user_id'])
    current = current_user.filter(Q(status='confirmed') |  Q(status='unconfirmed'))
    models.Appointment.objects.filter(student_id=request.session['user_id']).update(student_message_status='read')

    return render(request, 'pages/manageApp-current.html', {'current': current,'unread_message': unread_message})


def index_manageapp_history(request):
    from .models import Appointment
    unread_message1 = models.Appointment.objects.filter(student_id=request.session['user_id'])
    unread_message = unread_message1.filter(student_message_status='unread')
    order = Appointment.objects.order_by('date')
    current_user = order.filter(student_id=request.session['user_id'])
    history = current_user.filter(Q(status='completed') | Q(status='rejected') | Q(status='cancelled'))
    return render(request, 'pages/manageApp-history.html',{'history': history,'unread_message': unread_message})


def index_about(request):
    if request.session.get('is_login', None):  # 不允许重复登录

        unread_message1=models.Appointment.objects.filter(student_id=request.session['user_id'])
        unread_message = unread_message1.filter(student_message_status='unread')
        return render(request, 'pages/about.html', {'unread_message': unread_message})
    return render(request, 'pages/about.html')

def index_detail(request,id):
    from .models import User
    from .models import Timetable
    from .models import Appointment
    unread_message1 = models.Appointment.objects.filter(student_id=request.session['user_id'])
    unread_message = unread_message1.filter(student_message_status='unread')
    userdetail = User.objects.get(id=id)
    order = Timetable.objects.order_by('date')
    timedetail = order.filter(user_id= id)
    order_appointment = Appointment.objects.all().order_by('date')
    current_user = order_appointment.filter(student_id=request.session['user_id'])
    current = current_user.filter(Q(status='confirmed') | Q(status='completed') | Q(status='unconfirmed'))
    for i in current:
        unavailable_id = i.confirm_id
        models.Timetable.objects.filter(id=unavailable_id).update(status='unavailable')
    return render(request, 'pages/index-detail.html', {'userdetail': userdetail, 'timedetail': timedetail,'unread_message':unread_message})


def index_account_profile(request):
    unread_message1 = models.Appointment.objects.filter(student_id=request.session['user_id'])
    unread_message = unread_message1.filter(student_message_status='unread')
    current_user = models.User.objects.filter(id=request.session['user_id'])
    history_firstname = current_user.get().firstname
    history_lastname = current_user.get().lastname
    history_email = current_user.get().email
    history_gender = current_user.get().gender
    history_organization = current_user.get().organization
    history_img = current_user.get().img


    if request.method == 'POST':

        message = 'Please check the input！'
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        organization = request.POST.get('organization')

        img = request.FILES['img']

        save_path = '{}/img/{}'.format(settings.MEDIA_ROOT, img.name)
        with open(save_path, 'wb') as f:
            # 3、获取上传文件的内容， 并写到创建的文件中
            for content in img.chunks():  # pic.chunks文件内容
                f.write(content)
        models.User.objects.filter(name=request.session['user_name']).update(img='img/{}'.format(img.name))
        if not firstname == history_firstname:
            models.User.objects.filter(name=request.session['user_name']).update(firstname=firstname)
        if not lastname == history_lastname:
            models.User.objects.filter(name=request.session['user_name']).update(lastname=lastname)
        if not email == history_email:
            models.User.objects.filter(name=request.session['user_name']).update(email=email)
        if not gender == history_gender:
            models.User.objects.filter(name=request.session['user_name']).update(gender=gender)
        if not organization == history_organization:
            models.User.objects.filter(name=request.session['user_name']).update(organization=organization)
        if not img == history_img:
            models.User.objects.filter(name=request.session['user_id']).update(img='img/{}'.format(img.name))

        return render(request, 'pages/account-profile.html', locals())


    return render(request, 'pages/account-profile.html',{'unread_message': unread_message, 'current_user':current_user})


def index_account_pw(request):
    unread_message1 = models.Appointment.objects.filter(student_id=request.session['user_id'])
    unread_message = unread_message1.filter(student_message_status='unread')
    return render(request, 'pages/account-pw.html',{'unread_message':unread_message})


def index_sci(request):
    from .models import Appointment
    unread_message1 = models.Appointment.objects.filter(scientist_id=request.session['user_id'])
    unread_message = unread_message1.filter(scientist_message_status='unread')
    order = models.Timetable.objects.all().order_by('date')
    sci_timetable = order.filter(user_id=request.session['user_id'])
    order_appointment = Appointment.objects.all().order_by('date')
    current_user = order_appointment.filter(scientist_id=request.session['user_id'])

    current = current_user.filter(Q(status='confirmed') | Q(status='completed') | Q(status='unconfirmed'))
    current_1 = current_user.filter(Q(status='rejected') | Q(status='cancelled'))
    for i in current_1:

        available_id = i.confirm_id
        models.Timetable.objects.filter(id = available_id).update(status='available')

    for i in current:

        unavailable_id = i.confirm_id
        models.Timetable.objects.filter(id = unavailable_id).update(status='unavailable')

    available_time = models.Timetable.objects.filter(status='available')
    # for i in current:
    #     models.Timetable.objects.filter(id = )

    if request.method == 'POST':

        date = request.POST.get('date')
        starttime = request.POST.get('starttime')
        duration = request.POST.get('duration')
        method = request.POST.get('method')
        location_id = request.POST.get('location_id')

        new_timetable = models.Timetable()
        new_timetable.user_id = request.session['user_id']
        new_timetable.date = date
        new_timetable.starttime = starttime
        new_timetable.duration = duration
        new_timetable.method = method
        new_timetable.location_id = location_id

        new_timetable.save()



        return render(request, 'pages/ManageTime_SCI.html', locals())
    else:

        return render(request, 'pages/ManageTime_SCI.html', {'sci_timetable': sci_timetable,'available_time':available_time,'unread_message':unread_message})



def index_sci_manageapp(request):
    from .models import Appointment
    unread_message1 = models.Appointment.objects.filter(student_id=request.session['user_id'])
    unread_message = unread_message1.filter(student_message_status='unread')
    order = Appointment.objects.order_by('date')
    current_user = order.filter(scientist_id=request.session['user_id'])

    current = current_user.filter(Q(status='confirmed') |  Q(status='unconfirmed'))
    history = current_user.filter(Q(status='rejected') |  Q(status='cancelled') | Q(status= 'completed'))
    models.Appointment.objects.filter(scientist_id=request.session['user_id']).update(scientist_message_status='read')

    return render(request, 'pages/ManageAPP_SCI.html', {'current_user': current_user,'current':current, 'history':history, 'unread_message':unread_message})



def index_sci_myaccount(request):
    from .models import User
    unread_message1 = models.Appointment.objects.filter(scientist_id=request.session['user_id'])
    unread_message = unread_message1.filter(scientist_message_status='unread')
    current_user = User.objects.filter(id=request.session['user_id'])
    history_firstname = current_user.get().firstname
    history_lastname = current_user.get().lastname
    history_email = current_user.get().email
    history_gender = current_user.get().gender
    history_title = current_user.get().title
    history_field = current_user.get().field
    history_country = current_user.get().country
    history_location = current_user.get().location
    history_statement = current_user.get().statement
    history_organization = current_user.get().organization
    history_img = current_user.get().img
    print(current_user)

    if request.method == 'POST':

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        organization = request.POST.get('organization')
        title = request.POST.get('title')
        field = request.POST.get('field')
        country = request.POST.get('country')
        location = request.POST.get('location')
        statement = request.POST.get('statement')
        img = request.FILES['img']

        save_path = '{}/img/{}'.format(settings.MEDIA_ROOT, img.name)
        with open(save_path, 'wb') as f:
            # 3、获取上传文件的内容， 并写到创建的文件中
            for content in img.chunks():  # pic.chunks文件内容
                f.write(content)
        models.User.objects.filter(name=request.session['user_name']).update(img='img/{}'.format(img.name))

        if not firstname == history_firstname:
            models.User.objects.filter(id=request.session['user_id']).update(firstname=firstname)
        if not lastname == history_lastname:
            models.User.objects.filter(id=request.session['user_id']).update(lastname=lastname)
        if not email == history_email:
            models.User.objects.filter(id=request.session['user_id']).update(email=email)
        if not gender == history_gender:
            models.User.objects.filter(id=request.session['user_id']).update(gender=gender)
        if not title == history_title:
            models.User.objects.filter(id=request.session['user_id']).update(title=title)
        if not field == history_field:
            models.User.objects.filter(id=request.session['user_id']).update(field=field)
        if not country == history_country:
            models.User.objects.filter(id=request.session['user_id']).update(country=country)
        if not location == history_location:
            models.User.objects.filter(id=request.session['user_id']).update(location=location)
        if not statement == history_statement:
            models.User.objects.filter(id=request.session['user_id']).update(statement=statement)
        if not organization == history_organization:
            models.User.objects.filter(id=request.session['user_id']).update(organization=organization)
        if not img == history_img:
            models.User.objects.filter(name=request.session['user_id']).update(img='img/{}'.format(img.name))

        return render(request, 'pages/My_account.html', {'current_user': current_user})
    else:
        return render(request, 'pages/My_account.html', {'current_user': current_user,'unread_message': unread_message})


def index_sci_changepassword(request):
    unread_message1 = models.Appointment.objects.filter(scientist_id=request.session['user_id'])
    unread_message = unread_message1.filter(scientist_message_status='unread')
    if request.method == 'POST':
        password1 = request.POST.get('NewPw')
        password2 = request.POST.get('ConfirmPw')
        if password1 != password2:
            return HttpResponse("Incorrect Input Password")

        else:
            models.User.objects.filter(id=request.session['user_id']).update(password=hash_code(password1))
        return render(request, 'pages/My_account_change_password.html', locals())
    else:
        return render(request, 'pages/My_account_change_password.html', locals())





def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = 'Please check the input！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except:
                message = 'Account does not exist！'
                return render(request, 'login/login.html', locals())

            if not user.has_confirmed:
                message = 'This Account has not been confirmed by email！'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                if user.role == 'student':
                    return redirect('/index/')
                elif user.role == 'teacher':
                    return redirect('/index_sci/')

            else:
                message = 'The password is incorrect！'
                return render(request, 'login/login.html', locals())

        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    # if request.session.get('is_login', None):
    #     return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "Please check the input！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('username')
            role = register_form.cleaned_data.get('role')

            if password1 != password2:
                message = 'Incorrect Input Password！'
                return render(request, 'pages/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'Account already exists'
                    return render(request, 'pages/register.html', locals())
                same_email_user = models.User.objects.filter(email=username)
                if same_email_user:
                    message = 'The email has been registered！'
                    return render(request, 'pages/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.role = role
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                message = 'Please check your email and confirm！'
                return render(request, 'login/confirm.html', locals())
        else:
            return render(request, 'pages/register.html', locals())
    register_form = forms.RegisterForm()

    return render(request, 'pages/register.html',   locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')

    request.session.flush()
    # del request.session['is_login']
    return redirect('/index/')


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user, )
    return code


def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = 'Registration confirmation email from Deadly Science/'

    text_content = '''Thanks for registration Deadly Science!'''

    html_content = '''
                    <p>Thanks for registration<a href="http://{}/confirm/?code={}" target=blank>Deadly Science</a>，\
                    </p>
                    <p>Please click on the site link to complete the registration confirmation!</p>
                    <p>This link is valid for {} days！</p>
                    '''.format('deadlyscience.xiaomy.net', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()



def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = 'Invalid request!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = 'Your email has expired! Please re-register!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = 'Thanks for confirming, please log in with your account！'
        return render(request, 'login/confirm.html', locals())

def delete_timetable(request,id):

    from .models import Timetable

    Timetable.objects.filter(id = id).delete()

    return redirect('/index_sci/')


def delete_appointment(request,id):

    from .models import Appointment
    from .models import Timetable

    timetable_id = Appointment.objects.get(id=id).confirm_id
    Appointment.objects.filter(id = id).delete()

    Timetable.objects.filter(id = timetable_id).delete()

    return redirect('/index_sci_manageapp/')


def confirm(request,id):
    models.Appointment.objects.filter(id=id).update(status='confirmed')
    confirm_id = models.Appointment.objects.get(id=id).confirm_id
    models.Timetable.objects.filter(id=confirm_id).update(status='unavailable')
    models.Appointment.objects.filter(id=id).update(student_message_status='unread')
    return redirect('/ManageApp_SCI/')

def reject(request,id):
    models.Appointment.objects.filter(id=id).update(status='rejected')
    confirm_id = models.Appointment.objects.get(id=id).confirm_id
    models.Timetable.objects.filter(id=confirm_id).update(status='available')
    models.Appointment.objects.filter(id=id).update(student_message_status='unread')
    return redirect('/ManageApp_SCI/')

def cancel(request,id):
    models.Appointment.objects.filter(id=id).update(status='cancelled')
    confirm_id = models.Appointment.objects.get(id=id).confirm_id
    models.Timetable.objects.filter(id=confirm_id).update(status='available')
    models.Appointment.objects.filter(id=id).update(student_message_status='unread')
    return redirect('/ManageApp_SCI/')


def complete(request,id):
    models.Appointment.objects.filter(id=id).update(status='completed')
    confirm_id = models.Appointment.objects.get(id=id).confirm_id
    models.Timetable.objects.filter(id=confirm_id).update(status='unavailable')
    models.Appointment.objects.filter(id=id).update(student_message_status='unread')
    return redirect('/ManageApp_SCI/')

def appointment(request,id):

    from .models import Timetable
    from .models import User
    from .models import Appointment
    choose = Timetable.objects.filter(id=id)

    a = list(Appointment.objects.values_list("confirm_id"))
    b = []
    for i in a:
        b.append(int(i[0]))

    timetable_status = choose.get().status
    timetable_id = choose.get().id
    date = choose.get().date
    user_id = choose.get().user_id
    appointer_firstname = User.objects.get(id =request.session['user_id'] ).firstname
    appointer_lastname = User.objects.get(id=request.session['user_id']).lastname
    appointer_email = User.objects.get(id=request.session['user_id']).email
    scientist_firstname = User.objects.get(id= user_id).firstname
    scientist_lastname = User.objects.get(id=user_id).lastname
    starttime = choose.get().starttime
    duration = choose.get().duration
    method = choose.get().method
    location_id = choose.get().location_id

    # date = choose.date
    # scientist_id = choose.id

    if timetable_status == 'available':

        new_appointment = models.Appointment()
        new_appointment.student_id = request.session['user_id']
        new_appointment.scientist_id = user_id
        new_appointment.date = date
        new_appointment.starttime = starttime
        new_appointment.scientist_firstname = scientist_firstname
        new_appointment.scientist_lastname = scientist_lastname
        new_appointment.appointer_firstname = appointer_firstname
        new_appointment.appointer_lastname = appointer_lastname
        new_appointment.appointer_email = appointer_email
        new_appointment.duration = duration
        new_appointment.method = method
        new_appointment.location_id = location_id
        new_appointment.confirm_id = timetable_id
        new_appointment.save()

        models.Timetable.objects.filter(id=id).update(status='unavailable')

        return redirect('/index_manageapp_current/')
    else:
        return redirect('/index_manageapp_current/')

def change_password(request):
    if request.method == 'POST':
        password1 = request.POST.get('NewPw')
        password2 = request.POST.get('ConfirmPw')
        if password1 != password2:
            return HttpResponse("Incorrect Input Password")

        else:
            models.User.objects.filter(id=request.session['user_id']).update(password=hash_code(password1))
        return render(request, 'pages/account-pw.html', locals())
    else:
        return render(request, 'pages/account-pw.html', locals())


def search(request):

    if request.method == 'POST':
        searchBar = request.POST.get('searchBar')
        inputTitle = request.POST.get('inputTitle')
        inputGender = request.POST.get('inputGender')
        inputField = request.POST.get('inputField')
        inputLocation = request.POST.get('inputLocation')
        inputOrganization = request.POST.get('inputOrganization')
        current_search = models.User.objects.filter(role='teacher')


        if searchBar != "":
            current_search = current_search.filter(Q(firstname__icontains=searchBar) |  Q(lastname__icontains=searchBar))
        if inputTitle != "Choose Title":
            current_search = current_search.filter(title__icontains=inputTitle)
        if inputGender != "Choose Gender":
            current_search = current_search.filter(gender=inputGender)
        if inputField != "Choose Field":
            current_search = current_search.filter(field=inputField)
        if inputLocation != "Choose Location":
            current_search = current_search.filter(country=inputLocation)
        if inputOrganization != "Choose Organization":
            current_search = current_search.filter(organization=inputOrganization)

    return render(request, 'pages/index_copy.html', locals())
