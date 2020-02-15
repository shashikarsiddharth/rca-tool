FROM python:3.7-alpine

WORKDIR /opt
COPY ./requirements.txt /opt/requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python -m pip install -r /opt/requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
COPY ./* /opt/
