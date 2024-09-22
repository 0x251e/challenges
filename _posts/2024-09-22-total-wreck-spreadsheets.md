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


