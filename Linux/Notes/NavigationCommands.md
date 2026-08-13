# Navigation Commands

## What are Navigation Commands?

Navigation commands allow you to move around the Linux filesystem, locate files and directories, and view your current location.

These are some of the most frequently used Linux commands.

---

## pwd

### What Does It Do?

Displays the current working directory.

### Syntax

```bash
pwd
```

### Example

```bash
pwd
```

Output:

```text
/home/abdi/Documents
```

### Use Case

Verify your current location before running commands.

---

## ls

### What Does It Do?

Lists files and directories.

### Syntax

```bash
ls [options] [directory]
```

### Common Options

Show long format:

```bash
ls -l
```

Show hidden files:

```bash
ls -a
```

Show hidden files in long format:

```bash
ls -la
```

Show file sizes in human-readable format:

```bash
ls -lh
```

Sort by modification time:

```bash
ls -lt
```

### Examples

```bash
ls
```

```bash
ls -la
```

```bash
ls /etc
```

---

## cd

### What Does It Do?

Changes the current directory.

### Syntax

```bash
cd <directory>
```

### Examples

Move into a directory:

```bash
cd Documents
```

Move up one level:

```bash
cd ..
```

Move up two levels:

```bash
cd ../..
```

Move to home directory:

```bash
cd ~
```

Move to root directory:

```bash
cd /
```

Return to previous directory:

```bash
cd -
```

### Notes

`.` = Current directory

`..` = Parent directory

`~` = Home directory

---

## tree

### What Does It Do?

Displays a directory structure in a tree format.

### Syntax

```bash
tree
```

### Example

```bash
tree
```

Output:

```text
.
├── Documents
├── Downloads
└── notes.txt
```

### Common Options

Show directories only:

```bash
tree -d
```

Specify depth:

```bash
tree -L 2
```

### Notes

May need installation: