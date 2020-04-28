
#!/bin/bash

#Autor: Joao Victor R. Galvino
#Data de criacao: 06.04.20
#Ultima atualizacao: 15.04.20
#Objetivo: Gerenciar chaves OVPN mais facilmente. Tanto na criação/sobrescrita, quanto na verificação de existência.
#Versao: 1.0

#!/bin/bash

#verifica a chave OVPN
verificarChave() {

	#if [ -f ~/client-configs/files/"$1".ifce.ovpn ]; then
	if [ grep "$1" ~/clien-configs/files/* 2>1 ];
	then
		echo ">> Nenhuma credencial associada!!" && sleep 2
	else
		echo ">> Credenciais associadas existentes: " && sleep 1
		ls -la ~/client-configs/files/* | grep $1 ; 
		echo "Pressione qualquer tecla para continuar... " ; read -p ""
	fi
}

#define a criacao da chave
criaChave() {

		clear
		cd ~/openvpn-ca && source vars > /dev/null

		echo ">> Credencial a ser criada..." ; sleep 1
		cd ~/openvpn-ca && ./build-key $1
		cd ~/client-configs && ./make\_config.sh $1

		if [ -f ~/client-configs/files/"$1".ifce.ovpn ]; then

			sed -i 's/group nogroup/group nobody/g' ~/client-configs/files/"$1".ifce.ovpn
			echo ""
			echo "> RELATORIO FINAL <"
			echo "> Chave criada: $1.ifce.ovpn"
			echo "> Local da chave: ~/client-configs/files/$1.ifce.ovpn"
			read -p ""
		else
			echo "> ERRO NA CRIAÇÃO DA CHAVE!!"
		fi
}

while [ true ];
    do

    clear
    echo "$(tput bold)$(tput setaf 7)"
    echo "|==============|> IFCE OVPN <|==============|"
    echo "#(0) - Exit"
    echo "#(1) - Verificar existência de chave OVPN"
    echo "#(2) - Criar/Sobrescrever chave OVPN"
    echo "|-------------------------------------------|"
    read -p "Option: " menuChoice


    case $menuChoice in
            0) exit ;;
	    1) read -p "Insira o nome da chave OVPN conforme e-mail institucional (sem @ifce.edu.br): " chaveOVPN && verificarChave $chaveOVPN ;;
	    2) read -p "Insira o nome da chave OVPN conforme e-mail institucional (sem @ifce.edu.br): " chaveOVPN && criaChave $chaveOVPN;;
            *) echo "Opção inválida!!" ;;
    esac

    done
