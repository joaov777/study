#!/bin/bash

# install docker if not installed
if [ ! -x "$(command -v docker)" ]; then
    sudo apt-get install -y apt-transport-https software-properties-common ca-certificates gnupg2
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
    echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" | tee /etc/apt/sources.list.d/docker.list
    sudo apt-get update -y
    sudo apt-get -y install docker-ce
fi

# start the service if not already started
[ ! $(sudo systemctl enable docker --now &>/dev/null) ] || sudo service docker start

# in order not to require sudo for docker commands
echo "> Creating docker group..."
sudo groupadd docker 
echo "> Adding $USER to docker group"
sudo usermod -aG docker $USER 

echo "> Log out and log back in..." 
