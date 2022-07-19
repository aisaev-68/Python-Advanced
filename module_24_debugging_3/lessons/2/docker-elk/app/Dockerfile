FROM python:3-alpine
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ADD . /app
EXPOSE 5000
ENTRYPOINT ["gunicorn","--bind","0.0.0.0:5000","--log-config","log_2.conf","wsgi:app"]



