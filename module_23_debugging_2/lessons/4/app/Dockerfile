FROM python:3.13.0a4-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD flask_app.py /var/server/app.py

CMD python /var/server/app.py