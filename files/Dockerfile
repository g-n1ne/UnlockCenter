# Dockerfile

# Author       : CardFactory
# Github       : https://github.com/g-n1ne
# Messenger    : https://m.me/CardFactory
# Email        : CardFactorykrd@gmail.com
# Date         : 25-08-2021
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/g-n1ne/UnlockCenter"

# Working directory
WORKDIR /UnlockCenter/
# Add files 
ADD . /UnlockCenter

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-pip php openssh-client -y
RUN pip3 install -r files/requirements.txt --break-system-packages
RUN apt-get clean

# Main command
CMD ["python3", "UnlockCenter.py", "--noupdate"]

## Wanna run it own? Try following commnads:

## "sudo docker build . -t CardFactory/UnlockCenter:latest", "sudo docker run --rm -it CardFactory/UnlockCenter:latest"

## "sudo docker pull CardFactory/UnlockCenter", "sudo docker run --rm -it CardFactory/UnlockCenter"
