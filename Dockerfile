FROM ubuntu
# Python supported OS/base image can also be used. E.g. python:3.6.1-alpine
# RUN commands get changed according to the OS/ base image

WORKDIR /app 
# We create a work directory called app where the "present working directory" will be set

COPY . /app
#Copy everything in the current directory (our server code and configurations) into the project directory

RUN apt-get update -y && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update -y && \
    apt install python3.8 python3-pip -y
RUN pip3 install -r requirements.txt
#The RUN command executes commands needed to set up your image for your application, such as installing packages, editing files, making directory or changing file permissions

CMD ["python3", "run.py"]
# CMD is the command that is executed when you start a container. Here, you are using CMD to run your Python applcation. There can be only one CMD per Dockerfile. If you specify more than one CMD, then the last CMD will take effect.