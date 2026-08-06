# Linux Notes  

  

## Introduction  

  

This file contains my notes from the beginning of my Linux learning journey. I intend to use these notes to regularly recap and reinforce my knowledge as I continue developing my skills in Linux and DevOps.  

  

## What is Linux?  

  

Linux is an open-source operating system built around the Linux kernel.  

  

The Linux kernel is the core component of the operating system. It manages hardware resources and allows software to communicate with the hardware.  

  

### Linux Architecture  

  

```text  

Applications  

│  

▼  

Operating System  

│  

▼  

Linux Kernel  

│  

▼  

Hardware  

```  

  

### Founder  

  

- Linus Torvalds created the Linux kernel in 1991.  

  

---  

  

## Linux Distributions  

  

A Linux distribution (distro) is an operating system built around the Linux kernel.  

  

- Most Linux distributions are very similar.  

- They all use the Linux kernel.  

- The main differences are:  

- Package manager  

- Default software  

- Configuration  

- Release cycle  

  

### Examples  

  

- Ubuntu → uses `apt`  

- Fedora → uses `dnf`  

- Arch Linux → uses `pacman`  

  

---  

  

## Linux Command Structure  

  

Commands are instructions entered into a shell to tell the operating system to perform specific tasks.  

  

### Structure  

  

```text  

ls -l /home  

  

│ │ └─ Argument  

│ └────── Option  

└───────── Command  

```  

  

### Components  

  

- **Command** → The program or action to run.  

- **Option** → Modifies how the command behaves.  

- **Argument** → The target of the command.  

  

---  

  

## Shells  

  

A shell is a command-line interface (CLI) that allows users to interact with the operating system by entering commands.  

  

The shell interprets commands and passes them to the operating system for execution.  

  

### Examples  

  

- Bash  

- Zsh  

- Fish  

- PowerShell  

  

---  

  

## Programs and Binaries  

  

### Programs  

  

Programs are sets of instructions written by developers to perform specific tasks.  

  

Examples:  

  

- Web browsers  

- Text editors  

- Games  

- Linux utilities such as `ls` and `cp`  

  

### Binaries  

  

A binary is a compiled version of a program that the computer can execute.  

  

Examples:  

  

- `/bin/ls`  

- `/bin/cp`  

- `/usr/bin/git`  

  

### Program vs Binary  

  

```text  

Source Code  

│  

▼  

Compiler  

│  

▼  

Binary  

│  

▼  

Executed by the OS  

```  

  

---  

  

## Linux File System  

  

Linux uses a hierarchical file system that starts from a single root directory:  

  

```text  

/  

```  

  

Everything in Linux exists under the root directory.  

  

### Common Directories  

  

- `/` → Root directory  

- `/home` → User home directories  

- `/root` → Home directory of the root user  

- `/etc` → System configuration files  

- `/bin` → Essential command binaries  

- `/usr` → User applications and utilities  

- `/var` → Variable data such as logs  

- `/tmp` → Temporary files  

- `/boot` → Files required for system startup  

- `/dev` → Device files  

  

### Example Path  

  

```text  

/home/abdi/Documents  

```  

  

- `/` → Root directory  

- `home` → Home directory location  

- `abdi` → User directory  

- `Documents` → Folder inside the user's home directory  

  

---  

  

## File Permissions  

  

File permissions control who can read, write, or execute files and directories.  

  

Permissions are assigned to:  

  

- Owner  

- Group  

- Others  

  

### Permission Values  

  

```text  

Read = 4  

Write = 2  

Execute = 1  

```  

  

### Example  

  

```text  

-rwxr-xr-x  

```  

  

```text  

Owner = 7  

Group = 5  

Other = 5  

  

755  

```  

  

---  

  

## Standard Input, Output and Error Streams  

  

Linux programs use three standard streams:  

  

| Stream | Number | Purpose |  

|----------|----------|----------|  

| Standard Input (stdin) | 0 | Receives input |  

| Standard Output (stdout) | 1 | Displays normal output |  

| Standard Error (stderr) | 2 | Displays error messages |  

  

### Revision Tip  

  

```text  

0 = Input  

1 = Output  

2 = Error  

```  

  

---  

  

## Environment Variables  

  

Environment variables are named values stored by the operating system that can be used by programs and the shell.  

  

### Common Variables  

  

- `HOME` → Current user's home directory  

- `USER` → Current username  

- `PATH` → Directories searched for commands  

- `PWD` → Current working directory  

- `SHELL` → Current shell  

  

### PATH  

  

The `PATH` variable tells Linux where to look for executable files when a command is run.  

  

---  

  

## Aliases  

  

Aliases are shortcuts for commands.  

  

Example:  

  

```bash  

alias ll='ls -l'  

```  

  

Running:  

  

```bash  

ll  

```  

  

is equivalent to:  

  

```bash  

ls -l  

```  

  

---  

  

## Users and Groups  

  

Linux is a multi-user operating system.  

  

Each user:  

  

- Has a username  

- Belongs to one or more groups  

- Has specific permissions  

  

Special user:  

  

- `root` → Administrator account  

  

---  

  

## Linux Philosophy  

  

- Everything starts from the root directory (`/`).  

- Linux is case-sensitive.  

- Everything is treated as a file.  

- Linux supports multiple users.  

- Most administration tasks can be performed from the command line.  

  

---  

  

## Quick Revision  

  

- Linux is built around the Linux kernel.  

- The kernel manages hardware and system resources.  

- Distributions are operating systems built around the Linux kernel.  

- A shell allows users to interact with the operating system.  

- Commands consist of commands, options, and arguments.  

- Programs are sets of instructions that perform tasks.  

- Binaries are compiled programs that can be executed.  

- Linux uses a hierarchical file system starting from `/`.  

- File permissions are based on owner, group, and others.  

- Linux uses three standard streams:  

- stdin (0)  

- stdout (1)  

- stderr (2)  

- Environment variables store configuration information.  

- The `PATH` variable tells Linux where to find executables.  

- Aliases are shortcuts for commands.  

- Linux is a multi-user operating system.