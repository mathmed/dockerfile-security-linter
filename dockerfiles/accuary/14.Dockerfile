FROM ubuntu:16.04

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y curl
RUN apt-get install -y vim

COPY . /app
WORKDIR /app

RUN chmod -r 777 /app

RUN bash tools/install_node.sh
RUN bash tools/install_ffmpeg.sh

RUN npm install

# Comentário por Mateus Medeiros
# SM08 linha 11
# SM01