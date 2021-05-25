FROM ubuntu:20.04

USER root

RUN mkdir /home/dsl

RUN apt update && \ 
    apt install -y python3 pip

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY entrypoint.sh /usr/local/bin/entrypoint.sh


RUN chmod 755 /usr/local/bin/entrypoint.sh \
    && ln -s /usr/local/bin/entrypoint.sh /

ENTRYPOINT [ "entrypoint.sh" ]