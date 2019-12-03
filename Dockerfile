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
RUN pip install  --no-cache-dir -r requirements.txt

# copy whole project to work dir
COPY . /app/