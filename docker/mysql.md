# Mysql examples on Docker 

##### Creating a mysql container from scratch
```
docker pull mysql
docker container run -d -p 3306:3306 --name mymysql -e MYSQL_ROOT_PASSWORD=123123 mysql:latest
docker exec -it mymysql mysql -u root -p
```
##### Attaching the newly created mysql container into a different network
```
docker network disconnect bridge mymysql
docker network create my_lan3 --subnet 192.168.17.0/24
docker network connect my_lan3 mymysql
docker network inspect my_lan3 (in order to check the container attached)
```
##### Creating a mysql container and enabling network connectivity
- No IP definition
```
docker container run -d -p 3306:3306 --name mymysql -e MYSQL_ROOT_PASSWORD=123123 --network my_lan3 mysql:latest
```
- Defining IP within the network attached (my_lan3)
- It is important to notice that the ip given must be within the subnet attached (my_lan3)
```
docker container run -d -p 3306:3306 --name mymysql2 -e MYSQL_ROOT_PASSWORD=123123 --network my_lan3 --ip 192.168.17.10 mysql:latest
```
