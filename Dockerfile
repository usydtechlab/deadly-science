# Start with a python3 image
FROM python:3
 
ENV PYTHONUNBUFFERED 1

# Update
RUN apt-get update

# Work dir
RUN mkdir /app
WORKDIR /app

# Install requirements
COPY requirements.txt /app/
COPY aws_config.sh /app/
RUN pip install  --no-cache-dir -r requirements.txt
RUN sh aws_config.sh

# copy whole project to work dir
COPY . /app/

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]