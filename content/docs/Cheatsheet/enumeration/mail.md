---
title: mail
weight: 20
---

# smtp-user-enum
----------------

verify that user exists on system with higher delay to make sure we get all responses

```shell
smtp-user-enum -M VRFY -U user-file -t target-ip -m 60 -w 20
```

----------------