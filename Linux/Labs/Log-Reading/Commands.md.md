# Log Reading: Commands

Related: [[Linux-Auth-Log]] · [[SearchCommands]] · [[StreamsAndRedirection]]

---

## Look at a file

### See the first lines
```
head -n 5 file.log
```
- Shows the first 5 lines
- Do this first, so you know which column is which
- `head` on its own shows 10

### Count lines
```
wc -l file.log
```
- Counts lines, a quick way to gauge how big a log is

---

## Find things

### Search for a word
```
grep -i "fail" file.log
```
- Prints matching lines, ignoring upper/lower case
- Gotcha: "fail" also matches "failed" and "failure"

### Count matches
```
grep -ic "fail" file.log
```
- Prints how many lines match instead of the lines
- Gotcha: counts lines, not occurrences

### Show line numbers
```
grep -n "word" file.log
```

### Stop at the first match
```
grep -m1 "word" file.log
```

### Show lines around a match
```
grep -C 5 "word" file.log
```
- Shows 5 lines before and after
- Gotcha: capital `-C` needs a number straight after it, and lowercase `-c` is a different flag

### Exclude lines
```
grep -v "word" file.log
```
- Keeps only lines that don't match

---

## Pull out and count

### Print one column
```
awk '{print $5}' file.log
```
- Prints column 5 of every line
- Check the column number with `head` first

### Rank the most common values
```
awk '{print $5}' file.log | sort | uniq -c | sort -rn | head -5
```
1. `awk` pulls out the column
2. `sort` puts identical values next to each other
3. `uniq -c` collapses repeats and counts them
4. `sort -rn` sorts by that count, highest first
5. `head -5` keeps the top 5

Gotcha: `uniq` only merges neighbours, so `sort` has to come first.

---

## Words I met in the log

- `sshd`: the SSH server (remote logins)
- `ftpd`: the FTP server (file transfer)
- `pam_unix`: checks passwords
- `kernel`: the core of the OS
- `su`: switching users on the machine
- `rhost=`: the remote machine connecting
- `[12345]`: process ID, different for each connection
- `connection from`: someone knocking, before any login attempt

---

## Gotchas I hit

- 0 results for "error" didn't mean no problems, because this log says "fail"
- `head` can cut off results and hide smaller counts
- A missing field (like no `user=`) is still information
- A different search word gives a different count, so note which one you used
- A session line with no `rhost` can't tell you where it came from