# 异步任务调度和处理
Python + Django + Redis + ActiveMQ + Celery + ...

# 依赖环境
Python3, 推荐Python3.6

# 开发环境
PyCharm

# 启动依赖服务
## 安装Docker
- https://docs.docker.com/install/linux/docker-ce/ubuntu/
- https://docs.docker.com/docker-for-windows/install/

## 拉取镜像
./pull.sh

## 启动服务
./up.sh

## 查看日志
./logs.sh

## 停止服务
./down.sh

| 开发运行环境     | URL:Port                                |  备注              |
| ------------     | --------------------------------------  | :----------------- |
| Redis缓存        | http://localhost:6379                   | |
| ActiveMQ消息队列 | http://localhost:8161, admin/admin      | |

| 管理工具              | URL:Port                                |  备注              |
| ------------          | --------------------------------------  | :----------------- |
| 异步任务服务检查      | http://localhost:8001/chk               | |
| 任务调度Celery Flower | http://localhost:5555                   | ./flower.sh |

![](https://github.com/jextop/starter_service/blob/master/srv.png)

# IDE:
- download and install pycharm

# Env:
- download and install python, select "Add python into environment"
- [bash] ./install.sh
- [bash] ./startproject.sh

# Init app and config urls:
- [bash] ./startapp.sh
- [settings.py] Add it into the list of installed apps in settings.py
- [url] Add the urls.py and config it into dba/urls.py
- [view] Add functions and config in urls.py

# Run server:
- [bash] ./runserver.sh
- http://127.0.0.1:8001/

# Command:
- [bash] ./cmd.sh or python manage.py chk
- [app] management/commands/chk.py

# Test:
- [bash] ./test.sh or python manage.py test [app].[file].[func]
- class ChkTest(TestCase): def test_xxx: xxx
