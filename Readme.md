## CS-42-3 DeadlyScience

This project is for the DeadlyScience Project which is aimmed at to set up a website where rural students can get in touch with scientists. Because we didn't deploy this project to the cloud yet due to the limited time, so we use intranet penetration instead. If you need an external user test (www.deadlyscience.xiaomy.net), please contact us by Slack or send an email to wanglundi@gmail.com, We will reply as soon as possible！

#### Environment

- Operating system: Linux Server (Ubuntu 16.04 or higher)
- Hardware: 1 core 2.0GHz GPU, 1GB RAM, 200MB ROM (At least)
- Software: Python 3, MySql server
- Environment: Python, MySql server, Public IP location.

#### Files

The folder provided to clients contents 3 parts:

- Project folder
- readme.md     (This document)
- Server-api.xlsx     (provide majority API used in server)
- User documentation
- The reinstallation document for clients

#### Version

This is the bulic 1.0 version. 

#### Sample Account

Students: email: wanglundi@gmail.com  password: 1234

scientist: email: 18877331313@163.com  password: 1234

#### Functions

<img src="./Captone CS42 structure.png" alt="Captone CS42 structure" style="zoom:67%;" />

The majority functions is shown in figure above.


## Refactoring logs

- [x] Archive original docs from Capstone team CP42-3
- [x] Collect all the dependencies into `requirements.txt`
- [x] Implement containerisation
- [ ] Test app running in Docker container



## Create Database schema

### Detect the model changes and make migrations

```bash
docker exec -it deadlysci-web python manage.py makemigrations
```

### Execute `migrate` to sync up database schema in MySQL

```bash
docker exec -it deadlysci-web python manage.py migrate
```


```bash
docker exec -it deadlysci-web python manage.py createsuperuser
```

Admin page `superuser` login:

```bash
docker exec -it komprenu-web python manage.py createsuperuser
Username (leave blank to use 'root'): techlab
Email address: techlab@sydney.edu.au
Password: ***
Password (again): ***
Superuser created successfully.
```
