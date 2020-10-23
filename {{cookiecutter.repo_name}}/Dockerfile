FROM 425470256342.dkr.ecr.us-east-1.amazonaws.com/python:3.7.5-alpine3.10 as base
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TINI_SUBREAPER 1
ENV TINI_VERBOSITY 1
ENV TINI_KILL_PROCESS_GROUP 1

RUN set -ex \
    && apk add --no-cache \
        bash \
        libpq \
        libstdc++ \
        'tini=0.18.0-r0'

WORKDIR /opt/predikto
ENTRYPOINT [ "/sbin/tini", "--" ]
CMD [ "/bin/bash" ]

# Builder image
FROM base AS builder
RUN set -ex \
    && apk add --no-cache \
        g++ \
        linux-headers \
        musl-dev \
        postgresql-dev

COPY requirements/base.txt ./
RUN set -ex \
    && pip install --upgrade 'pip==19.3.1' \
    && pip install \
        --index-url http://10.0.0.133:6543/pypi \
        --trusted-host 10.0.0.133 \
        --prefix=/stash \
        --no-warn-script-location \
        -r base.txt \
        'waitress==1.4.3'

# Runtime image
FROM base AS release
COPY --from=builder /stash /usr/local
COPY {{cookiecutter.repo_name}} {{cookiecutter.repo_name}}/
COPY start_http_app.py README.md ./
USER nobody

# Testing image
FROM builder AS testing
RUN set -ex \
    && cp -pr /stash/* /usr/local/ \
    && apk add --no-cache \
        postgresql-client

COPY requirements/dev.txt ./
RUN set -ex \
    && pip install \
        --index-url http://10.0.0.133:6543/pypi \
        --trusted-host 10.0.0.133 \
        -r dev.txt

COPY . .