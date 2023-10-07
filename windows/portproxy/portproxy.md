
#### 1. Allow the ports through the firewall
Firewall > Inbound rule > Port > set the listenports (ports on which the windows host will listen)
```bash
netsh advfirewall firewall add rule name="choose the rule name here" dir=in action=allow protocol=TCP localport=8877
```

#### 2. Create the proxies
listenport: The port on which the Windows host will listen.
listenaddress: The address on which the Windows host will listen (0.0.0.0 means it will listen on all available interfaces).
connectport: The port to which the traffic will be forwarded on the WSL instance.
connectaddress: The IP address of the WSL instance.

Example below: Enable traffic forwarding from port 8877 on the windows host to port 8880 on the WSL 
```bash
netsh interface portproxy add v4tov4 listenport=8877 listenaddress=0.0.0.0 connectport=8880 connectaddress=172.24.142.7
```

#### 3. Check the proxies
```bash
netsh interface portproxy show all
```
Obs.: It is possible to delete rules based on the command `netsh int portproxy reset all`

#### 4. Test the connection
```bash
telnet <HOST_LAN_IP> <listenport>
telnet 10.10.10.100 8877
```





