#!/bin/bash

# restore_db_container.sh 
# Usage: restore_db_container.sh example.dump
# Context: Local development restore of an arbirtrary container database
# Workflow: One positional parameter must be provided. The dump is created if none is found
# Creation: 07.07.22
# Last update: 09.08.22

SCRIPT_FILE="$(readlink -f $0)" # script absolute path
SCRIPT_DIR="$(dirname "$SCRIPT_FILE")" # script directory
PROJECT_DIR="$(dirname $(dirname $(dirname $SCRIPT_DIR)))" #base file system (/)
CONTAINER_NAME="container_name"
TARGET_MACHINE_PASSWORD="target_machine_password"
TARGET_MACHINE="target_machine"
TARGET_MACHINE_USER="target_machine_db_user"
LOCAL_DATABASE_NAME="local_database_name"

# if first positional argument not empty
if [ ! -z "$1" ]; then

	# Dump is created if no target file is found 
	# echo "$1" && sleep 30
	if [ ! -f "$1" ]; then
		echo "> Creating new dump..." && sleep 3 && PGPASSWORD="$TARGET_MACHINE_PASSWORD" pg_dump "$CONTAINER_NAME" --host="$TARGET_MACHINE" --username="$TARGET_MACHINE_USER" --schema=public -O -Fc -v > "$1" 
	fi

	# dropping and setting up a new suap_dev database locally within the container
	echo "> Restoring dump file $1 to local container database..." && sleep 3
	docker exec -i $CONTAINER_NAME psql --username postgres -c "DROP DATABASE IF EXISTS "$LOCAL_DATABASE_NAME" WITH (FORCE)"
	docker exec -i $CONTAINER_NAME psql --username postgres -c "CREATE DATABASE "$LOCAL_DATABASE_NAME" with encoding 'utf-8'"
	docker exec -i $CONTAINER_NAME psql --username postgres -c "ALTER DATABASE "$LOCAL_DATABASE_NAME" SET bytea_output TO 'escape'"

	# restoring existing dump into container database and enabling extensions
	echo "> Restoring existing dump into container database and enabling extensions..." && sleep 3 
	docker exec -i $CONTAINER_NAME pg_restore --username postgres -v --dbname "$LOCAL_DATABASE_NAME" < "$1"
	docker exec -i $CONTAINER_NAME psql --username=postgres --dbname="$LOCAL_DATABASE_NAME" --host=localhost -c "CREATE EXTENSION IF NOT EXISTS unaccent with schema pg_catalog;"
	docker exec -i $CONTAINER_NAME psql --username=postgres --dbname="$LOCAL_DATABASE_NAME" --host=localhost -c "CREATE EXTENSION IF NOT EXISTS pg_trgm with schema pg_catalog;"

	# setting all user passwords to 123
	echo "> Setting all user passwords to 123..." && sleep 3
	docker exec -i $CONTAINER_NAME python manage.py set_passwords_to_123

	echo "> SUCCESS!"
		
else
echo "> ERROR: Provide the dump file path"
fi