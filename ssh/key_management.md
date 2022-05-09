# A few tips on how to manage SSH keys

## Create keys

```bash
ssh-keygen
ssh-keygen -t ed25519 -C "unique name to identify this key."
ssh-keygen -t ed25519 -C "$(whoami)@$(hostname)"
```

## Set password (passphrase)

## Start the SSH agent

```bash
ssh-agent -s
eval `ssh-agent -s`
```

## Create config file

```bash
vim ~/.ssh/config
```

## Remove all keys from currently active ssh-agent session

```bash
ssh-add -D
```

## Add the key to the keychain (enter the passphrase once and then not anymore)

```bash
ssh-add -K ~/.ssh/PRIVATE_KEY
ssh-add ~/.ssh/PRIVATE_KEY

ssh-add -l
```

## Avoid passphrase prompting

```bash
 Host *
 AddKeysToAgent yes
 IgnoreUnknown UseKeychain
 UseKeychain yes
 IdentityFile <PATH_TO_PRIVATE_KEY>
```

## Check the key fingerprint

```bash
ssh-keygen -l -f <key file>
```
