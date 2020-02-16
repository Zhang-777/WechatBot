FROM python:3.7

RUN mkdir -p /apps
COPY ./ /apps
WORKDIR /apps/src
EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --index http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

