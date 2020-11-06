#!/bin/bash

#Importing mainfunctions
. ~/Desktop/estudoshell/myfunctions.sh

# invoke the is_file_dir and pass $file as arg
#check_file "$1"
check_dir $1 && {
    #create logic here in case the folder exists
    echo "I can develop my logic now because $1 exists!!"
} || {
    #create logic here in case the folder does not exist
    echo "I can't develop my logic now because $1 does not exist!!"
}

