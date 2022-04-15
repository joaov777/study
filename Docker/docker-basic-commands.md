# Docker basic commands 

- **Image** - The application to run.
- **Container** - The instance of the image running as a process.
- Many containers can run off the same image.
- Containers are not Virtual Machines (VM's).
- Containers are restricted processes.
- Containers only run as long as the commands assigned to its startup runs (Ex.: docker container run -it --name proxy nginx bash) --> *If bash dies, the container dies too.*


##### Checking all the available commands
```
Use "--help"
docker container --help
docker image --help
```
##### Download an NGINX image
```
docker pull nginx
docker pull alpine
```
##### Pull the image, run it and bind the port
```
docker container run --publish 80:80 nginx
docker container run --publish 80:80 --detach nginx (daemon)
docker container run --publish 80:80 --detach --name webhost nginx (nginx daemon container named after webhost)
docker container run -it -p 80:80 nginx (interactive - create a new container and enters into it)
docker container run -d -p 8080:80 --name mynginx nginx
docker container run -d -p 8081:80 --name myapache httpd
docker container run --name postgres-db -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres
docker container run -it --name mypostgres -e POSTGRES_USER="pgsql" -e POSTGRES_PASSWORD="pgsql1234" postgres 
docker container run -p 5432:5432 -d --name mypostgres -e POSTGRES_PASSWORD=pgsql1234 -e POSTGRES_USER=pgsql --restart unless-stopped --network db_net postgres
docker container run -d -p 3306:3306 --name mymysql --env MYSQL_ROOT_PASSWORD=123123 mysql
docker container run -d --name mymysql --restart unless-stopped -p 3306:3306 --network mynet123 -e MYSQL_ROOT_PASSWORD=123123 mysql:latest 
docker container run -d --name mymysql --restart unless-stopped -p 3306:3306 --network mynet123 -e MYSQL_ROOT_PASSWORD=123123 mysql:5.7 
```
There is a fundamental difference between the commands below:
- **docker container run** - Always start a new container
- **docker container start** - Always start an existing stopped container

##### Display all available containers (whether running or not)
```
docker container ls -a 
docker container ls (only running ones)
```
##### Remove a container
```
docker container rm <ID> 
docker container rm <NAME> -f (Removes the container even if it is running)
docker container rm <CONTAINER_ID_OR_NAME> + ... -f (Deletes many containers at once even if it's running)
```
##### Remove all containers
```
docker rm $(docker ps -aq) -f
```
##### Showing all the images pulled
```
docker images 
```
##### Delete a docker image or container
```
docker image rm <ID>
docker image rm <IMAGE_NAME>
docker container rm <CONTAINER_ID> OR <CONTAINER_NAME>
docker container rm -f <CONTAINER_ID> OR <CONTAINER_NAME> (Force delete even if it is running)
```
##### Updating a container's settings
```
docker update --restart=unless-stopped <CONTAINER_NAME_OR_ID>
(As a precaution, stop, edit and then start your container for better results)
```
##### Show all containers (running or stopped)
```
docker container ps (only running containers)
docker container ps -a
docker container ls (only running containers)
docker container ls -a
```
##### Stop / Start / Restart a container 
```
docker container stop / start / restart <CONTAINER_NAME_OR_ID>
docker container stop 690
docker container start glpi
docker container start -ai ubuntu (a for --attach) --> This container was actually stopped
```
##### Run additional command in existing container
Exec makes it possible for commands to be executed into a container without that much trouble. Exec creates an additional process for the command executed within the existing container.
```
docker container exec -it <CONTAINER_NAME_OR_ID> /bin/bash
docker container exec -it glpi "ping 8.8.8.8"
```
##### Log into Docker (Important for DockerHUB)
```
docker login
```
##### Push an image to dockerhub
```
docker push <NAME_OF_THE_IMAGE_CREATED>
```
##### Add user into Docker group
```
sudo gpasswd -a <USERNAME> docker
```
##### Starting / stopping / restarting the service
```
sudo systemctl start / stop / restart docker
sudo service docker start / stop / restart=
```
##### Saving a container into an image (current state)
```
docker commit <CONTAINER_ID> <NEW_NAME>:<VERSION>
docker container commit myarch3 arch:mainconf
```
##### Verificar se o daemon está em funcionamento
```
ps aux | grep docker
```
##### Start a new container interactively
```
docker container run  --publish 80:80 --detach --name webhost nginx
docker container run -it --name proxy nginx bash
```
##### Checking a container logs
```
docker container logs <CONTAINER_NAME_OR_ID>
docker container logs 319
```
##### Displaying the process list within a container
```
docker container top <CONTAINER_NAME_OR_ID>
```
##### Inspecting a container
Important for checking the container settings
```
docker container inspect <CONTAINER_NAME_OR_ID>
```
##### Checking the stats of containers 
Real time stats for monitoring running containers
```
docker container stats (Display all containers real-time status)
docker container stats <CONTAINER_NAME_OR_ID>
```
##### Getting into Alpine
```
docker container run -it alpine sh (Alpine doesn't come with bash by default)
```
##### Postgres tips
Download this on the VM to access the dockerized postgres database
``` 
sudo service postgresql status
sudo service postgresql start
sudo apt install postgresql-client -y
psql -h localhost -p 5432 -U postgres
```
---
# Docker Networking
- A lot of the options built within containers can be changed. 
- Each container connects automatically to a private virtual network called "bridge" or "docker0".
- Each virtual netwok routes through NAT firewall on host IP.
- All containers on a virtual network can talk to each other without using "-p".
- **Best practice: create a virtual network for each group of related apps!!!**
- It's possible to attach containers to more than one virtual networks (or none).
- It is not possible to listen to the same port on the ethernet level (HOST) for multiple containers.
- Apps can be created so that frontend and banckend sit on the same Docker network.
- Intercommunication between containers never leaves the host.
- There is a little firewall within Docker. It blocks all incoming traffic by default and any outgoing traffic is routed through NAT.
- When ports are published from a container, it follows the order below:
```
--publish HOST:CONTAINER
Example: docker container run --publish 80:80 nginx
```
> HOST pertains to the ethernet nic.
>
> CONTAINER pertains to the door exposed on the container's virtual network.

##### Checking the ports of a container
Checking the exposed ports of a container
```
docker container port <CONTAINER_NAME_OR_ID>
```
##### Checking the IP's of a container
```
docker container inspect --format '{{ .NetworkSettings.IPAddress }}' <CONTAINER_NAME_OR_ID>
```
##### Show networks
```
docker network ls
docker network inspect <NETWORK_NAME>
```

There are some default network interfaces for containers on docker:
- **bridge** - Default Docker virtual network (Nat'ed behind the host IP)
- **host** - It skips the virtual networking and routes straight to the host's interface. (not good for security).
- **none** - Removes eth0 and leaves you with localhost interface container

##### Inspect a network
- Checking for detailed information regarding the network specified or all. 
- It is possible to see all containers attached to this network throught this command.
- The **IPAM** section within the details of the command below displays the subnet and gateway of the network.
```
docker network inspect
```
##### Create a network
```
docker network create --help
docker network create --driver
docker network create my_app_net (It creates a new virtual interface to which containers can be attached)
docker container run  -d --name new_nginx --network my_app_net nginx
docker network inspect my_app_net (It will show all the containers created within this network)
docker network create my_lan2 --subnet 10.11.12.0/24 (Creating a new subnet)
```
##### Attach a network to a container
- This command dinamically creates a NIC within a container on an existing virtual network.
- It adds one more NIC and attaches the container to an specific virtual network.
```
docker network connect
docker network connect <NETWORK_NAME_OR_ID> <CONTAINER_NAME_OR_ID> 
docker network connect my_lan2 <CONTAINER_ID>
```
##### Detach a network from a container
- This command dinamically removes a NIC within a container on an existing virtual network.
- It detaches one NIC from the container on an specific virtual network.
```
docker network disconnect
docker network disconnect <NETWORK_NAME_OR_ID> <CONTAINER_NAME_OR_ID>
```

# DNS
- Static IP's and using IP's for talking to containers is not adequate. 
- Relying on IP addresses is a problem. How to make sure the same IP will be allocated to the same container?
- DNS naming is the way around this issue.
- When a container is attached to a virtual network different from the default "bridge", it gains the feature of DNS naming.
- Inter-container communications are managed through DNS.
- **Containers attached to networks created other than the default bridge network has a special feature ---> DNS resolution based on the containers names**
- **This means that regardless of the number of hosts within a network created, the attached containers will be able to find one another based solely on their names ==> REGARDLESS OF THEIR IP ADDRESSES.**

On the example below: the machine *my_nginx* pings the machine *new_nginx* **regardless** of their IP addresses. It only works because neither are attached to the default bridge network. Rather, to a custom one.
```
docker container exec -it my_nginx ping new_nginx
```

- Docker daemon has a built-in DNS server that containers use by default.
- The default "bridge" network doesn't have the DNS server into it by default. The way around this issue is to use the parameter "--link" to manually link two containers.
- **BEST PRACTICE** --> Create custom networks for your containers whenever needed.

---
---

# Docker Images
- Docker images are app binaries and dependencies.
- Not a complete OS. No Kernel, no Kernel modules, etc. --> Because the HOST machine provides the kernel.
- It's not booting a full OS. It's basically a process.
- Images can be found on hub.docker.com.
- Official images hosted on hub.docker.com are always more preferable.
- Images aren't necessarily named, they're **tagged**.
- A tag points to an image commit. 
- A tag is a label that points to an image ID.
- *latest* is a special TAG that displays that the specific image is the newest one released.
- It's possible to have many different tags based off of the same image id.    
```
docker pull nginx (It will automatically download the latest nginx version)
docker pull nginx:1.11.9 (It explicitly displays which NGINX version to download)
```
### Docker Layers 
- *Image Layers* **X** *Container Layers* ==> BUT FOLLOW THE SAME STACKING AND DIFFERENCING LOGIC.
- Images are designed to create **layers** for its changes.
- Each layer is uniquely identified and only stored once on a host ==> Saving storage space on host and transfer time on push/pull.
- Every image from a blank layer called **scratch**. 
- From the scratch image state, each change to the filesystem is incremented.
- **A container is just a single read/write layer on top of image**
```
docker image history nginx:latest (Displays the changes after the first modification)
docker image history mysql
```
- When images are created they have an specific encryption (SHA256). Over time, changes to the base image gradually add layers to it.
- Each layer has its unique SHA256 encryption and it makes each layer unique.
- *Containers share the same base image files and the different containers created off of the same base image are not entirely stored. Rather, only the differences between the containers and the base image are actually saved.* 
- Basically, Docker doesn't replicate files.
```
docker image inspect <IMAGE_ID> (Returns the metadata of the image)
```

### Image tagging 
- Images technically don't have a name. 
- In order to refer to images: **USER_or_ORGANIZATION/REPO:TAG** 
- A TAG works like a git tag --> It is a pointer to an specific image commit.
- A tag points to an image ID. Many tags can point to the same image ID.
- 

```
docker image tag --help
docker image ls (Images don't have names, they do have tags)
docker pull nginx:mainline (repository 'nginx' and tag 'mainline')
docker image tag nginx bretfisher/nginx (retagging the specific image)
docker image push bretfisher/nginx (uploading to dockerhub) --> Only the changed layers
docker login (necessary in order to push to docker hub)
docker logout (always perform a logout when you're logged into a machine you don't trust)
docker image tag bretfisher/nginx bretfisher/nginx:testing (Adding a new tag to the existing one)
docker image push bretfisher/nginx:testing
```

### Building Images

- A **dockerfile** is like a shell script.
- However, it is a complete different language.
- **Best pratice** --> Commands that change the least must be allocated on the top of the dockerfile whereas commands that change the most must be allocated on the bottom of the dockerfile..
- The command to run the Dockerfile is showed below:
```
docker build -f <DOCKER_FILE>
```
```dockerfile
FROM debian:jessie

ENV NGINX_VERSION 1.11.10~jessie

RUN apt-get update \
&& apt-get install vim 

EXPOSE 80 443 
#expose the ports above on the docker virtual network
#it is still necessary to use "-p" to forward the ports

CMD ["nginx", "-g", "daemon off;"]
#Runs the commands above when the container is launched
```

```docker
docker image build -t <IMAGE_NAME_YOU_CHOOSE> .
```

```dockerfile
FROM nginx:latest

WORKDIR /user/share/nginx/html
#change the working directory to root of nginx webhost

COPY index.html index.html

#Expose and CMD don't necessarily neeed to be especified since they are in my FROM
```

- Running a container based on an image and using systemd (attaching to mylan)
```bash
docker container run -itd --privileged updated_arch02 /usr/sbin/init --network mylan --restart unless-stopped updated_arch02
```
