# Aliases

## What are Aliases?

Aliases are command shortcuts that allow you to replace long or frequently used commands with shorter, custom commands.

They help improve productivity and reduce typing when working in the terminal.

---

## Why Use Aliases?

Benefits:

- Save time
- Reduce typing
- Simplify complex commands
- Create memorable command names
- Improve workflow efficiency

Example:

Without alias:

```bash
ls -la
```

With alias:

```bash
ll
```

---

## Viewing Existing Aliases

Display all aliases currently configured:

```bash
alias
```

Example output:

```text
alias ll='ls -la'
alias grep='grep --color=auto'
```

---

## Creating an Alias

### Syntax

```bash
alias name='command'
```

### Example

```bash
alias ll='ls -la'
```

Now:

```bash
ll
```

is equivalent to:

```bash
ls -la
```

---

## Common Alias Examples

### Long Directory Listing

```bash
alias ll='ls -la'
```

Usage:

```bash
ll
```

---

### Clear Terminal

```bash
alias cls='clear'
```

Usage:

```bash
cls
```

---

### Update Ubuntu Packages

```bash
alias update='sudo apt update && sudo apt upgrade'
```

Usage:

```bash
update
```

---

### Display Disk Usage

```bash
alias diskspace='df -h'
```

Usage:

```bash
diskspace
```

---

### Display Memory Usage

```bash
alias memory='free -h'
```

Usage:

```bash
memory
```

---

### Display IP Address

```bash
alias myip='ip addr'
```

Usage:

```bash
myip
```

---

## Temporary vs Permanent Aliases

### Temporary Alias

Created in the current terminal session.

Example:

```bash
alias ll='ls -la'
```

Works until:

- Terminal is closed
- System reboots
- User logs out

---

### Permanent Alias

Stored in a shell configuration file.

Common locations:

```text
~/.bashrc
~/.bash_profile
~/.zshrc
```

---

## Creating Permanent Aliases

Open Bash configuration:

```bash
nano ~/.bashrc
```

Add:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

Save and reload:

```bash
source ~/.bashrc
```

---

## Removing Aliases

### Remove Single Alias

```bash
unalias ll
```

---

### Remove All Aliases

```bash
unalias -a
```

---

## Checking an Alias

Display a specific alias:

```bash
alias ll
```

Example output:

```text
alias ll='ls -la'
```

---

## Aliases with Multiple Commands

Aliases can run several commands.

Example:

```bash
alias update='sudo apt update && sudo apt upgrade -y'
```

Usage:

```bash
update
```

---

## Aliases with Git

Many developers create Git aliases.

Example:

```bash
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'
```

Usage:

```bash
gs
ga
gp
```

---

## How Aliases Work

```text
User types:
      │
      ▼
     ll
      │
      ▼
Alias expands to:
      │
      ▼
   ls -la
      │
      ▼
Command executes
```

---

## Useful Real-World Aliases

```bash
alias ll='ls -la'
alias cls='clear'
alias h='history'
alias gs='git status'
alias gp='git push'
alias update='sudo apt update && sudo apt upgrade'
alias ports='ss -tuln'
alias diskspace='df -h'
```

---

## Limitations

Aliases are useful for short commands, but for more complex logic it is usually better to create:

- Shell scripts
- Bash functions

Example:

```bash
#!/bin/bash

echo "Hello, World!"
```

---

## Troubleshooting

### Alias Not Working

Check:

```bash
alias
```

Verify it exists.

Reload configuration:

```bash
source ~/.bashrc
```

---

### Command Overrides Alias

Use:

```bash
\command
```

Example:

```bash
\ls
```

Runs the original command instead of the alias.

---

## Revision Notes

- Aliases are command shortcuts.
- Create alias:

```bash
alias name='command'
```

- View aliases:

```bash
alias
```

- Remove alias:

```bash
unalias name
```

- Permanent aliases are typically stored in:

```text
~/.bashrc
```

- Reload Bash configuration:

```bash
source ~/.bashrc
```

---

## Quick Revision

```bash
# Create
alias ll='ls -la'

# View
alias

# Check specific alias
alias ll

# Remove
unalias ll

# Reload Bash config
source ~/.bashrc
```