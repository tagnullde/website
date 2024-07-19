---
title: Traceback
date: 2020-08-15
# bookComments: false
# bookSearchExclude: false
---

<p align="center">
  <img src="traceback-banner.png" />
</p>

***

# External Recon

Welcome to my first box and writeup since my OSCP. 
We start with a nmap scan as usual:

![nmap](nmap_scan.png)

# Website

Checking the website it seems like somebody already defaced the website.

![ownd_site](owned_site.png)

We find a little hint in the sourcecode.

![websource_code](websource_code.png)

A google search on "webshells + Xh4H" reveals a [github repository](https://github.com/Xh4H/Web-Shells)
with a bunch of webshells. And sure enough we try all of them on our target.

![webshell_github](webshell_github.png)

![sample_shells](sample_shells.png)

The `smevk` webshell works!

![smevk_webshell](smevk_webshell.png)

Checking the github repository for credentials reveals `admin:admin` in the config.

![smevk_creds](smevk_creds.png)

After logging in the next step was to upload a propper [php-reverse-shell](https://github.com/pentestmonkey/php-reverse-shell) to get some sane control over the machine.

![upload_revshell](upload_revshell.png)

I created a `nc` listener on `port 9001` and called the reverse-shell via the browser.

![initial_shell](initial_shell.png)

# User PrivEsc

As seen in the above screenshot, we have `webadmin` permissions. So let's go and check his home directory.

![webadmin_note](webadmin_note.png)

The user `Sysadmin` left a note about a tool `webadmin` might want to practice with.
Running `sudo -l` leaked the tool in question and the info that we can run it without the password from `Sysadmin`.

![sudo_l](sudo_l.png)

Futher investigation reveal more useful information. In the history-file you can see how the command was used by the attacker that defaced the box.

![history](history.png)

It looks like a `.lua` file is needed and can be passed as an argument to the `luvit` tool from "sysadmin". I checked the [gtfobins website](https://gtfobins.github.io/gtfobins/lua/) to see what I can do with lua. 

![gtfo_lua](gtfo_lua.png)

After creating a file with `os.execute("/bin/bash")` as content and naming the file `privesc.lua`, I was able to privesc to `Sysadmin` and capture the user flag.

![privesc_userflag](privesc_userflag.png)

# Enumeration of Sysadmin

With the new privileges at hand I uploaded two of my goto tools to the system. `LinPEAS` and `pspy64`. Neither disappoint in this scenario.
I sifted through the `LinPEAS` output and found some very promissing information.

![motd_linpeas](motd_linpeas.png)

Pspy64 confirmed that something is about the `motd` (motto-of-the-day) files as they are constantly restored by a cronjob.

![pspy](pspy.png)

Before we move on to root the box I went and created an ssh-key for sysadmin to get a better and more stable shell. After logging in I noticed
the custom banner from the initial attacker. 

![ssh_banner](ssh_banner.png)

# Root

So after enumerating the Sysadmin-User I checked the motd files. The `00-header` file was particilar interessting.

![motd_header](motd_header.png)

If you check the very last line you can see that it's the same we saw after using our ssh-key for Sysadmin.
The privesc path should be clear at this point. 

The motd files are essentially bash-scripts and Sysadmin can edit them. But they are run by root once you log in via ssh.

So I appended a reverse-shell to the `00-header` file and had a listener ready to capture the shell. 
As we know through our enumeration, the file will be restored every couple of seconds. So we need to be quick.

Append the shell, login as Sysadmin and capture the shell.

![root_privesc](root_privesc.png)

![root_shell](root_shell.png)

Easy as that. :) 

See you in a bit!

x41

