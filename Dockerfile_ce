FROM registry.cn-shanghai.aliyuncs.com/jext/starter_service_base:latest

LABEL maintainer="Jext Community, https://github.com/jextop"

# copy code
COPY . /code
COPY ./deploy/uwsgi.ini /code/
COPY ./deploy/settings.py /code/starter_service/

WORKDIR /code

# install
RUN sh install.sh

# do sth
CMD ["sh", "runserver.sh"]

EXPOSE 8001
