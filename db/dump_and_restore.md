## DUMP
- pg_dump usa o modo plain text por padrão
- Importante utilizar os parâmetros (flags)
  - -v ou --verbose
  - -W ou --password
  - -O ou --no-owner

- Salvando no modo plain text
```shell
pg_dump suap --host=suap-bd.ifce.edu.br --username=suap --schema=public -W -O -v > /home/$USER/backup_suap_producao.sql
```
- Salvando no modo custom
```shell
# incluindo a diretiva --file para especificar o caminho e nome de saída do dump. format=c determina que é custom 
pg_dump --file "C:\\Users\\joao\\Desktop\\teste.sql" --host "127.0.0.1" --port "5432" --username "postgres" --no-password --verbose --role "postgres" --format=c --blobs --no-owner --schema "public" "suap_dev"

# dump para um arquivo de saída específico. Sem diretiva --file
pg_dump --host "127.0.0.1" --port "5432" --username "postgres" --no-password --verbose --role "postgres" --format=c --blobs --no-owner --schema "public" "suap_dev" > /home/joao/mybackup.sql

# outro exemplo
pg_dump –-host 127.0.0.1 –-port 5432 -–username postgres -–no-password –-verbose –-role postgres –-format=c –-blobs –-no-owner –-schema public suap_dev > mydump

# dump de um banco remoto para salvar localmente. Arquvo de saida final é "production_dump". 
pg_dump --host [REMOTE_MACHINE_IP] --port 5432 --username [DATABASE_USER] -W --verbose --format=c --blobs --no-owner --schema public [DATABASE_NAME] > production_dump
```

## RESTORE
- pg_restore é usado com dumps custom
```shell
# restaurando banco de um container
docker exec -i my_pg_container pg_restore --no-owner --username postgres -v --dbname [TARGET_DATABASE] < [LOCAL_DUMP_PATH]
```

- psql é usado com dumps plaintext
```shell
psql --dbname=[TARGET_DATABASE] --host=localhost --username=postgres -W < [LOCAL_DUMP_PATH].sql
```
