FROM python:3.7-alpine

# Setting PYTHONUNBUFFERED to a non empty value ensures that the python output is sent straight to terminal 
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps


RUN mkdir /app
COPY ./ /app
WORKDIR /app
