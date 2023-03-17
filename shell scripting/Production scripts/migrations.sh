#!/bin/bash

FILE_MIGRATIONS="/home/$USER/.migrations"
FILE_UNAPPLIED="/home/$USER/.unapplied"

# Generate a list of all migrations
ALL_MIGRATIONS=$(docker exec -it suap-suap-1 python /suap/manage.py showmigrations --list > $FILE_MIGRATIONS)

# Remove escape characters from a file
sed -i 's/\x1B\[[0-9;]\+[A-Za-z]//g' $FILE_MIGRATIONS && sed -i 's/\r//' $FILE_MIGRATIONS

# Get the list of unapplied migrations
UNAPPLIED_MIGRATIONS=$(echo $FILE_MIGRATIONS | grep "\[ \]" | cut -d " " -f 4 > $FILE_UNAPPLIED) 
sed -i 's/\x1B\[[0-9;]\+[A-Za-z]//g' $FILE_UNAPPLIED && sed -i 's/\r//' $FILE_UNAPPLIED

# Create an array from the contents of the file, splitting on newlines
IFS=$'\n' read -r -d '' -a migrations_array <<< "$UNAPPLIED_MIGRATIONS"

for migration in "${migrations_array[@]}"
do

    # extracting the migration number
    migration_number=${migration:2:2}

    # extracting the line where the migration pattern was found
    line=$(echo "$ALL_MIGRATIONS" | grep -n "$migration" | cut -d ':' -f 1)
    latest_migration_applied=$((line-1))

    # showing module name
    module_name=$(echo "$ALL_MIGRATIONS" | sed "$(($line-$migration_number))q;d")

    echo $latest_migration_applied_name

    echo $migration
    echo $module_name

done