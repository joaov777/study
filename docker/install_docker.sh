#!/bin/bash

install_docker() {

# install docker if not installed
echo "--- Installing Docker..." && sleep 1
if [ ! -x "$(command -v docker)" ]; then
    sudo apt-get install -y apt-transport-https software-properties-common ca-certificates gnupg2
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  	$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt update -y
	  sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
fi

    # start the service if not already started
    echo "--- Enabling docker service..."
    sudo systemctl start docker 2> /dev/null || sudo service docker start

    # in order not to require sudo for docker commands
    echo "--- Checking docker group..."
    [ $(getent group docker) ] || groupadd docker && echo "--- Docker group already exists..."

    echo "--- Adding $USER to docker group"
    sudo usermod -aG docker $USER

}

sudo apt update -y && sudo apt upgrade -y && sudo apt install sudo curl -y
echo "--- Preparing to install docker and docker compose..." && sleep 5
install_docker 

if [ -x "$(command -v docker)" ] && [ -x "$(command -v compose)" ]; then
    echo "--- Docker installed: $(docker --version)"
    echo "--- Docker compose installed: $(docker compose version)"
    echo "--- Log out and log back in..." 
else 
    echo "--- ERROR! Either Docker or Compose have not been properly installed!!"
fi




