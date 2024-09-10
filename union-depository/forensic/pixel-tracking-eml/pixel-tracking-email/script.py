#! /usr/bin/env python3 

import telnetlib
import time
import os
import time

stmp_server="localhost"
port=25
sender="elliot@allSafe.com"
recipient="trevor@localhost"
eml_folder="/home/trevor/Desktop/EmailGenerator/output"

tn=telnetlib.Telnet(stmp_server,port)
def send_command(command):
    print(f"Sending: {command.strip()}")
    tn.write(command.encode('utf-8')+b"\r\n")
    time.sleep(1)
    response=tn.read_until(b"\n",timeout=2).decode('utf-8')
    print(f"Response: {response.strip()}")
    return response

def read_eml_files(file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        return f.read()

eml_files=[f for f in os.listdir(eml_folder) if f.endswith('.eml')]

for i, eml_file in enumerate(eml_files):
    file_path=os.path.join(eml_folder,eml_file)
    message_content=read_eml_files(file_path)
    print(f"Sending email from file: {eml_file} ({i+1}/{len(eml_files)})")

    send_command("HELO localhost")
    send_command(f"MAIL FROM:<{sender}>")
    send_command(f"RCPT TO: <{recipient}>")
    send_command(f"DATA")
    tn.write(message_content.encode('utf-8') + b"\r\n.\r\n")
    time.sleep(1)
    print(tn.read_until(b"\n",timeout=2).decode('utf-8'))

send_command("QUIT")
tn.close()
