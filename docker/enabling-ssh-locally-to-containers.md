# Connecting to Docker containers through SSH locally

## You can follow similar procedures like below
### Creating the base image

- Creating a Dockerfile to build a base image

vim Dockerfile
```bash
FROM ubuntu:latest
RUN apt update -y && apt upgrade -y
RUN useradd -m -s /bin/bash -k /etc/skel joao
RUN passwd joao
RUN apt install net-tools sudo vim iputils-ping openssh-server -y
RUN service ssh start
CMD ["bash"]
```
- Building the image (Run this command on the same directory as the Dockerfile)
```bash
docker build -t teste_imagem .
```
### Creating the network for the containers
```bash
docker network create local_net --subnet 70.70.70.0/24
```

### Creating the containers
```bash
# creating 3 containers based off teste_imagem. Exposing 222x from the containers while maintaining 
# the standard SSH port for the service within the container
docker container run -itd --name teste_container01 --network local_net -p 2222:22 teste_imagem
docker container run -itd --name teste_container02 --network local_net -p 2223:22 teste_imagem
docker container run -itd --name teste_container03 --network local_net -p 2224:22 teste_imagem
```

### Connect to each container and change sshd_config on each container
```bash

docker attach teste_container01

#uncomment these lines
Port 22
ListenAddress 0.0.0.0

# restart the service
service ssh restart

# check if the ports are open on the container
netstat -ntpl4

root@3c6acee84654:/# netstat -ntpl4
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      3430/sshd: /usr/sbi
tcp        0      0 127.0.0.11:34685        0.0.0.0:*               LISTEN      -
```

### On an elevated local terminal:
```bash
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=<SSH_EXPOSED_PORT> connectaddress=<WSL_IP_ADDRESS> connectport=<SSH_SERVICE_PORT>

# Enabling for container01
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=2222 connectaddress=172.31.86.232 connectport=22

# Enabling for container02
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=2223 connectaddress=172.31.86.232 connectport=22

# Enabling for container03
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=2224 connectaddress=172.31.86.232 connectport=22
```

### Check if the ports are open on WSL
```
netstat -ntpl4
 ⚡~/temp/estudo_docker_file ❯ netstat -ntpl4
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:2222            0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:37359         0.0.0.0:*               LISTEN      2487/node
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      -
```

Additional tips:
```bash
# to reset all these rules
netsh int portproxy reset all

# to display all the rules
netsh interface portproxy show v4tov4
```

### Testing access to containers from the local machine
```bash
# connecting to teste_container02
ssh -p 2223 joao@localhost 

# connecting to container01
ssh -p 2222 127.0.0.1

# connecting to container03
ssh localhost -p 2224
```

### Enabling LAN access to the containers
- Follow the menus below
 - Windows Defender Firewall with Advanced Security
 - Inbound Rules
 - New Rule
 - Port
 - TCP
 - Specific local ports (exposed port on WSL)
 - Allow the connection
 - Next and Finish 

### Testing access from a lan remote machine
```bash
ssh -p <exposed_port> <user>@<local_machine_ip>
ssh -p 2222 joao@192.168.16.190
```
### Adding ports to the firewall (to be exposed on the LAN)
```bash
netsh advfirewall firewall add rule name="inbound suap dev" dir=in action=allow protocol=TCP localport=8001
netsh advfirewall firewall add rule name="inbound suap dev" dir=in action=allow protocol=TCP localport=8000
```

### WSL Port forwarding
```bash
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=8001 connectaddress=localhost connectport=8001
```
- listenaddress = where to accept connections from 
- listenport = port exposed and used by other lan users to connect to you (in the browser)
- connectaddress = localhost (localhost automatically uses wsl)
- connectport = wsl service port exposed

### Testing the connection
on the browser: <LAN IP address>:<port>
