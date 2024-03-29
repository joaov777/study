### - Redirect traffic from 8888 remotely to localhost (locally) on port 8000
#### Purpose: Good for accessing home resources without further configuration
```bash
ssh -N -R 8888:localhost:8000 joao@localdev.ifce.edu.br &
```



### - Access localhost:8887 locally instead of localdev.ifce.edu.br:8000
#### Purpose: Good for accessing external resources without displaying URL and real ports
```bash
ssh -N -L 8887:localhost:8000 joao@localdev.ifce.edu.br &
ssh -N -L 7777:localhost:8000 joao@localdev.ifce.edu.br
```
