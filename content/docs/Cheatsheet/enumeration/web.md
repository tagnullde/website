---
title: web
weight: 21
---

# ferox
----------------

basic usage
```shell
feroxbuster -u http://target-ip -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
----------------


# gobuster
----------------

bruteforce webdirectories and files by extention
```shell
gobuster dir -u http://target-ip -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt -t 30
```
----------------

# wfuzz
----------------

bruteforce web parameter
```shell
wfuzz -u http://target-ip/path/index.php?param=FUZZ -w /usr/share/wordlists/rockyou.txt
```

bruteforce post data (login)
```shell
wfuzz -u http://target-ip/path/index.php?action=authenticate -d 'username=admin&password=FUZZ' -w /usr/share/wordlists/rockyou.txt
```
----------------


# fuff
----------------

bruteforce web directories
```shell
ffuf -w /path/to/wordlist -u https://target/FUZZ
```
----------------


# davtest
----------------

tries to upload (executable) files to webdav
```shell
davtest -url http://target-ip/ -sendbd auto
```
----------------


# nikto
----------------

scan website for vulnerabilities
```shell
nikto -C all -h http://target-ip
```
----------------

# wpscan
----------------

scan wordpress installation for vulnerabilities
```shell
wpscan --url http://target-ip/ --enumerate p
```
----------------
