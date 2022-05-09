#!/bin/bash

clear
nomelista="";

echo "#########################################################";
echo "########## INSIRA O NOME DA LISTA A SER CRIADA ##########";
echo "#########################################################";

echo "Nome: ";
read nomelista;

        if grep $nomelista "/etc/aliases" > /dev/null
        then
                echo "O nome da lista $nomelista j? existe.";
        else

        echo -e "\n" >> conf.txt

        sudo    echo "##$nomelista" >> /etc/aliases
        sudo    echo $nomelista:                                "\"|/var/lib/mailman/mail/mailman post $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-admin:                          "\"|/var/lib/mailman/mail/mailman admin $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-bounces:                        "\"|/var/lib/mailman/mail/mailman bounces $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-confirm:                        "\"|/var/lib/mailman/mail/mailman confirm $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-join:                           "\"|/var/lib/mailman/mail/mailman join $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-leave:                          "\"|/var/lib/mailman/mail/mailman leave $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-owner:                          "\"|/var/lib/mailman/mail/mailman owner $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-request:                        "\"|/var/lib/mailman/mail/mailman request $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-subscribe:                      "\"|/var/lib/mailman/mail/mailman subscribe $nomelista\"" >> /etc/aliases
        sudo    echo $nomelista-unsubscribe:                    "\"|/var/lib/mailman/mail/mailman unsubscribe $nomelista\"" >> /etc/aliases

                echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>";
                echo ">>>>> Lista \"$nomelista\" adicionada com sucesso!!";
                echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>";

                sudo newaliases
                ##sudo /etc/init.d/mailman restart
        fi


