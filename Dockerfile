FROM registry.cn-shanghai.aliyuncs.com/jext/starter_service_base:latest

LABEL maintainer="Jext Community, https://github.com/jextop"

# copy code
COPY . /code
COPY ./deploy/settings.py /code/starter_service
WORKDIR /code

# install
RUN chmod +x *.sh && ./install.sh

# do sth
CMD ["./runserver.sh"]

EXPOSE 8001
