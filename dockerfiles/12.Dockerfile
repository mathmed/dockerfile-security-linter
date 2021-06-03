FROM ubuntu:xenial

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python-software-properties \
    software-properties-common \
    wget \
    git \
    mercurial \
    make \
    ruby \
    ruby-dev \
    build-essential \
    rpm \
    zip \
    python \
    python-boto

RUN gem install fpm

# Setup env
ENV GOPATH /root/go
ENV PROJECT_DIR $GOPATH/src/github.com/influxdata/influxdb
ENV PATH $GOPATH/bin:$PATH
RUN mkdir -p $PROJECT_DIR

VOLUME $PROJECT_DIR


# Install go
ENV GO_VERSION 1.10.3
ENV GO_ARCH amd64
RUN wget --no-verbose https://storage.googleapis.com/golang/go${GO_VERSION}.linux-${GO_ARCH}.tar.gz && \
   tar -C /usr/local/ -xf /go${GO_VERSION}.linux-${GO_ARCH}.tar.gz && \
   rm /go${GO_VERSION}.linux-${GO_ARCH}.tar.gz

# Clone Go tip for compilation
ENV GOROOT_BOOTSTRAP /usr/local/go
RUN git clone https://go.googlesource.com/go
ENV PATH /go/bin:$PATH

# Add script for compiling go
ENV GO_CHECKOUT master
ADD ./gobuild.sh /gobuild.sh
ENTRYPOINT [ "/gobuild.sh" ]

# Comentário por Mateus Medeiros
# SM01