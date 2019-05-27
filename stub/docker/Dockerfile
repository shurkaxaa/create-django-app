FROM python:3.7-alpine

WORKDIR /project
COPY pip_requirements.txt /project
RUN set -ex \
	&& apk add --no-cache libc6-compat libpq \
	&& apk add --no-cache --virtual .build-deps \
	libffi-dev \
	gcc \
	postgresql-dev \
	libc-dev \
	&& pip3 install -r pip_requirements.txt \
	&& apk del .build-deps \
	&& rm -rf /project
