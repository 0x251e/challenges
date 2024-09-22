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

#### 3. Extracting VBA macros from the spreadsheets

```
oledump Employee_Salaries_2024.xlsm
```

Output:
![solve3](/assets/posts/chall-writeup-img/total-wreck-spreadsheets/solve3.png)

Here we can noticed a capital **M** on `A3: M 7064 'VBA/Module1` which is a stream. Always take note on the **M** and **m** where **M** means that the macro is compressed where else **m** means is uncompressed, it could be metadata which is easier to analyze



