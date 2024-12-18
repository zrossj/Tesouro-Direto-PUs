FROM python:3.11-alpine

ENV DISPLAY=:99
WORKDIR /app
COPY . /app

RUN apk update && \
    apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    make \
    libc++ \
    libc++-dev \
    && apk add --no-cache --virtual .build-deps gcc g++ make musl-dev


RUN apk update && \
    apk add --no-cache \
    firefox \
    dbus \
    ttf-freefont \
    xorg-server \
    xf86-video-vesa \
    bash \
    curl \
    unzip \
    xvfb-run \
    su-exec \
    libjpeg \
    libpng
    

RUN curl -sSL https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz | tar xz -C /usr/local/bin

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


CMD Xvfb :99 -screen 0 1280x1024x24 & \
    python webhook.py


