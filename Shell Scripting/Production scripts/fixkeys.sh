#!/bin/bash

#Author: Joao Victor R. Galvino
#Creation: 28.04.20
#Last update: 28.04.20
#Main purpose: Fix ovpn keys replacing nogroup with nobody keyword within the .ovpn key file
#Version: 1.0

	path=$1

	for i in {1..$(ls $path | wc -l)}
	do
		sed -i 's/group nogroup/group nobody/g' $path/*.ifce.ovpn
	done
	
	#one liner could be possible
	#for i in {1..$(ls $path | wc -l)}; do sed -i 's/group nogroup/group nobody/g' path/*.ifce.ovpn; done
	
	#another for loop example
	#for i in /etc/*.conf; do cp $i /backup; done