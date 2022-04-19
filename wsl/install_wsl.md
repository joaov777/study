## Instalando WSL

1. Ir na opção para **Ativar ou desativar recursos do windows** e marcar as seguintes opções:
	- Hyper-V
	- Plataforma de maquina virtual
	- Subsistema do Windows para Linux	

2. Reinicie a máquina

3. Instalar o WSL2
```bash 
wsl --install
# reinicie a máquina
```

4. Listando distribuições disponíveis
```bash
wsl --list --online
wsl --install -d <DISTRO_NAME>
# reinicie a máquina
```

5. Configure a distribuição
