# SSH (Secure Shell)

## Quick Revision

| Command | Purpose |
|----------|----------|
| ssh | Connect to a remote machine |
| ssh-keygen | Generate SSH keys |
| ssh-copy-id | Copy SSH key to a remote machine |
| scp | Securely copy files |
| sftp | Secure file transfer |
| ssh -p | Connect using a specific port |
| exit | Disconnect from a remote machine |

### Most Common Commands

```bash
ssh user@server

ssh user@192.168.1.10

ssh-keygen

ssh-copy-id user@server

scp file.txt user@server:/home/user
```

---

# What is SSH?

SSH (Secure Shell) is a secure protocol used to remotely access and manage computers over a network.

SSH encrypts all communication between devices.

Common uses:

- Remote server management
- File transfers
- Running remote commands
- Git authentication
- System administration

---

## SSH Architecture

```text
Client
  │
  ▼
SSH Connection
  │
  ▼
Remote Server
```

Example:

```bash
ssh abdi@192.168.1.10
```

```text
Your PC
   │
   ▼
SSH
   │
   ▼
Linux Server
```

---

## ssh

### What Does It Do?

Connects to a remote machine.

### Syntax

```bash
ssh user@host
```

### Examples

Using hostname:

```bash
ssh abdi@server1
```

Using IP Address:

```bash
ssh abdi@192.168.1.10
```

---

## Connect Using a Specific Port

### Syntax

```bash
ssh -p port user@host
```

### Example

```bash
ssh -p 2222 abdi@192.168.1.10
```

### Notes

Default SSH port:

```text
22
```

---

## Running Commands Remotely

Instead of logging in interactively:

```bash
ssh user@server "hostname"
```

Example:

```bash
ssh abdi@server "uptime"
```

Output:

```text
14:35:20 up 10 days
```

---

## Disconnect from SSH

Exit the remote session:

```bash
exit
```

or

```text
Ctrl + D
```

---

# SSH Keys

## What are SSH Keys?

SSH keys provide a more secure alternative to passwords.

SSH uses:

```text
Private Key
     │
     ▼
Authentication
     │
     ▼
Public Key
```

### Benefits

- More secure than passwords
- Convenient authentication
- Used heavily in DevOps and Git

---

## Generate SSH Keys

### Syntax

```bash
ssh-keygen
```

### Example

```bash
ssh-keygen -t rsa -b 4096
```

Press Enter to accept defaults.

Files created:

```text
~/.ssh/id_rsa
~/.ssh/id_rsa.pub
```

### Notes

```text
id_rsa      = Private key
id_rsa.pub  = Public key
```

Never share your private key.

---

## View Public Key

```bash
cat ~/.ssh/id_rsa.pub
```

Example:

```text
ssh-rsa AAAAB3...
```

---

## Copy Public Key to Server

### Syntax

```bash
ssh-copy-id user@host
```

### Example

```bash
ssh-copy-id abdi@192.168.1.10
```

### What Happens?

The public key is copied to:

```text
~/.ssh/authorized_keys
```

on the remote server.

---

## Passwordless Authentication

After adding your public key:

```bash
ssh user@server
```

You can log in without entering a password.

---

# SCP (Secure Copy)

## What Does It Do?

Securely copies files between machines using SSH.

### Copy Local File to Remote Server

```bash
scp notes.txt user@server:/home/user
```

### Copy Remote File to Local Machine

```bash
scp user@server:/home/user/notes.txt .
```

### Copy Directory

```bash
scp -r Projects user@server:/home/user
```

---

# SFTP (Secure File Transfer Protocol)

## What Does It Do?

Transfers files over SSH.

### Connect

```bash
sftp user@server
```

### Commands

Upload file:

```bash
put file.txt
```

Download file:

```bash
get file.txt
```

List files:

```bash
ls
```

Exit:

```bash
exit
```

---

# Common SSH Files

SSH configuration directory:

```text
~/.ssh
```

Common files:

```text
id_rsa
id_rsa.pub
authorized_keys
known_hosts
config
```

---

## known_hosts

Stores fingerprints of previously connected hosts.

View:

```bash
cat ~/.ssh/known_hosts
```

---

## authorized_keys

Contains public keys allowed