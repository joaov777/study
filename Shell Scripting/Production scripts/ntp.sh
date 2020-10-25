   clear

        echo "#########################################"
        echo "--- SINCRONIZACAO DE HORARIO COM NTPD ---"
        echo "###### -- NAO ABORTE A EXECUCAO -- ######"

        #desabilitando atualiza??es autom?ticas do hor?rio
        echo "--> Desabilitando atualiza??o autom?tica do hor?rio..."
        timedatectl set-ntp off 1> /dev/null 2> /dev/stdout

        #download dos pacotes necess?rios
        echo "--> Baixando pacotes necess?rios..."
        apt-get update 1> /dev/null 2> /dev/stdout
        apt-get install ntpdate 1> /dev/null 2> /dev/stdout

        #configura??o do crontab - a cada hora
        #/var/spool/cron/crontabs/root
        echo "--> Configurando CRONTAB..."
        sudo echo  "00 * * * * /usr/sbin/ntpdate b.st1.ntp.br" >> /var/spool/cron/crontabs/root
		sudo echo "@reboot /usr/sbin/ntpdate b.st1.ntp.br" >> /var/spool/cron/crontabs/root
        echo "--> Hora atualizada..."
