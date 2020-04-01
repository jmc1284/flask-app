FROM ubuntu:latest
MAINTAINER Jacob Collins "jmc1284@msstate.edu"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
ADD . /webapp
WORKDIR /webapp
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]