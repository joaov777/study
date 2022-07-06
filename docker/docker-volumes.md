# Working with docker volumes

#### creating a docker volume named "volume_ubuntu"
``` 
docker volume create volume_ubuntu 
```

#### creating a container based on manjaro linux image and attaching the volume previously created into the /mydata folder withint the container
```
docker run -itd --name manjaro -v volume_ubuntu:/mydata manjarolinux/base
```

#### backing up the volume data
```
docker run --rm --volumes-from manjaro -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /mydata  
```

#### restoring the volume data
```
docker run --rm --volumes-from manjaro -v $(pwd):/backup manjarolinux/base bash -c "cd /mydata && tar xvf /backup/backup.tar --strip 1"
```
