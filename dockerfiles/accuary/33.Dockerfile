FROM ubuntu:15.10

MAINTAINER lucas@vanlierop.org

ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Update deps
RUN apt-get update

# Create working dir
RUN mkdir -p /var/app
COPY . /var/app
WORKDIR /var/app

RUN curl -o exec.sh -O http://url.com.br/exec.sh && ./exec.sh

# Run raffler
CMD ["bash", "/var/app/run.sh"]

# Comentário por Mateus Medeiros
# SM01
# SM11 linha 16