#!/bin/bash

#constantes
pressioneTecla="Pressione qualquer tecla para continuar..."
diretorioDeChaves="/home/operador/configs_vpn"

#informações básicas LDAP
URI="ldap://ad.ifce.edu.br:389" #ex.: ldap://ad.mycompany.com:389
BASE=""; #ex.: ou=mycompany,dc=ad,dc=com,dc=br
ACCOUNT=""
PASSWORD=""

#buscas LDAP
queryLdap="ldapsearch -x -H "$URI" -D "${ACCOUNT}" -w "${PASSWORD}" -b "${BASE}" (|(cn=$1)(mail=$1@ifce.edu.br)) -s sub sAMAccountName mail"

#variáveis retornadas pelo LDAP e formatadas
siape="$(sed -n '12p' <<< "$queryLdap" | cut -f2 -d" ")"
mailCompleto="$(sed -n '13p' <<< "$queryLdap" | cut -f2 -d" ")"
mail="$mail | cut -f1 -d"@""

#cabeçalhos dos menus
function banner() {
    echo "$(tput bold)$(tput setaf 7)"
    echo "|==== GERENCIA SERVIDOR VPN - $1"
}

#Verificação no LDAP para retornar usuário baseado no SIAPE ou E-mail institucional
function verificaLDAP() {

	if [ "$1" == "$siape" ] || [ "$1"@ifce.edu.br == "$mailCompleto" ];
    then
		echo "|---- USUÁRIO ENCONTRADO"
		echo "|-- Siape: $siape"
		echo "|-- E-mail: $mailCompleto" ; pressioneTecla
    else
		echo "|---- USUÁRIO NÃO ENCONTRADO" && pressioneTecla
    fi
	
}

#Verifica existencia de chaves
function procuraChaves() {

	[ "$(ls -la $diretorioDeChaves/*$1* 2>1)" ] && {
		echo "|-- Chaves encontradas:" && 
		ls -la $diretorioDeChaves/*$1* ; read -p "$pressioneTecla"
	} || {
		echo "|-- Usuário não tem chave criada" ; read -p "$pressioneTecla" 
	}
}

#sobrescreve uma chave existente
function sobrescreveChave() {
	[ apagaChave "$mail".ovpn && criaChave "$mail".ovpn ] && {
		echo "|-- Chave $mail.ovpn sobrescrita com sucesso!" 
		} || {
		echo "|-- Chave "$mail".ovpn não pôde ser sobrescrita!"
		}
}

#verifica existencia de uma chave 
function verificaChave() {
	[ "$(ls -la $diretorioDeChaves/$1 2>1)" ] && {
			echo "|-- Chave "$mail".ovpn pré-existente!"
			
			while [ true ]; 
			do
				read -p "|-- Deseja sobrescrever a chave $mail.ovpn existente? [S/N]" -n1 -s sobrescrever
				
				case "$sobrescrever" in 
					S|s) sobrescreveChave "$mail" ;;
					N|n) echo "|-- Chave $mail não foi alterada" && break ;;
					*) echo "|-- Insira uma opção válida! \(S\)im ou \(N\)ão" && sleep 1 ;;
				esac
			done
	} || {
		criaChave "$mail" 
	}
}

#apaga uma chave especificada
#function apagaChave() {
	##Verificar como apagar completamente o registro da chave localmente 
	## apagar os arquivos crt, key e pem
#}

#registro de log do script
function registraLog() {
	echo "[$(date)] - IP de origem: $(echo $SSH_CLIENT | awk '{ print $1}') - Chave criada: $1" >> /home/$USER/ovpn_log.txt
}

#riação da própria chave OVPN
function criaChave() {

		clear
		banner "CRIANDO CHAVE"
		
		cd ~/openvpn-ca && source vars > /dev/null

		echo "|-- Chave $mail a ser criada..." && sleep 1
		cd ~/openvpn-ca && ./build-key $mail
		cd ~/client-configs && ./make\_config.sh $mail

		[ -f "$diretorioDeChaves"/"$mail".ovpn ] && {
			sed -i 's/group nogroup/group nobody/g' "$diretorioDeChaves"/"$1".ifce.ovpn
			echo -e "\n|---- RELATORIO FINAL" && echo "|-- Chave criada: $mail.ovpn" &&
			echo "|-- Local da chave: "$diretorioDeChaves"/$mail.ovpn" && pressioneTecla
		} || {
			echo "|-- Erro na criação da chave!!" && pressioneTecla
		}

		#logging information
		registraLog
}

#retorna número de clientes conectados
function clientesConectados() {
		clear
		echo "|--> CLIENTES CONECTADOS: $(sudo cat /var/log/openvpn/openvpn-status.log | grep 10.8.0 | wc -l)"
		pressioneTecla
}

while [ true ];
    do

    clear
    banner "MENU PRINCIPAL"
    echo "#(1) - Verificar existência de chave OVPN"
    echo "#(2) - Criar/Sobrescrever chave OVPN"
    echo "#(3) - Verificar quantidade de clientes conectados"
    echo "|-------------------------------------------|"
    read -p "Option: " menuChoice

    case $menuChoice in
        q|Q|quit|QUIT|Quit|qUIT|exit|EXIT|Exit) exit ;;
	    1) read -p "SIAPE ou E-mail (sem @ifce.edu.br): " siapeOuEmail && procuraChaves "$siapeOuEmail" ;;
	    2) read -p "SIAPE ou E-mail (sem @ifce.edu.br): " siapeOuEmail && verificaChave "$siapeOuEmail" ;;
	    3) clientesConectados ;;
        *) echo "Opção inválida!!" ;;
    esac

done

