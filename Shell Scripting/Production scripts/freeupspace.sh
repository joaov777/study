#!/bin/bash

	while [ true ];
	do

	clear
	echo '>> EXECUTAR SOMENTE COM USUARIO ROOT! '
	echo '>> Atenção! Este script apagará todos os anexos de todas as listas até o ano de 2016'
	echo '>> Deseja prosseguir? (1) - sim / (2) - nao'
	read -p "Opcao: " menuChoice

	case $menuChoice in
		1)
			echo '>>>> APAGANDO DADOS <<<<'
			sleep 1
			cd /var/lib/mailman/archives/private
			rm -r [a-z]*.[a-z]*/attachments/201[0-6]*
			
			echo '>>>> DADOS APAGADOS ATÉ 2016 <<<<'
			exit;;

		2)
			echo '>>>> SAINDO <<<<'
			sleep 1 
			exit

			exit;;
	
	esac

	done




