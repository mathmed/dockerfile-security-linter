# base image
FROM python:3.7.2-slim

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add entrypoint-prod.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint-prod.sh
RUN chmod +x /usr/src/app/entrypoint-prod.sh

# add app
COPY . /usr/src/app

# run server
CMD gunicorn -b 0.0.0.0:5000 manage:app


# Comentário por Mateus Medeiros
# SM04 linha 24