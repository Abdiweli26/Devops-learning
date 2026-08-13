# Streams and Redirection

## Quick Revision

| Command/Symbol | Purpose |
|---------------|---------|
| stdin (0) | Standard Input |
| stdout (1) | Standard Output |
| stderr (2) | Standard Error |
| `>` | Redirect output (overwrite) |
| `>>` | Redirect output (append) |
| `<` | Redirect input |
| `2>` | Redirect errors |
| `2>>` | Append errors |
| `2>&1` | Redirect errors to stdout |
| `|` | Pipe output to another command |
| `tee` | Display and save output |
| `/dev/null` | Discard output |

### Most Common Examples

```bash
ls > output.txt

echo "Hello" >> notes.txt

cat < notes.txt

ls missing.txt 2> errors.txt

ls > output.txt 2>&1

ls -l | grep notes

command > /dev/null 2>&1

ls | tee output.txt
```

---

# What are Streams?

Linux programs communicate using streams.

There are three standard streams:

| Stream | Number | Purpose |
|----------|----------|----------|
| stdin | 0 | Receives input |
| stdout | 1 | Normal output |
| stderr | 2 | Error messages |

---

## Stream Diagram

```text
Keyboard/File
      │
      ▼
 stdin (0)
      │
      ▼
   Program
      │
      ├── stdout (1)
      │
      └── stderr (2)
```

---

# Standard Input (stdin)

## What Does It Do?

Provides input to a program.

### Example

```bash
cat
```

Type:

```text
Hello Linux
```

Output:

```text
Hello Linux
```

The keyboard is acting as stdin.

---

## Redirect Input from a File

### Syntax

```bash
command < file
```

### Example

```bash
cat < notes.txt
```

Instead of typing manually, input comes from the file.

---

# Standard Output (stdout)

## What Does It Do?

Displays normal program output.

### Example

```bash
echo "Hello World"
```

Output:

```text
Hello World
```

The output is sent to stdout.

---

# Standard Error (stderr)

## What Does It Do?

Displays error messages.

### Example

```bash
ls file_that_does_not_exist
```

Output:

```text
ls: cannot access 'file_that_does_not_exist'
```

The message is sent to stderr.

---

# Output Redirection (>)

## What Does It Do?

Redirects output to a file.

### Syntax

```bash
command > file
```

### Example

```bash
ls > files.txt
```

Output is written to:

```text
files.txt
```

### Important

If the file already exists:

```text
Contents are overwritten
```

---

# Append Output (>>)

## What Does It Do?

Appends output to a file.

### Syntax

```bash
command >> file
```

### Example

```bash
echo "New Line" >> notes.txt
```

### Difference

```text
>   = overwrite

>>  = append
```

---

# Input Redirection (<)

## What Does It Do?

Uses a file as program input.

### Syntax

```bash
command < file
```

### Example

```bash
cat < notes.txt
```

Program reads from the file.

---

# Error Redirection (2>)

## What Does It Do?

Redirects errors to a file.

### Syntax

```bash
command 2> file
```

### Example

```bash
ls missing.txt 2> errors.txt
```

Errors go to:

```text
errors.txt
```

---

# Append Errors (2>>)

## What Does It Do?

Appends errors to a file.

### Example

```bash
ls missing.txt 2>> errors.txt
```

---

# Redirect Stdout and Stderr Separately

### Example

```bash
command > output.txt 2> errors.txt
```

Results:

```text
output.txt -> stdout
errors.txt -> stderr
```

---

# Redirect Everything to One File

### Example

```bash
command > output.txt 2>&1
```

Meaning:

```text
stdout -> output.txt
stderr -> stdout
```

Result:

```text
Everything goes to output.txt
```

---

# /dev/null

## What Does It Do?

Discards anything written to it.

Often called:

```text
The Linux black hole
```

---

## Discard Output

```bash
command > /dev/null
```

Example:

```bash
ls > /dev/null
```

No output appears.

---

## Discard Errors

```bash
command 2> /dev/null
```

Example:

```bash
ls missing.txt 2> /dev/null
```

No error message appears.

---

## Discard Everything

```bash
command > /dev/null 2>&1
```

Example:

```bash
ls missing.txt > /dev/null 2>&1
```

Output and errors are hidden.

---

# Pipes (|)

## What Does It Do?

Passes output from one command into another command.

### Syntax

```bash
command | command
```

---

## Example

```bash
ls -l | grep notes
```

### How It Works

```text
ls -l
  │
  ▼
stdout
  │
  ▼
grep notes
```

Only matching lines are displayed.

---

## More Examples

Count files:

```bash
ls | wc -l
```

Search running processes:

```bash
ps aux | grep nginx
```

Display specific information:

```bash
cat users.txt | grep admin
```

---

# tee

## What Does It Do?

Displays output and saves it to a file at the same time.

### Syntax

```bash
command | tee file
```

### Example

```bash
ls | tee files.txt
```

Results:

```text
Output displayed on screen
Output saved to files.txt
```

---

## Append with tee

```bash
command | tee -a file
```

Example:

```bash
echo "Hello" | tee -a notes.txt
```

---

# Combining Streams and Pipes

### Example

```bash
ps aux | grep nginx | tee nginx.txt
```

Process:

```text
ps aux
   │
   ▼
grep nginx
   │
   ▼
tee nginx.txt
```

Result:

```text
Display nginx processes

AND

Save results to nginx.txt
```

---

# Practical Examples

Save directory listing:

```bash
ls -la > files.txt
```

Append text:

```bash
echo "Linux" >> notes.txt
```

Hide errors:

```bash
ls missing.txt 2> /dev/null
```

Save output and errors:

```bash
command > output.txt 2>&1
```

Search logs:

```bash
cat logfile.log | grep error
```

Count users:

```bash
cat users.txt | wc -l
```

Display and save:

```bash
ls | tee files.txt
```

---

# Common Interview Questions

### Difference Between `>` and `>>`

```text
>   Overwrites file

>>  Appends to file
```

---

### Difference Between stdout and stderr

```text
stdout = Normal output

stderr = 