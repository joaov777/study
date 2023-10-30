#!/bin/bash

function press_enter_to_continue() {
	read -p "Press enter to continue..."
}

menu_options=(
	"Install base packages"
	"Enable configuration files"
	"Set up basic local servers"
	"Check up current configuration"
	"Manage ZSH"
	)

menu_functions=(
	"Function of option 1"
	"Function of option 2"
	"Function of option 3"
	"Function of option 4"
	"Function of option 5"
)

while true; do

	clear
	echo "------------"
	for ((i=0; i<${#menu_options[@]}; i++)); do
		echo "($((i+1))) - ${menu_options[i]}"
	done

		read -p "Option: " user_option

		[[ "$user_option" =~ ^[qQ]$|^quit$|^QUIT$ ]] && exit 0 

		[[ "$user_option" =~ ^[1-${#menu_options[@]}]$ ]] && {
			user_option=$((user_option - 1))
			echo "${menu_functions[$user_option]}" 
			press_enter_to_continue
		} || {
			echo "Invalid input" && press_enter_to_continue
		}
	clear
done
