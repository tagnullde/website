---
title: network
weight: 20
---

# nmap
----------------

enumerate services and use default scripts  

```shell
nmap -sC -sV -oN normal.txt target-ip
```

scan all tcp ports  

```shell
nmap -p- -oN all_ports.txt target-ip
```

scan all udp ports  
```shell
nmap -p- -sU -oN all_udp_ports.txt target-ip
```

use script categories  
```shell
nmap --script vuln,safe,discovery -oN scan.txt target-ip
```

list all nse scripts  
```shell
ls -lh /usr/share/nmap/scripts/
```

nmap through socks4 proxy  
```shell
nmap --proxies socks4://proxy-ip:1080 target-ip
```

ftp bounce scan
```shell
nmap -P0 -n -b username:password@target-ip target2-ip --proxies socks4://proxy-ip:1080 -vvvv
```
----------------

# massscan
----------------
tbd