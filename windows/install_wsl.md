## Instalando WSL

1. Ir na opção para **Ativar ou desativar recursos do windows** e marcar as seguintes opções:
	- Hyper-V
	- Plataforma de maquina virtual
	- Subsistema do Windows para Linux	

Ou executar somente os comandos abaixo
```bash
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
bcdedit /set hypervisorlaunchtype auto
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All -NoRestart
```

2. Reinicie a máquina

3. Instalando o WSL2
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
# check all available distros
wsl -l -d

# checking wsl version for all distros locally installed
wsl -l -v

# converting a distro to wsl2
wsl --set-version Ubuntu-20.04 2
