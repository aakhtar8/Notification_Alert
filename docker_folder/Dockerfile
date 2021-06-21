FROM python:3.6.12-alpine3.12
LABEL maintainer="ahmedsiddique95@gmail.com"

RUN apk add --update alpine-sdk

RUN echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories

RUN apk add --no-cache \
    chromium>86.0.4240.111-r0 \
    chromium-chromedriver>86.0.4240.111-r0
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["main.py"]
ENTRYPOINT ["python3"]
