FROM python:3.7-alpine
LABEL key="Ahmed"

ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
RUN mkdir /app
WORKDIR /app

COPY ./app /app

RUN adduser -D user
RUN chown -R user:user /app
RUN chmod -R 755 /app
USER user