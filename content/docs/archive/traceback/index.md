---
title: "HTB-Writeup - Traceback"
date: 2020-08-15
# bookComments: false
# bookSearchExclude: false
---

{{< banner "traceback-banner.png" "HTB Traceback badge: a detective with a magnifying glass and footprints" >}}

***

# External Recon

Welcome to my first box and writeup since my OSCP. 
We start with an nmap scan as usual:

![Nmap scan results showing SSH and HTTP ports](nmap_scan.png)

# Website

Checking the website it seems like somebody already defaced the website.

![Defaced website message from attacker Xh4H](owned_site.png)

We find a little hint in the sourcecode.

![HTML source code with hidden webshell hint comment](websource_code.png)

A google search on "webshells + Xh4H" reveals a [github repository](https://github.com/Xh4H/Web-Shells)
with a bunch of webshells. And sure enough we try all of them on our target.

![Google search result for Xh4H Web-Shells GitHub repo](webshell_github.png)

![List of PHP webshell files in the repository](sample_shells.png)

The `smevk` webshell works!

![SmEvK webshell login page](smevk_webshell.png)

Checking the github repository for credentials reveals `admin:admin` in the config.

![SmEvK config file showing admin credentials](smevk_creds.png)

After logging in the next step was to upload a proper [php-reverse-shell](https://github.com/pentestmonkey/php-reverse-shell) to get some sane control over the machine.

![Uploading php-reverse-shell.php via the webshell](upload_revshell.png)

I created a `nc` listener on `port 9001` and called the reverse-shell via the browser.

![Reverse shell connected as webadmin user](initial_shell.png)

# User PrivEsc

As seen in the above screenshot, we have `webadmin` permissions. So let's go and check his home directory.

![note.txt left by sysadmin in home directory](webadmin_note.png)

The user `Sysadmin` left a note about a tool `webadmin` might want to practice with.
Running `sudo -l` leaked the tool in question and the info that we can run it without the password from `Sysadmin`.

![sudo -l output showing luvit permission](sudo_l.png)

Further investigation reveals more useful information. In the history-file you can see how the command was used by the attacker that defaced the box.

![Bash history revealing privesc.lua commands](history.png)

It looks like a `.lua` file is needed and can be passed as an argument to the `luvit` tool from "sysadmin". I checked the [gtfobins website](https://gtfobins.github.io/gtfobins/lua/) to see what I can do with lua. 

![GTFOBins Lua shell command entry](gtfo_lua.png)

After creating a file with `os.execute("/bin/bash")` as content and naming the file `privesc.lua`, I was able to privesc to `Sysadmin` and capture the user flag.

![Sysadmin shell after privesc showing user.txt](privesc_userflag.png)

# Enumeration of Sysadmin

With the new privileges at hand I uploaded two of my goto tools to the system. `LinPEAS` and `pspy64`. Neither disappoints in this scenario.
I sifted through the `LinPEAS` output and found some very promising information.

![LinPEAS output showing writable motd files](motd_linpeas.png)

Pspy64 confirmed that something is about the `motd` (motto-of-the-day) files as they are constantly restored by a cronjob.

![pspy output showing motd restore cronjob](pspy.png)

Before we move on to root the box I went and created an ssh-key for sysadmin to get a better and more stable shell. After logging in I noticed
the custom banner from the initial attacker. 

![SSH login banner left by attacker Xh4H](ssh_banner.png)

# Root

So after enumerating the Sysadmin-User I checked the motd files. The `00-header` file was particularly interesting.

![Contents of the 00-header motd script](motd_header.png)

If you check the very last line you can see that it's the same we saw after using our ssh-key for Sysadmin.
The privesc path should be clear at this point. 

The motd files are essentially bash-scripts and Sysadmin can edit them. But they are run by root once you log in via ssh.

So I appended a reverse-shell to the `00-header` file and had a listener ready to capture the shell. 
As we know through our enumeration, the file will be restored every couple of seconds. So we need to be quick.

Append the shell, log in as Sysadmin and capture the shell.

![Reverse shell payload appended to motd header](root_privesc.png)

![Root shell obtained via motd cronjob exploit](root_shell.png)

Easy as that. :) 

See you in a bit!

x41

