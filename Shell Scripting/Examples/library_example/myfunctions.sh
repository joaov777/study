#!/bin/bash

declare -r TRUE=0
declare -r FALSE=1

# Function used to determine whether the argument is a directory, a file, a link or even and executable file.
function check_type_of_file(){

    # $f is local variable
	local f="$1"

    [ -f "$f" ] && { echo "file"; exit 0; } || {
        [ -d "$f" ] && { echo "folder"; exit 0; } || {
            [ -L "$f" ] && { echo "link"; exit 0; } || {
                [ -x "$f" ] && { echo "executable"; exit 0; } || {
                    echo "unknown"; exit 0;
                }
            }
        }
    }

}
#end of function

### FUNCTION 2 ###
# This function takes a folder name and check whether the current directory has it. If so, it deletes it. If not, it creates it.
##################
function check_dir_and_act() {

    local folder="$1"
    [ ! -d $folder ] && mkdir $PWD/$folder || rm -rf $PWD/$folder fi

}

function check_dir() {
    local folder="$1"
    [ -d $folder ] && return $TRUE || return $FALSE 
}






