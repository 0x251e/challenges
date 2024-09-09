---
title: Lemon and Tangerine
time: 2024-08-27
categories: [crypto]
tags: [beginner, encoding]
image: /assets/posts/chall_category/crypto.jpg
---

## Description:

Description: My mom told me to buy lemons and tangerines but she only speaks binary, I totally forgot which is label as “1” or “0”.

- Category: Cryptography

**Flag format:** CTF{flag}

<button onclick="downloadFile()">Download File</button>

<script>
function downloadFile() {
    const link = document.createElement('a');
    link.href = 'https://raw.githubusercontent.com/0x251e/challenges/main/union-depository/crypto/lemon_and_tangerine.txt';
    link.download = 'lemon_and_tangerine.txt';
    link.click();
}
</script>

## Solutions:



```py
emoji_string = """
🍋🍊🍋🍋🍋🍋🍊🍊🍋🍊🍋🍊🍋🍊🍋🍋🍋🍊🍋🍋🍋🍊🍊🍋🍋🍊🍊🍊🍊🍋🍊🍊🍋🍊🍊🍋🍊🍊🍋🍊🍋🍊🍋🍋🍊🍊🍊🍊🍋🍊🍊🍋🍊🍊🍋🍊🍋🍊🍋🍊🍊🍊🍊🍊🍋🍊🍊🍊🍋🍋🍊🍊🍋🍊🍊🍋🍋🍋🍊🍊🍋🍋🍊🍊🍋🍋🍋🍋🍋🍋🍊🍊🍋🍋🍋🍊🍋🍊🍊🍋🍋🍊🍋🍋🍋🍊🍊🍋🍋🍊🍋🍊🍋🍊🍊🍋🍋🍊🍋🍋🍋🍊🍋🍊🍊🍊🍊🍊🍋🍊🍊🍋🍊🍊🍋🍊🍋🍋🍊🍊🍋🍋🍊🍊🍋🍊🍋🍊🍊🍊🍊🍊🍋🍊🍊🍋🍋🍋🍊🍋🍋🍋🍊🍊🍋🍋🍊🍊🍋🍊🍋🍋🍊🍋🍋🍊🍋🍊🍊🍋🍊🍊🍊🍋🍋🍊🍋🍋🍋🍊🍊🍊🍋🍊🍋🍊🍊🍊🍊🍊🍋🍊🍊🍋🍋🍋🍋🍊🍋🍊🍋🍊🍊🍊🍊🍊🍋🍊🍋🍋🍋🍊🍋🍋🍋🍊🍋🍊🍋🍊🍋🍊🍋🍊🍋🍋🍊🍊🍋🍊🍋🍊🍋🍋🍋🍋🍊🍋🍋🍊🍋🍋🍋🍋🍋🍊🍋🍊🍋🍊🍊🍋🍊🍋🍋🍊🍋🍊🍊🍋🍊🍋🍋🍊🍊🍊🍊🍊🍋🍊
"""

def decode(emoji):
  emoji_map = {"🍊":"1","🍋":"0"}
  binary = ""
  for e in emoji:
    binary+=emoji_map.get(e,"")
  return binary

flag = decode(emoji_string)
print(flag)
```

**Output:**: `0100001101010100010001100111101101101101010011110110110101011111011100110110001100110000001100010110010001100101011001000101111101101101001100110101111101100010001100110100100101101110010001110101111101100001010111110100010001010101010011010100001001000001010110100101101001111101`


```sh
echo "0100001101010100010001100111101101101101010011110110110101011111011100110110001100110000001100010110010001100101011001000101111101101101001100110101111101100010001100110100100101101110010001110101111101100001010111110100010001010101010011010100001001000001010110100101101001111101" | perl -lpe '$_=pack"B*",$_'
```


## Challenge Creation:

This challenge was inspired by the characters from the movie "Bullet Train". 
