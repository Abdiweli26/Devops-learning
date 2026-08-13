# Search Commands

## What are Search Commands?

Search commands allow you to locate files, directories, text, executables, and patterns within Linux.

They are commonly used for:

- Finding files
- Searching logs
- Troubleshooting
- Finding installed programs
- Filtering command output

---

## find

### What Does It Do?

Searches for files and directories.

### Syntax

```bash
find <location> <criteria>
```

### Examples

Find a file:

```bash
find . -name notes.txt
```

Find all markdown files:

```bash
find . -name "*.md"
```

Find directories only:

```bash
find . -type d
```

Find files only:

```bash
find . -type f
```

Find files larger than 100 MB:

```bash
find . -size +100M
```

Find files modified within 7 days:

```bash
find . -mtime -7
```

### Common Options

```bash
-name
```

Search by name.

```bash
-type
```

Search by file type.

```bash
-size
```

Search by file size.

```bash
-mtime
```

Search by modification time.

---

## locate

### What Does It Do?

Quickly searches for files using a database.

### Syntax

```bash
locate <filename>
```

### Examples

```bash
locate notes.txt
```

```bash
locate "*.md"
```

### Notes

The database may need updating:

```bash
sudo updatedb
```

### Difference Between find and locate

```text
find   = Searches the filesystem live
locate = Searches a database
```

`locate` is usually faster.

---

## grep

### What Does It Do?

Searches for text patterns inside files.

### Syntax

```bash
grep <pattern> <file>
```

### Examples

Search for "error":

```bash
grep "error" logfile.log
```

Search regardless of case:

```bash
grep -i "error" logfile.log
```

Display matching line numbers:

```bash
grep -n "error" logfile.log
```

Search recursively:

```bash
grep -r "error" .
```

### Common Options

```bash
-i
```

Ignore case.

```bash
-r
```

Recursive search.

```bash
-n
```

Show line numbers.

```bash
-v
```

Show non-matching lines.

---

## egrep

### What Does It Do?

Searches using extended regular expressions.

### Syntax

```bash
egrep "pattern" file
```

### Example

Search for either "error" or "warning":

```bash
egrep "error|warning" logfile.log
```

### Note

Often replaced by:

```bash
grep -E
```

Example:

```bash
grep -E "error|warning" logfile.log
```

---

## which

### What Does It Do?

Locates the executable used when a command runs.

### Syntax

```bash
which <command>
```

### Example

```bash
which git
```

Output:

```text
/usr/bin/git
```

---

## whereis

### What Does It Do?

Locates binaries, source files, and manual pages.

### Syntax

```bash
whereis <command>
```

### Example

```bash
whereis git
```

Output:

```text
git: /usr/bin/git /usr/share/man/man1/git.1.gz
```

### Difference

```text
which   = Executable only
whereis = Binary + source + man pages
```

---

## awk

### What Does It Do?

Processes and extracts data from structured text.

### Syntax

```bash
awk '{print $column}' file
```

### Examples

Display first column:

```bash
awk '{print $1}' users.txt
```

Display first and third columns:

```bash
awk '{print $1, $3}' users.txt
```

### Example File

```text
John Admin
Sarah User
```

Command:

```bash
awk '{print $1}'
```

Output:

```text
John
Sarah
```

---

## sed

### What Does It Do?

Searches and modifies text streams.

### Syntax

```bash
sed 's/old/new/' file
```

### Examples

Replace word:

```bash
sed 's/error/warning/' logfile.txt
```

Replace all occurrences:

```bash
sed 's/error/warning/g' logfile.txt
```

### Example

Input:

```text
error found
```

Output:

```text
warning found
```

---

## sort

### What Does It Do?

Sorts lines alphabetically or numerically.

### Syntax

```bash
sort file
```

### Example

```bash
sort names.txt
```

Input:

```text
Charlie
Alice
Bob
```

Output:

```text
Alice
Bob
Charlie
```

### Numerical Sort

```bash
sort -n numbers.txt
```

---

## uniq

### What Does It Do?

Removes duplicate lines.

### Syntax

```bash
uniq file
```

### Example

Input:

```text
apple
apple
orange
```

Command:

```bash
uniq file.txt
```

Output:

```text
apple
orange
```

### Common Usage

```bash
sort file.txt | uniq
```

---

## cut

### What Does It Do?

Extracts specific columns or characters.

### Syntax

```bash
cut [option]
```

### Examples

Extract first column:

```bash
cut -d ":" -f1 /etc/passwd
```

### Common Options

```bash
-d
```

Delimiter.

```bash
-f
```

Field number.

---

## wc

### What Does It Do?

Counts lines, words, and characters.

### Syntax

```bash
wc file
```

### Examples

Count lines:

```bash
wc -l notes.txt
```

Count words:

```bash
wc -w notes.txt
```

Count characters:

```bash
wc -m notes.txt
```

### Example Output

```text
25 notes.txt
```

---

## xargs

### What Does It Do?

Builds command arguments from input.

### Syntax

```bash
command | xargs another-command
```

### Example

Delete all text files found:

```bash
find . -name "*.txt" | xargs rm
```

### Common Use

```bash
find
```

+

```bash
xargs
```

---

## Pipes and Searching

### What Does It Do?

Combines commands together.

### Syntax

```bash
command | command
```

### Examples

Search running processes:

```bash
ps aux | grep nginx
```

Count matching entries:

```bash
grep "error" logfile.txt | wc -l
```

Find markdown files and sort:

```bash
find . -name "*.md" | sort
```

---

## Practical Examples

Find Docker processes:

```bash
ps aux | grep docker
```

Search for failed logins:

```bash
grep "failed" auth.log
```

Find all shell scripts:

```bash
find . -name "*.sh"
```

Display installed Git location:

```bash
which git
```

Count log file lines:

```bash
wc -l logfile.log
```

---

## Revision Notes

- `find` → Search filesystem
- `locate` → Fast file search
- `grep` → Search text
- `egrep` → Advanced pattern search
- `which` → Find executable
- `whereis` → Find binaries and man pages
- `awk` → Extract columns
- `sed` → Modify text
- `sort` → Sort output
- `uniq` → Remove duplicates
- `cut` → Extract fields
- `wc` → Count lines, words, characters
- `xargs` → Build command arguments
- `|` → Pass output between commands

---

## Quick Revision

```bash
find . -name "*.md"

locate notes.txt

grep "error" logfile.log
grep -i "error" logfile.log

which git
whereis git

awk '{print $1}' file.txt

sed 's/error/warning/g' file.txt

sort names.txt

uniq file.txt

cut -d ":" -f1 /etc/passwd

wc -l logfile.log

find . -name "*.txt" | xargs rm

ps aux | grep nginx
```

### Most Common Commands

```bash
find
grep
which
whereis
awk
sed
sort
cut
wc
```