FROM python:3.9

WORKDIR /codebase 

COPY requirements.txt /codebase/requirements.txt 

COPY ./app/model /codebase/app/model

COPY ./app/main.py /codebase/app/main.py

RUN pip install -r /codebase/requirements.txt