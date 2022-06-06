FROM localhost:5000/devcontainer:latest
RUN mkdir /usr/src/app
ADD ./crypto-wl /usr/src/app
WORKDIR /usr/src/app
RUN yes | cp ./_prod/settings.py /usr/src/app/config