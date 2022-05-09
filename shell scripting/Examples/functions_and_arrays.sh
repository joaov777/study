#!/bin/bash


function showArray(){
    arr=("$@")
    for i in "${arr[@]}";
    do 
        echo "$i"
    done
}

function sum(){
    return $(( $1 + $2 ))
}

#read -p "First number: " number1
#read -p "Second number: " number2

#sum "$number1" "$number2"
#echo "$?"
array=("Joao" "Marcos" "Andre" "Carlos" "Santana" "Alexandre" "Saulo" "Carla" "Antonia" "Mirella" "Sandra" "Marcelo" "Carolina" "Erlen" "Christopher")

showArray "${array[@]}"







