---
title: Financial Fallout
time: 2024-09-17
categories: [forensic]
tags: [memory forensic, medium]
image: /assets/posts/chall_category/forensic.jpg
---

## Description:

A finance department employee opened a spreadsheet using OpenOffice to view financial data. Unknown to the employee, this spreadsheet contained a malicious payload that exploited the machine with CSV injection vulnerability. The exploit led to the download and execution of malware, establishing a reverse shell connection to an external server.

The company's IT security team detected this event and isolated the machine. They've provided you with a memory dump for analysis. Your task is to analyze the memory dump and find out the location of the hidden malware and modification of files perform by the malware. 

This challenge demonstrates the vulnerability of CSV injection with DDE payloads on Apache OpenOffice before 4.1.1 **(CVE-2014-3524)**. 

- Category: Forensic
- **Flag format:** CTF{flag} (There are two parts of the flag)

<script>
function downloadFile() {
    const link = document.createElement('a');
    link.href = 'https://drive.google.com/file/d/1M7Pn7_5X_OI9SB6DQFLAYUTvoLN2A_a_/view?usp=sharing';
    link.download = 'memdump-zip';
    link.click();
}
</script>



