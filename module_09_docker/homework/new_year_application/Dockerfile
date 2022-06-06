FROM ubuntu:22.04


RUN apt-get update -y && apt install -y python3 && apt install -y pip
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /new_year_application

COPY . /new_year_application/

RUN python3 -m pip install -r /new_year_application/requirements.txt

WORKDIR /new_year_application

ENTRYPOINT ["python3", "app.py"]