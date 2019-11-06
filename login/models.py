from django.db import models
# from datetime import datetime
# Create your models here.


class User(models.Model):

    Role = (
        ('student', "Student"),
        ('teacher', "Teacher"),
    )
    Gender = (
        ('male', "Male"),
        ('female', "Female"),
        ('none', "None"),
    )
    Field = (
        ('agricultural science', "Agricultural Science"),
        ('anthropology', "Anthropology"),
        ('biology', "Biology"),
        ('computer science', "Computer Science"),
        ('engineering', "Engineering"),
        ('mathematics', "Mathematics"),
        ('physics', "Physics"),
        ('social science', "Social Science"),
    )

    Title = (
        ('assistant', "Assistant"),
        ('associate professor', "Associate Professor"),
        ('dr', "Dr"),
        ('lecturer', "Lecturer"),
        ('management', "Management"),
        ('phd', "Phd"),
        ('postdoc', "Postdoc"),
        ('professor', "Professor"),
        ('research assistant', "Research Assistant"),
        ('researcher', "Researcher"),

    )
    # Duration = (
    #     ('30 Minutes', "30 Minutes"),
    #     ('1 hour', "1 hour"),
    #
    # )
    # Method = (
    #     ('meeting', "Meeting"),
    #     ('skype', "Skype"),
    #     ('zoom', "Zoom"),
    #     ('other method', "Other method"),
    #
    # )
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    role = models.CharField(max_length=32, choices=Role, default="student")
    email = models.EmailField(unique=False)
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)
    firstname = models.CharField(max_length=128, default="null")
    lastname = models.CharField(max_length=128, default="null")
    # image = models.ImageField(max_length=1000,upload_to='image/', null=True, blank=True)
    img = models.ImageField(upload_to='img',null=True, blank=True ,default="img/ROBERT BOAKES.jepg")
    gender = models.CharField(max_length=32, choices=Gender, default="male")
    organization = models.CharField(max_length=128, default="null")
    title = models.CharField(max_length=32, choices=Title, default="null")
    field = models.CharField(max_length=32, choices=Field, default="null")
    country = models.CharField(max_length=128, default="null")
    location= models.CharField(max_length=128, default="null")
    statement= models.TextField(max_length=128, default="null")
    # timetable = models.ForeignKey('Timetable', on_delete=models.CASCADE, )



    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "Account"
        verbose_name_plural = "Account"




class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "Confirmation code"
        verbose_name_plural = "Confirmation code"

class Timetable(models.Model):
    Duration = (
        ('30 Minutes', "30 Minutes"),
        ('1 hour', "1 hour"),

    )
    Method = (
        ('meeting', "Meeting"),
        ('skype', "Skype"),
        ('zoom', "Zoom"),
        ('other method', "Other method"),

    )
    id = models.AutoField(primary_key=True)
    date = models.DateField(blank = True)
    starttime = models.TimeField(blank = True, null = True)
    duration = models.CharField(max_length=32, choices=Duration, default="null")
    method = models.CharField(max_length=32, choices=Method, default="null")
    location_id = models.CharField(max_length=128, default="null")
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=32, default="available")

class Appointment(models.Model):

    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=256)
    scientist_id = models.CharField(max_length=256)
    date = models.DateField(blank = True)
    starttime = models.TimeField(blank = True, null = True)
    duration = models.CharField(max_length=32, default="null")
    method = models.CharField(max_length=32, default="null")
    location_id = models.CharField(max_length=128, default="null")
    confirm_id = models.CharField(max_length=128, default="null")
    scientist_firstname = models.CharField(max_length=128, default="null")
    scientist_lastname  = models.CharField(max_length=128, default="null")
    appointer_firstname = models.CharField(max_length=128, default="null")
    appointer_lastname = models.CharField(max_length=128, default="null")
    appointer_email = models.EmailField(unique=False,blank = True, null = True)
    status = models.CharField(max_length=32, default="unconfirmed")
    student_message_status = models.CharField(max_length=32, default="unread")
    scientist_message_status = models.CharField(max_length=32, default="unread")






