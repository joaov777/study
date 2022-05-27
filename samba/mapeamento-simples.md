## Simples mapeamento de pasta e habilitação do serviço SAMBA no Linux

1. Instale o samba
```shell
sudo apt install samba -y
```
2. Definir senha para o usuário no samba
```shell
sudo smbpassw -a <usuario>
```
3. Escolha uma pasta ou crie uma para ser compartilhada e defina as permissões de acesso
```shell
mkdir <pasta>
chmod 777 <pasta>
```
4. Edite o arquivo smb.conf parecido com os dados abaixo:
```shell
sudo vim /etc/samba/smb.conf

[publico]

	path	=	<caminho da pasta a ser compartilhada>
	valid users	=	joaovictor;
	admin users	=	joaovictor;
	read list	=	joaovictor;
	write list	=	joaovictor;
```
5. Reinicie o serviço do samba e verifique o status
```shell
/etc/init.d/smbd restart 
sudo systemctl enable smbd --now
sudo service smbd start 

# verificando status
/etc/init.d/smbd status
```

6. Teste o acesso à pasta compartilhada através do IP da máquina e credenciais definidas para o usuário


