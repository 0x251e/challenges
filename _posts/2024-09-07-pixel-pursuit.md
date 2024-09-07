---
title: 'Pixel Pursuit: Tracking the Leak'
time: 2024-09-07
categories: [forensic]
tags: [easy, wireshark]
image: /assets/posts/chall_category/forensic.jpg
---

## Description:
You have been hired as a forensic analyst for SOC101, a growing cybersecurity firm. Recently, their internal mail server has come under suspicion of being compromised. A series of suspicious emails have been flagged by the IT team, and they believe one of these emails contains a hidden tracker designed to leak sensitive information.

Your task is to analyze the provided packet capture (PCAP) file from the company’s mail server traffic. Within this data, one of the emails contains a tracking pixel image designed to communicate with an external server. The flag is embedded in this pixel image.

- Category: Forensic
- **Flag format:** CTF{flag}

<button onclick="downloadFile()">Download File</button>

<script>
function downloadFile() {
    const link = document.createElement('a');
    link.href = 'https://github.com/0x251e/challenges/raw/main/union-depository/forensic/pixel-pursuit/pixel-pursuit.pcapng';
    link.download = 'pixel-pursuit.pcapng';
    link.click();
}
</script>


