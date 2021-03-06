#!/bin/bash

# CONFIGURAÇÕES NECESSÁRIAS PARA CORRETO FUNCIONAMENTO DESTE SCRIPT
# - Usuário "backup" deverá ser criado no firewall remoto com autenticaão por chaves assimétricas.e pela porta 5555
# - O local de execução deste script deverá possuir a chave pública mapeada nos firewalls remotos (conta "backup")
# - Rclone deverá ser corretamente mapeado no mesmo local de instalação/execução deste script (neste exemplo: coir)

# declaração da associação dos campus
declare -A campus_keys
campus_keys['200.129.18.2']='Polo de Inovacao'
campus_keys['200.129.16.1']='Reitoria'
#campus_keys['200.129.25.178']='Itapipoca'
campus_keys['200.17.33.1']='Pici'
#campus_keys['200.129.25.144']='Horizonte'

# declaração dos campus a serem feitos backup particionado dos firewalls listados em "campus_keys"

firewall_sections=(
    aliases unbound dnsmasq dhcpd 
    dhcpdv6 nat filter interfaces \
    rrddata cron syslog system snmpd \
    staticroutes vlans captiveportal \
    installedpackages)

# função principal
main_procedure(){
    
for pkg in "${!campus_keys[@]}"; do
	clear
	echo "|==============|> PFSENSE XML BACKUP <|==============|"
    echo "|=====> Campus: ${campus_keys[$pkg]}"

    if [ ! -d ~/bkp ]; then mkdir ~/bkp ; fi #checando se existe a pasta temporaria local

    # checando se existe a pasta do campus especifico em bkp
    if [ ! -d ~/bkp/"${campus_keys[$pkg]}" ]; then mkdir ~/bkp/"${campus_keys[$pkg]}" ; fi

    # checando a existencia da pasta do campus no google drive
    if [[ $(rclone tree coir:/BACKUPS/Firewalls | grep "${campus_keys[$pkg]}") = "" ]];
        then rclone mkdir coir:/BACKUPS/Firewalls/"${campus_keys[$pkg]}"
    fi

    # retornando a quantidade de backups feitos pelo campus especifico
    n=$(rclone lsd coir:/BACKUPS/Firewalls/"${campus_keys[$pkg]}" | wc -l)

    # configurando a nomenclatura utilizada para o arquivo config.xml
    file="config - 00$n - ${campus_keys[$pkg]} - $(date +%d-%m-%y) - $(date +%T).xml"



    echo "|===> Configuração global..." ; sleep 1
    # download do arquivo .xml
    scp -P 5555 backup@$pkg:/cf/conf/config.xml ~/bkp/"${campus_keys["$pkg"]}"/"$file" > /dev/null
    echo "|===> config.xml de ${campus_keys[$pkg]} : OK"

    # envio do arquivo .xml ao google drive
    rclone copy ~/bkp/"${campus_keys[$pkg]}"/"$file" coir:/BACKUPS/Firewalls/"${campus_keys[$pkg]}"/"$file"/GLOBAL
    echo "|===> Config.xml enviado ao Google Drive!!!" ; sleep 2;

    done 

    # remocao de lixo da maquina local
    rm -rf ~/bkp

}
    # execucao da função principal
    main_procedure
