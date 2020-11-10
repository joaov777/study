#!/bin/bash

# OVPNREITORIA

#Autor: Joao Victor R. Galvino
#Contato: joao.galvino@ifce.edu.br
#Setor de Atuacao: Coordenadoria de Infraestrutura de Redes - COIR
#Data de criacao: 06.04.20
#Ultima atualizacao: 10.11.20 - Inserção da troca dos IP's da VPN do Pici pela VPN da Reitoria na chave gerada.
#Objetivo: Gerenciar chaves OVPN mais facilmente. Tanto na criação/sobrescrita, quanto na verificação de existência.
#Versao: 1.0

#verifica a chave OVPN
verificarChave() {

	#if [ -f ~/client-configs/files/"$1".ifce.ovpn ]; then
	if [ grep "$1" ~/client-configs/files/* 2>1 ];
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

			#Alteração no arquivo final gerado para adequação da conectividade
			sed -i 's/group nogroup/group nobody/g' ~/client-configs/files/"$1".ifce.ovpn
			sed -i 's/200.17.33.43/200.129.17.20/g' ~/client-configs/files/"$1".ifce.ovpn
			echo ""
			echo "> RELATORIO FINAL <"
			echo "> Chave criada: $1.ifce.ovpn"
			echo "> Local da chave: ~/client-configs/files/$1.ifce.ovpn"
			read -p ""
		else
			echo "> ERRO NA CRIAÇÃO DA CHAVE!!"
		fi

		#envio para log
		echo "[$(date)] - IP de origem: $(echo $SSH_CLIENT | awk '{ print $1}') - Chave criada: $1" >> ~/ovpn_log.txt
}

#verifica a quantidade de clientes conectados
clientesConectados() {
		
		clear
		echo "> CLIENTES CONECTADOS <"
		echo "$(sudo cat /var/log/openvpn/openvpn-status.log | grep 10.8.0 | wc -l)"
		read -p ""

}

while [ true ];
    do

    clear
    echo "$(tput bold)$(tput setaf 7)"
    echo "|==============|> IFCE OVPN - REITORIA <|==============|"
    echo "#(0) - Exit"
    echo "#(1) - Verificar existência de chave OVPN"
    echo "#(2) - Criar/Sobrescrever chave OVPN"
    echo "#(3) - Verificar quantidade de clientes conectados"
    echo "|-------------------------------------------|"
    read -p "Option: " menuChoice


    case $menuChoice in
            0) exit ;;
	    1) read -p "Insira o nome da chave OVPN conforme e-mail institucional (sem @ifce.edu.br): " chaveOVPN && verificarChave $chaveOVPN ;;
	    2) read -p "Insira o nome da chave OVPN conforme e-mail institucional (sem @ifce.edu.br): " chaveOVPN && criaChave $chaveOVPN;;
	    3) clientesConectados ;;
            *) echo "Opção inválida!!" ;;
    esac

    done
