---
title: smb
weight: 24
---

# mount
----------------

mount shares
```shell
mount -o hard,nolock target-ip:/home folder
```
```shell
mount -t cifs -o user=username,domain=domainname //target-ip/share /mnt/folder
```
```shell
mount -t nfs target-ip:share /mnt/folder -o nolock
```
----------------

list Shares

```shell
showmount -e target-ip
```
----------------