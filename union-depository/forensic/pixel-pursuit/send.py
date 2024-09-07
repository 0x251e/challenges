import telnetlib
import time

# SMTP server details
smtp_server = "localhost"
port = 25
sender = "johndoe@tesla.com"
recipient = "soc101@localhost"

# Start a Telnet session
tn = telnetlib.Telnet(smtp_server, port)

def send_command(command):
    print(f"Sending: {command.strip()}")
    tn.write(command.encode('ascii') + b"\r\n")
    time.sleep(1)
    response = tn.read_until(b"\n", timeout=2).decode('ascii')
    print(f"Response: {response.strip()}")
    return response

# Loop to send 50 emails
for i in range(50):
    subject = f"Test Email #{i+1}"  # Unique subject for each email
    body = f"This is email number {i+1}.\nIt is part of a batch of 50 emails sent via Telnet.\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    # Generate a unique message for each email
    message = f"""From: {sender}
To: {recipient}
Subject: {subject}

{body}
"""

    # Send SMTP commands for each email
    send_command("HELO yourdomain.com")
    send_command(f"MAIL FROM:<{sender}>")
    send_command(f"RCPT TO:<{recipient}>")
    send_command("DATA")
    tn.write(message.encode('ascii') + b"\r\n.\r\n")  # Send the message followed by a period
    time.sleep(2)
    print(tn.read_until(b"\n", timeout=2).decode('ascii'))

# Quit the session
send_command("QUIT")

# Close the connection
tn.close()
