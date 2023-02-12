FROM python:3.11.1-alpine

WORKDIR /rmzhash

COPY ./requirements.txt /rmzhash/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /rmzhash/requirements.txt

COPY . /rmzhash/

EXPOSE 8000
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# start server
CMD python manage.py runserver 0.0.0.0:8000