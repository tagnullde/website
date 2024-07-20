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

host discovery for fast scan
```shell
nmap -sn -v -oA nmap/host_discovery target-ip
```

find all host that are up
```shell
grep "Up" nmap/host_discovery.gnmap | awk '{print $2}' > ips_host_discovery.tx
```

scan only hosts that are up
```shell
nmap -p- -sC -sV -T5 --min-parallelism 100 -oA nmap/all_ports -iL host_discovery -v
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
todo

----------------

# snmpwalk
----------------

## gather snmp v1 information with standard community strings
```shell
snmpwalk -v1 -c public target-ip
```
```shell
snmpwalk -v1 -c private target-ip
```
```shell
snmpwalk -v1 -c manager target-ip
```

## enumerate windows users
```shell
snmpwalk -c public -v1 target-ip 1.3.6.1.4.1.77.1.2.25
```
    
## enumerate current windows processes
```shell
snmpwalk -c public -v1 target-ip 1.3.6.1.2.1.25.4.2.1.2
```
    
## enumerate windows open tcp ports
```shell
snmpwalk -c public -v1 target-ip 1.3.6.1.2.1.6.13.1.3
```
 
## enumerate installed software
```shell
snmpwalk -c public -v1 target-ip 1.3.6.1.2.1.25.6.3.1.2
```

## make use of MIB files and translate the OIDs automatically
- default folder for MIB files: `/usr/share/snmp/mibs`
```shell
export MIBS=ALL
```
----------------

# onesixtyone
----------------

## bruteforce community strings
```shell
echo public > community.txt
echo private >> community.txt
echo manager >> community.txt
for ip in $(seq 200 254); do echo 1.2.3.${ip}; done > target-ip.txt
```

```shell
onesixtyone -c community.txt -i target-ip.txt
```
----------------


# dig
----------------

full zone transfer
```shell
dig -t AXFR target-dns-ip
```
# host
----------------

full zone transfer
```shell
host -l target-dns-ip
```
----------------