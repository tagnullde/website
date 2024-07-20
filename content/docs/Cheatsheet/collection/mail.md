---
title: mail
weight: 20
---

# telnet
----------------

end mail via telnet

```shell
# connect
telnet target-ip 25

# provide valid or fake email-address
EHLO username@domain.tld

# set mail-from
MAIL FROM: <username@domain>

# set recipient-to
RCPT TO: <target-username@target-domain.tld>

# set body and sent mail
DATA
354 Ok Send data ending with <CRLF>.<CRLF>
FROM: username@domain

Hallo World!
.
```

get mails via pop3

```shell
# connect
telnet target-ip 110

# login
USER username
PASS password

# list emails
LIST

# retrieve emails
RETR 1
```
----------------

# curl
----------------

download emails via curl
```shell
curl --insecure --url "imaps://target-domain/Drafts;UID=4" --user "username:password"
```

bypass useragent blacklisting
```shell
curl -A "Googlebot" http://target-ip/robots.txt
```
----------------