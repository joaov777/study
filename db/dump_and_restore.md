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
pg_dump --file "C:\\Users\\joao\\Desktop\\teste.sql" --host "127.0.0.1" --port "5432" --username "postgres" --no-password --verbose --role "postgres" --format=c --blobs --no-owner --schema "public" "suap_dev"
pg_dump --host "127.0.0.1" --port "5432" --username "postgres" --no-password --verbose --role "postgres" --format=c --blobs --no-owner --schema "public" "suap_dev" > /home/joao/mybackup.sql
pg_dump –-host 127.0.0.1 –-port 5432 -–username postgres -–no-password –-verbose –-role postgres –-format=c –-blobs –-no-owner –-schema public suap_dev > mydump
```

## RESTORE
- pg_restore é usado com dumps custom
```shell
docker exec -i suap-suapdb-1 pg_restore --no-owner --username postgres -v --dbname suap_dev < 12.09.22.dump
```

- psql é usado com dumps plaintext
```shell
psql --dbname=suap_dev --host=localhost --username=postgres -W < backup_suap_producao.sql
```
