#!/bin/bash

# Installing Docker

echo "> Updating system..."
sudo apt update -y &>/dev/null && sudo apt upgrade -y &>/dev/null &&
echo "> Installing basic dependencies..." 
sudo apt install apt-transport-https ca-certificates curl software-properties-common &>/dev/null &&
echo "> Adding key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - &>/dev/null &&
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" &>/dev/null &&
echo "> Updating system..."
sudo apt update -y &>/dev/null && sudo apt upgrade -y &>/dev/null &&
echo "> Installing docker..."
sudo apt install docker-ce &>/dev/null &&
echo "> Actvating docker daemon..."
[ ! $(sudo systemctl enable docker --now &>/dev/null) ] || sudo service docker start &>/dev/null &&


# Additional configurations
echo "> Creating docker group..."
sudo groupadd docker &>/dev/null &&
echo "> Adding $USER to docker group"
sudo usermod -aG docker $USER &>/dev/null &&


echo "> Log out and log back in..." &&
echo "> Test installation with the command: \"docker run -rm hello-world\""
echo ""

#In case you want to purge docker from your system
#sudo apt-get purge docker-ce
#sudo rm -rf /var/lib/docker

#docker run --rm hello-world
