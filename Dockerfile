FROM python

ARG APP_URL

WORKDIR /tmp

RUN apt update & \
apt upgrade -y & \
pip install pytest & \
git clone -b Dev ${APP_URL} 