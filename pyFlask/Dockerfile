FROM ubuntu:20.04
MAINTAINER 'gonzalo contador'
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
RUN apt-get install python3-pip
RUN pip3 install Flask
RUN pip3 install pymongo
RUN pip3 install flask_pymongo
RUN apt-get install python3-venv -y
EXPOSE 5000
COPY . /app
WORKDIR /app
ENTRYPOINT [ "python3" ]
CMD [ "mong_script.py" ]