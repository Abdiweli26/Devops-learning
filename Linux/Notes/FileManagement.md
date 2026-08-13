# File Management

## What is File Management?

File management involves creating, viewing, moving, copying, renaming, and deleting files and directories in Linux.

These commands are used daily by Linux administrators, DevOps engineers, and developers.

---

## touch

### What Does It Do?

Creates an empty file.

### Syntax

```bash
touch <filename>
```

### Examples

Create a file:

```bash
touch notes.txt
```

Create multiple files:

```bash
touch file1.txt file2.txt file3.txt
```

---

## mkdir

### What Does It Do?

Creates directories.

### Syntax

```bash
mkdir <directory>
```

### Examples

Create a directory:

```bash
mkdir Projects
```

Create multiple directories:

```bash
mkdir Docs Downloads Scripts
```

Create nested directories:

```bash
mkdir -p Projects/Linux/Notes
```

### Common Options

```bash
-p
```

Creates parent directories if they don't exist.

---

## cp

### What Does It Do?

Copies files and directories.

### Syntax

```bash
cp source destination
```

### Examples

Copy a file:

```bash
cp notes.txt backup.txt
```

Copy to another directory:

```bash
cp notes.txt Documents/
```

Copy a directory:

```bash
cp -r Projects Backup
```

### Common Options

```bash
-r
```

Copy directories recursively.

```bash
-v
```

Verbose output.

```bash
-i
```

Prompt before overwrite.

---

## mv

### What Does It Do?

Moves or renames files and directories.

### Syntax

```bash
mv source destination
```

### Examples

Rename a file:

```bash
mv notes.txt linux-notes.txt
```

Move a file:

```bash
mv notes.txt Documents/
```

Move a directory:

```bash
mv Projects Documents/
```

### Common Options

```bash
-i
```

Prompt before overwrite.

```bash
-v
```

Verbose output.

---

## rm

### What Does It Do?

Deletes files and directories.

### Syntax

```bash
rm <file>
```

### Examples

Delete a file:

```bash
rm notes.txt
```

Delete multiple files:

```bash
rm file1.txt file2.txt
```

Delete a directory:

```bash
rm -r Projects
```

### Common Options

```bash
-r
```

Remove recursively.

```bash
-f
```

Force removal without confirmation.

```bash
-i
```

Prompt before deletion.

### Notes

Be careful with:

```bash
rm -rf
```

It can permanently delete files and directories.

---

## rmdir

### What Does It Do?

Removes empty directories.

### Syntax

```bash
rmdir directory
```

### Example

```bash
rmdir EmptyFolder
```

### Notes

Will only work if the directory is empty.

---

## cat

### What Does It Do?

Displays file contents.

### Syntax

```bash
cat filename
```

### Examples

View a file:

```bash
cat notes.txt
```

Display multiple files:

```bash
cat file1.txt file2.txt
```

Create a file:

```bash
cat > notes.txt
```

Stop typing with:

```text
Ctrl + D
```

---

## less

### What Does It Do?

Views large files one page at a time.

### Syntax

```bash
less filename
```

### Example

```bash
less logfile.log
```

### Navigation

```text
Space → Next page
b     → Previous page
/search → Search
q     → Quit
```

---

## more

### What Does It Do?

Displays a file page by page.

### Syntax

```bash
more filename
```

### Example

```bash
more logfile.log
```

### Notes

Similar to `less` but with fewer features.

---

## head

### What Does It Do?

Displays the first lines of a file.

### Syntax

```bash
head filename
```

### Examples

First 10 lines:

```bash
head notes.txt
```

First 20 lines:

```bash
head -20 notes.txt
```

---

## tail

### What Does It Do?

Displays the last lines of a file.

### Syntax

```bash
tail filename
```

### Examples

Last 10 lines:

```bash
tail logfile.log
```

Last 20 lines:

```bash
tail -20 logfile.log
```

Follow a log in real time:

```bash
tail -f logfile.log
```

### Common Options

```bash
-f
```

Continuously monitor file updates.

---

## nano

### What Does It Do?

Terminal-based text editor.

### Syntax

```bash
nano filename
```

### Example

```bash
nano notes.txt
```

### Useful Shortcuts

```text
Ctrl + O → Save
Ctrl + X → Exit
Ctrl + K → Cut line
Ctrl + U → Paste
```

---

## vim

### What Does It Do?

Advanced terminal-based text editor.

### Syntax

```bash
vim filename
```

### Example

```bash
vim notes.txt
```

### Basic Workflow

Open file:

```bash
vim notes.txt
```

Enter insert mode:

```text
i
```

Save and quit:

```text
Esc
:wq
```

Quit without saving:

```text
Esc
:q!
```

---

## file

### What Does It Do?

Identifies file types.

### Syntax

```bash
file filename
```

### Example

```bash
file notes.txt
```

Output:

```text
notes.txt: ASCII text
```

---

## stat

### What Does It Do?

Displays detailed file information.

### Syntax

```bash
stat filename
```

### Example

```bash
stat notes.txt
```

Displays:

- File size
- Permissions
- Owner
- Creation time
- Modification time

---

## Wildcards

### *

Matches any number of characters.

Example:

```bash
ls *.txt
```

Lists all text files.

---

### ?

Matches a single character.

Example:

```bash
ls file?.txt
```

Matches:

```text
file1.txt
file2.txt
```

But not:

```text
file10.txt
```

---

## Combining Commands

Copy and rename:

```bash
cp notes.txt backup.txt
```

Move and rename:

```bash
mv notes.txt Documents/linux-notes.txt
```

View newest log entries:

```bash
tail -f logfile.log
```

---

## Revision Notes

- `touch` → Create files
- `mkdir` → Create directories
- `cp` → Copy files/directories
- `mv` → Move or rename files/directories
- `rm` → Delete files/directories
- `rmdir` → Remove empty directories
- `cat` → Display file contents
- `less` → View large files
- `head` → View beginning of a file
- `tail` → View end of a file
- `nano` → Simple text editor
- `vim` → Advanced text editor
- `file` → Identify file type
- `stat` → View file metadata

---

## Quick Revision

```bash
touch notes.txt
mkdir Projects

cp notes.txt backup.txt
mv notes.txt Documents/

rm notes.txt
rm -r Projects

cat notes.txt
less logfile.log

head logfile.log
tail logfile.log
tail -f logfile.log

nano notes.txt
vim notes.txt

file notes.txt
stat notes.txt
```