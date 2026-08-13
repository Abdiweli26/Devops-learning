# Common Linux Interview Questions

## Linux Fundamentals

### What is Linux?

Linux is an open-source operating system built around the Linux kernel.

---

### What is the Linux Kernel?

The Linux kernel is the core component of the operating system responsible for managing hardware, memory, processes, and communication between software and hardware.

---

### What is a Linux Distribution?

A Linux distribution (distro) is an operating system built around the Linux kernel.

Examples:

- Ubuntu
- Debian
- Fedora
- Arch Linux

---

### What is a Shell?

A shell is a command-line interface that allows users to interact with the operating system.

Examples:

- Bash
- Zsh
- Fish

---

### What is the difference between a Program and a Process?

Program:
- A file containing instructions stored on disk.

Process:
- A running instance of a program.

---

### What is the difference between Linux and Unix?

Unix is a family of proprietary operating systems.

Linux is an open-source Unix-like operating system.

---

## Linux File System

### What is the root directory?

The root directory is the top-level directory in Linux represented by:

```text
/
```

All files and directories exist underneath it.

---

### What is the purpose of /home?

Stores user home directories.

Example:

```text
/home/abdi
```

---

### What is the purpose of /etc?

Stores system configuration files.

---

### What is the purpose of /var?

Stores variable data such as:

- Logs
- Cache
- Mail queues

---

### What is the purpose of /tmp?

Stores temporary files.

---

### What is the purpose of /bin?

Contains essential command binaries.

Examples:

```bash
ls
cp
mv
```

---

## Navigation Commands

### What does pwd do?

Displays the current working directory.

---

### What does cd do?

Changes the current directory.

---

### What is the difference between an absolute path and a relative path?

Absolute Path:

Starts from the root directory.

Example:

```text
/home/abdi/Documents
```

Relative Path:

Depends on the current location.

Example:

```text
Documents
```

---

### What does cd .. do?

Moves up one directory.

---

### What does cd ~ do?

Moves to the user's home directory.

---

### What is the difference between . and .. ?

```text
.  = Current directory

.. = Parent directory
```

---

### What is the difference between find and locate?

find:
- Searches the filesystem directly
- More accurate
- Slower

locate:
- Uses a database
- Faster
- May be outdated

---

### What does which do?

Displays the location of an executable.

Example:

```bash
which git
```

---

## File Management

### What is the difference between cp and mv?

cp:
- Copies files or directories

mv:
- Moves or renames files and directories

---

### What is the difference between rm -r and rmdir?

rmdir:
- Removes empty directories only

rm -r:
- Removes directories and their contents

---

### What is the purpose of touch?

Creates an empty file.

---

### What is the purpose of mkdir?

Creates directories.

---

### What is the difference between head and tail?

head:
- Displays the beginning of a file

tail:
- Displays the end of a file

---

### Why is tail -f commonly used?

To monitor logs in real time.

---

## File Permissions

### What are Linux permissions?

Permissions determine who can:

- Read
- Write
- Execute

files and directories.

---

### What do the values 4, 2 and 1 represent?

```text
4 = Read

2 = Write

1 = Execute
```

---

### What does chmod 755 mean?

```text
Owner = rwx = 7

Group = r-x = 5

Others = r-x = 5
```

---

### What does chmod 777 mean?

Provides:

```text
Read
Write
Execute
```

for everyone.

Generally considered insecure.

---

### What is the difference between chmod and chown?

chmod:
- Changes permissions

chown:
- Changes ownership

---

### What is the difference between a User, Group and Others?

User:
- File owner

Group:
- Members of the assigned group

Others:
- Everyone else

---

## Streams and Redirection

### What is stdin?

Standard Input.

```text
0
```

---

### What is stdout?

Standard Output.

```text
1
```

---

### What is stderr?

Standard Error.

```text
2
```

---

### What is the difference between > and >> ?

```text
>  Overwrites a file

>> Appends to a file
```

---

### What does 2> do?

Redirects standard error.

---

### What does 2>&1 do?

Redirects stderr to stdout.

---

### What is a Pipe?

A pipe (`|`) passes output from one command as input to another command.

Example:

```bash
ls -l | grep notes
```

---

### What is /dev/null?

A special file that discards anything written to it.

---

## Search Commands

### What does grep do?

Searches for text patterns.

---

### What is the difference between grep and find?

grep:
- Searches text inside files

find:
- Searches for files and directories

---

### What does awk do?

Processes and extracts data from text.

---

### What does sed do?

Searches and modifies text.

---

### What does wc do?

Counts:

- Lines
- Words
- Characters

---

## Environment Variables

### What is an Environment Variable?

A named value used by the shell and applications.

---

### What is PATH?

PATH contains directories Linux searches when running commands.

---

### Why is PATH important?

Without PATH, Linux would not know where to locate executables.

---

### What is the difference between a local variable and an exported variable?

Local:
- Current shell only

Exported:
- Available to child processes

---

### How do you display an environment variable?

```bash
echo $VARIABLE
```

---

## Aliases

### What is an Alias?

A shortcut for a command.

Example:

```bash
alias ll='ls -la'
```

---

### How do you view aliases?

```bash
alias
```

---

### How do you remove an alias?

```bash
unalias alias_name
```

---

### Where are permanent aliases usually stored?

```text
~/.bashrc
```

---

## User Management

### What is a User ID (UID)?

A unique identifier assigned to every user.

---

### What is the root user?

The administrator account with unrestricted access.

---

### What is the difference between su and sudo?

su:
- Switches users

sudo:
- Runs a command as another user

---

### What file stores user information?

```text
/etc/passwd
```

---

### What file stores passwords?

```text
/etc/shadow
```

---

### What file stores group information?

```text
/etc/group
```

---

### How do you add a user?

```bash
sudo adduser username
```

---

### How do you delete a user?

```bash
sudo userdel -r username
```

---

## Process Management

### What is a Process?

A running instance of a program.

---

### What is a PID?

Process ID.

A unique identifier assigned to every process.

---

### What does ps do?

Displays running processes.

---

### What does top do?

Displays real-time process information.

---

### What is the difference between top and htop?

top:
- Basic process monitor

htop:
- More interactive and user-friendly

---

### What is the difference between kill and kill -9?

kill:
- Graceful termination

kill -9:
- Forcefully terminates a process

---

### What does nohup do?

Allows a process to continue running after logout.

---

## Package Management

### What is a Package?

A bundle containing:

- Software
- Dependencies
- Configuration files
- Metadata

---

### What is apt?

A package manager used by Debian-based distributions.

---

### What is the difference between apt update and apt upgrade?

apt update:
- Refreshes package information

apt upgrade:
- Installs updates

---

### What is a Dependency?

Software required by another application.

---

### What is a Package Repository?

An online location where packages are stored.

---

## Networking

### What does ping do?

Tests network connectivity.

---

### What is DNS?

DNS translates domain names into IP addresses.

---

### What does nslookup do?

Queries DNS records.

---

### What is the difference between curl and wget?

curl:
- Transfers data
- Often used with APIs

wget:
- Downloads files

---

### What command displays IP addresses?

```bash
ip addr
```

---

### What is a Port?

A logical communication endpoint used by network services.

Examples:

```text
22   SSH
80   HTTP
443  HTTPS
```

---

### What does netstat or ss show?

Network connections and listening ports.

---

## SSH

### What does SSH stand for?

Secure Shell.

---

### What is SSH used for?

Secure remote access to another machine.

---

### What is the default SSH port?

```text
22
```

---

### What is the difference between SCP and SFTP?

SCP:
- Secure file copy

SFTP:
- Interactive file transfer

---

### What does ssh-keygen do?

Generates SSH key pairs.

---

### What is the difference between a public key and a private key?

Public Key:
- Shared with servers

Private Key:
- Kept secret

---

### What file stores allowed SSH public keys?

```text
~/.ssh/authorized_keys
```

---

## System Administration

### How do you check disk usage?

```bash
df -h
```

---

### How do you check directory sizes?

```bash
du -sh *
```

---

### How do you view memory usage?

```bash
free -h
```

---

### How do you check system uptime?

```bash
uptime
```

---

### Where are Linux logs commonly stored?

```text
/var/log
```

---

### How do you view system logs?

```bash
journalctl
```

---

### How do you monitor logs in real time?

```bash
tail -f logfile.log
```

or

```bash
journalctl -f
```

---

## Common Scenario Questions

### A service is not working. What would you check first?

- Service status
- Logs
- Running processes
- Network connectivity
- Configuration files

---

### A server is running slowly. What would you check?

- CPU usage (`top`)
- Memory usage (`free -h`)
- Disk usage (`df -h`)
- Running processes (`ps aux`)
- System logs

---

### A user cannot access a file. What would you check?

- Ownership (`ls -l`)
- Permissions (`chmod`)
- Group membership (`groups`)
- Parent directory permissions

---

### You can't SSH into a server. What would you check?

- Network connectivity (`ping`)
- SSH service status
- Port 22 availability
- Firewall rules
- SSH logs