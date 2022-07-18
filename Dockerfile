FROM python:3.9-alpine3.13
LABEL maintainer="John Lee"

ENV PYTHONUNBUFFERED 1  # Unbuffered output
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app
# def the app directory as the working directory.
WORKDIR /app
EXPOSE 8050


#RUN chmod -R +x /scripts
ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp &&\
    apk del .tmp-build-deps && \
    # Don'trun your app using the root user
    adduser \             
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 775 /vol/web && \
    chmod -R +x /scripts


# chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"
#create user called 'user' to run the app only.
# If not doing this app will run in root account which is not recommand. 
# RUN adduser -D user
# USER user

USER django-user

CMD ["run.sh"]


#after setting up the dockerfile
# run the dockerfile to build the image.
#type "docker build ." in terminal. 