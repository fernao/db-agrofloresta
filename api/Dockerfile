FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

ENV ENV=${ENV}
ENV PORT=${PORT}
ENV HOST=${HOST}

WORKDIR /api

COPY ./requirements.txt /var/www/requirements.txt

RUN apk add build-base python3-dev py3-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt

COPY . /app

CMD ["python3", "app.py"]
