---
title: operating system
weight: 22
---

# peass - privilege escalation awesome scripts suite
----------------

very easy to use on linux
```shell
./linpeas.sh
```

windows has multiple versions
- `winpeasx64.exe`
- `winpeasx86.exe`
- `winpeas.bat`

registry entry for winpeas colors
```shell
REG ADD HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1
```
----------------

# enum4linux
----------------

scan target-ip
```shell
enum4linux target-ip
```
----------------

# rpcdump.py
----------------

dump rpc endpoints
```shell
/opt/impacket/examples/rpcdump.py username:password@target-ip
```
----------------

# lookupsid.py
----------------

get sid via rpc
```shell
/opt/impacket/examples/lookupsid.py username:password@target-ip
```
----------------


# rpcclient
----------------

get information via rpc with username
```shell
rpcclient -U username target-ip
```

get information via rpc without username
```shell
rpcclient -U "" target-ip
```

sub-commands once connected
```shell 
srvinfo
```
```shell
lookupnames username
```
----------------