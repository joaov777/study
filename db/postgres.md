#### Habilitando acesso remoto ao banco
```shell
sudo vim /etc/postgresql/13/main/pg_hba.conf
host	all	all	0.0.0.0/0	md5

sudo vim /etc/postgresql/13/main/postgresql.conf
listen_addresses = '*'

sudo service postgresql start
```

#### Testando acesso ao banco remoto
```shell 
psql -U postgres -p 5432 -h 200.129.18.18
```

#### Alterando a senha do usuário postgres
```shell
sudo -u postgres psql
postgres=# \password postgres
Enter new password: <new-password>
postgres=# \q

# another possibility below
sudo -u postgres psql
ALTER USER postgres PASSWORD '<new_password>'

# another possibility
sudo -u postgresql psql db_name
ALTER USER postgres WITH PASSWORD '<new_password>';
```

#### Alterando o nome do usuário no banco
```shell
ALTER USER <name> RENAME TO <new_name>
```
