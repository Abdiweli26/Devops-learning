# Environment Variables

## What are Environment Variables?

Environment variables are named values stored by the operating system that can be accessed by the shell and applications.

They are commonly used to store:

- User information
- File paths
- Application settings
- System configuration
- Authentication tokens

---

## Why Use Environment Variables?

Benefits:

- Store configuration separately from applications
- Avoid hardcoding values
- Easily share settings between programs
- Customize shell behaviour

Example:

```bash
echo $HOME
```

Output:

```text
/home/abdi
```

---

## Viewing Environment Variables

Display all environment variables:

```bash
env
```

or

```bash
printenv
```

---

## Viewing a Specific Variable

### Syntax

```bash
echo $VARIABLE_NAME
```

### Example

```bash
echo $HOME
```

Output:

```text
/home/abdi
```

---

## Common Environment Variables

### HOME

Current user's home directory.

```bash
echo $HOME
```

Example:

```text
/home/abdi
```

---

### USER

Current username.

```bash
echo $USER
```

Example:

```text
abdi
```

---

### PWD

Current working directory.

```bash
echo $PWD
```

Example:

```text
/home/abdi/Documents
```

---

### SHELL

Current shell.

```bash
echo $SHELL
```

Example:

```text
/bin/bash
```

---

### PATH

Directories Linux searches when you run a command.

```bash
echo $PATH
```

Example:

```text
/usr/local/bin:/usr/bin:/bin
```

---

## Understanding PATH

When you run:

```bash
git
```

Linux searches through each directory listed in `PATH` until it finds:

```text
/usr/bin/git
```

### Example

```bash
which git
```

Output:

```text
/usr/bin/git
```

### PATH Diagram

```text
User runs:
      git
       │
       ▼

Checks PATH:
       │
       ▼

/usr/local/bin
/usr/bin
/bin
       │
       ▼

Finds:
/usr/bin/git
       │
       ▼

Runs command
```

---

## Creating Variables

### Syntax

```bash
VARIABLE_NAME=value
```

### Example

```bash
MY_NAME=Abdi
```

Display it:

```bash
echo $MY_NAME
```

Output:

```text
Abdi
```

---

## Temporary Variables

Variables created in the terminal are temporary.

Example:

```bash
MY_NAME=Abdi
```

The variable exists only for the current shell session.

If you close the terminal, it disappears.

---

## Exporting Variables

Exporting makes a variable available to child processes.

### Syntax

```bash
export VARIABLE=value
```

### Example

```bash
export MY_NAME=Abdi
```

Verify:

```bash
echo $MY_NAME
```

Output:

```text
Abdi
```

---

## Local Variables vs Exported Variables

### Local Variable

```bash
MY_NAME=Abdi
```

Only available in the current shell.

---

### Exported Variable

```bash
export MY_NAME=Abdi
```

Available in the current shell and child processes.

---

## Making Variables Permanent

Open:

```bash
nano ~/.bashrc
```

Add:

```bash
export MY_NAME=Abdi
```

Save and reload:

```bash
source ~/.bashrc
```

Verify:

```bash
echo $MY_NAME
```

---

## Removing Variables

### Remove Variable

```bash
unset MY_NAME
```

Check:

```bash
echo $MY_NAME
```

No output means the variable has been removed.

---

## Viewing Variables with printenv

Display all variables:

```bash
printenv
```

Display one variable:

```bash
printenv HOME
```

---

## Practical Examples

### Store Environment

```bash
export ENVIRONMENT=development
```

Display:

```bash
echo $ENVIRONMENT
```

---

### Store Application Port

```bash
export PORT=8080
```

---

### Store API Endpoint

```bash
export API_URL=https://api.example.com
```

---

## Environment Variables in Scripts

Example:

```bash
#!/bin/bash

echo "Hello $USER"
```

Output:

```text
Hello abdi
```

---

## Troubleshooting

### Variable Not Showing

Check:

```bash
echo $VARIABLE
```

Verify it exists:

```bash
env
```

---

### Changes Not Applied

Reload Bash configuration:

```bash
source ~/.bashrc
```

---

## Security Note

Avoid storing sensitive information directly in scripts.

Instead use environment variables:

```bash
export API_KEY=xxxxx
```

This is commonly used in:

- Docker
- Kubernetes
- CI/CD pipelines
- Cloud applications

---

## How Environment Variables Work

```text
Operating System
       │
       ▼
Environment Variable
       │
       ▼
Shell / Application
       │
       ▼
Uses stored value
```

Example:

```text
HOME=/home/abdi
```

Application reads:

```bash
$HOME
```

Result:

```text
/home/abdi
```

---

## Revision Notes

- Environment variables store values used by the shell and applications.
- Use `$` to access a variable.
- View all variables:

```bash
env
```

- Create a variable:

```bash
MY_NAME=Abdi
```

- Export a variable:

```bash
export MY_NAME=Abdi
```

- Remove a variable:

```bash
unset MY_NAME
```

- Reload Bash config:

```bash
source ~/.bashrc
```

---

## Quick Revision

```bash
# Show all variables
env

# Show specific variable
echo $HOME

# Create variable
MY_NAME=Abdi

# Export variable
export MY_NAME=Abdi

# Remove variable
unset MY_NAME

# Display PATH
echo $PATH

# Reload Bash config
source ~/.bashrc
```

### Most Important Variables

```text
HOME   → User home directory
USER   → Current user
PWD    → Current directory
SHELL  → Current shell
PATH   → Command search locations
```