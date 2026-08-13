# Process Management

## What is a Process?

A process is a running instance of a program.

When you execute a command, Linux creates a process.

Examples:

```text
bash
nginx
docker
git
python
```

Every process has a unique identifier called a PID (Process ID).

---

## Process Lifecycle

```text
Command
   │
   ▼
 Process Created
   │
   ▼
 Running
   │
   ▼
 Completed or Terminated
```

Example:

```bash
python app.py
```

Linux creates a process and assigns it a PID.

---

## PID (Process ID)

A PID uniquely identifies a process.

Example:

```text
PID 1234 = python
PID 5678 = nginx
```

---

## ps

### What Does It Do?

Displays running processes.

### Syntax

```bash
ps
```

### Example

```bash
ps
```

Output:

```text
PID TTY          TIME CMD
1234 pts/0    00:00:00 bash
5678 pts/0    00:00:00 ps
```

---

## ps aux

### What Does It Do?

Displays detailed information about all running processes.

### Syntax

```bash
ps aux
```

### Example

```bash
ps aux
```

### Useful Fields

```text
USER = Process owner
PID  = Process ID
%CPU = CPU usage
%MEM = Memory usage
COMMAND = Process name
```

---

## pgrep

### What Does It Do?

Searches for processes by name.

### Syntax

```bash
pgrep <process>
```

### Example

```bash
pgrep nginx
```

Output:

```text
1234
```

Find all bash processes:

```bash
pgrep bash
```

---

## top

### What Does It Do?

Displays real-time system and process information.

### Syntax

```bash
top
```

### Example

```bash
top
```

Displays:

- Running processes
- CPU usage
- Memory usage
- System load

### Exit

```text
q
```

---

## htop

### What Does It Do?

Interactive version of `top`.

### Syntax

```bash
htop
```

### Example

```bash
htop
```

### Features

- Easier to read
- Mouse support
- Better process management

### Install

```bash
sudo apt install htop
```

---

## kill

### What Does It Do?

Terminates a process using its PID.

### Syntax

```bash
kill <PID>
```

### Example

```bash
kill 1234
```

Terminates process:

```text
PID 1234
```

---

## kill -9

### What Does It Do?

Forcefully terminates a process.

### Syntax

```bash
kill -9 <PID>
```

### Example

```bash
kill -9 1234
```

### Notes

Use only when a process won't stop normally.

---

## pkill

### What Does It Do?

Terminates processes by name.

### Syntax

```bash
pkill <process>