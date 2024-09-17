---
title: Pixel Pursuit
time: 2024-09-10
categories: [forensic]
tags: [wireshark, easy]
image: /assets/posts/chall_category/forensic.jpg
---

## Description:

You are hired as a forensic analyst in a particular company and given a task to analyze network traffic of a internal mail server. This internal mail server has come under suspicion of being compromised. A series of suspicious emails have been flagged by the IT team, and they believe one of these emails contains a hidden tracker designed to leak sensitive information.

Your task is to analyze the provided packet capture (PCAP) file from the company’s mail server traffic. One of the email looks suspicious compared to the others.

- Category: Forensic

- **Flag format:** CTF{flag}

<button onclick="downloadFile()">Download File</button>

<script>
function downloadFile() {
    const link = document.createElement('a');
    link.href = 'https://github.com/0x251e/challenges/raw/main/union-depository/forensic/pixel-tracking-eml/pixel-tracking-email/mail-server-localhost.pcapng';
    link.download = 'mail-server-localhost.pcapng';
    link.click();
}
</script>


