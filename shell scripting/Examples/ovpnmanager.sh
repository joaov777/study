#!/bin/bash

#OVPN MANAGER


#constantes
diretorioDeChaves="~/Documents/client-configs/files"
caminhoKey="/home/operador/rsa3/pki/reqs/$mail.req"
caminhoReq="/home/operador/rsa3/pki/private/$mail.key"
caminhoCrt="/home/operador/rsa3/pki/issued/$mail.crt"

#informações básicas LDAP
URI="ldap://ad.ifce.edu.br:389"
BASE="ou=ifce,dc=adproducao,dc=ifce,dc=edu,dc=br";
ACCOUNT="" #sensitive information to be added later
PASSWORD="" #sensitive information to be added later

#principal query LDAP
queryLdap="$(ldapsearch -x -H "$URI" -D "${ACCOUNT}" -w "${PASSWORD}" -b "${BASE}" (|(cn=$1)(mail=$1@ifce.edu.br)) -s sub sAMAccountName mail)"

#variaveis retornadas da base LDAP e formatadas
siape="$(sed -n '12p' <<< "$queryLdap" | cut -f2 -d" ")"
mailCompleto="$(sed -n '13p' <<< "$queryLdap" | cut -f2 -d" ")"
mail="$($mailCompleto | cut -f1 -d'@')"

#cabecalhos dos menus
function banner() {
    echo "$(tput bold)$(tput setaf 7)"
    echo "|==== GERENCIA SERVIDOR VPN - $1"
}

#Verificação no LDAP para retornar usuário baseado no SIAPE ou E-mail institucional
function verificaLDAP() {

  if [ "$1" == "$siape" ] || [ "$1"@ifce.edu.br == "$mailCompleto" ];
    then
      echo "|---- Usuário encontrado na base LDAP"
      echo "|-- Siape: $siape"
      echo "|-- E-mail: $mailCompleto"
    else
      echo "|---- Usuário não encontrado na base LDAP" ; read -p ""
    fi
}

#procura por chaves localmente baseado em partes do nome da chave
function procuraChavesFuzzy() {

  [ -f "$diretorioDeChaves"/*"$mail"* ] && {
    echo "|-- Chaves encontradas:" && ls -la "$diretorioDeChaves"/*"$mail"* ; read -p ""
  } || {
    echo "|-- Nenhuma chave encontrada para $mail " ; read -p ""
  }
}

#sobrescreve uma chave existente
function sobrescreveChave() {
  [ apagaChave "$mail.ovpn" && criaChave "$mail.ovpn" ] && {
    echo "|-- Chave $mail.ovpn sobrescrita com sucesso!" 
    } || {
    echo "|-- Chave "$mail".ovpn não pôde ser sobrescrita!"
    }
}

#verifica existencia de chave 
function verificaChave() {

  [ -f "$diretorioDeChaves"/"$mail".ovpn ] && {  
      echo "|-- Chave "$mail".ovpn pré-existente!" ; read -p ""
      
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
    criaChave "$1" 
  }
}

#apaga uma chave especificada
function apagaChave() {
  sudo rm caminhoKey caminhoReq caminhoCrt > /dev/null
}

#registro de log do script
function registraLog() {
  echo "[$(date)] - IP de origem: $(echo $SSH_CLIENT | awk '{ print $1}') - Chave criada: $mail" >> /home/$USER/ovpn_log.txt
}

#criação da própria chave OVPN
function criaChave() {

    clear
    banner "CRIANDO CHAVE"
    
      cd ~/openvpn-ca && source vars > /dev/null

      echo "|-- Chave $mail a ser criada..." && sleep 1
      cd ~/openvpn-ca && ./build-key $mail
      cd ~/client-configs && ./make\_config.sh $mail

      #verifica se a chave foi corretamente criada
      [ -f "$diretorioDeChaves"/"$mail".ovpn ] && {
          sed -i 's/group nogroup/group nobody/g' "$diretorioDeChaves"/"$1".ovpn
          echo -e "\n|---- RELATORIO FINAL" && echo "|-- Chave criada: $mail.ovpn" &&
          echo "|-- Local da chave: "$diretorioDeChaves"/$mail".ovpn ; read -p ""
        } || {
          echo "|-- Erro na criação da chave!!" && read -p ""
        }

      #logging information
      registraLog
}

#retorna número de clientes conectados
function clientesConectados() {
    clear
    banner "CLIENTES CONECTADOS"
    echo "|-- Clientes conectados: $(sudo cat /var/log/openvpn/openvpn-status.log | grep 10.8.0 | wc -l)"
    read -p ""
}

#menu principal
while [ true ];
    do

    clear
    banner "MENU PRINCIPAL"
    echo "#(1) - Verificar existência de chave OVPN"
    echo "#(2) - Criar/Sobrescrever chave OVPN"
    echo "#(3) - Apagar chave"
    echo "#(4) - Verificar quantidade de clientes conectados"
    echo "|-------------------------------------------|"
    read -p "Option: " opcaoMenu


    case $opcaoMenu in
      q|Q|quit|QUIT|Quit|qUIT|exit|EXIT|Exit) exit ;;
      1) read -p "SIAPE ou E-mail (sem @ifce.edu.br): " siapeOuEmail && procuraChavesFuzzy "$siapeOuEmail" ;;
      2) read -p "SIAPE ou E-mail (sem @ifce.edu.br): " siapeOuEmail && verificaChave "$siapeOuEmail" ;;
      3) read -p "SIAPE ou E-mail (sem @ifce.edu.br): " siapeOuEmail && apagaChave "$siapeOuEmail" ;;
      4) clientesConectados ;;
      *) echo "Opção inválida!!" ;;
    esac
done
