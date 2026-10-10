# Linux Auth Log (Loghub sample)

**Dataset:** Linux_2k.log from loghub (link in README)
**Goal:** practise finding errors and patterns using only the command line

## Log format
(what each column is, based on `head -5`)

## Questions and answers

### 1. How many lines are there?
**Command:** `wc -l Linux_2k.log`
**Result:** 1999
**What I learned:** A quick way to gauge how big a Log is before you read it.

### 2. How many lines mention "fail"?
**Command:** grep -ic "failure" Linux_2k.log
**Result:** 538

### 3. Which services log the most?
**Command:** Awk '{print $5}' Linux_2k.log |  sort | uniq c | sort -rn | head |
**Result:**  7

### 4. What happened around the first authentication failure?
**Command:** 
**Result:** 
**My reading of it:** (what do you think was going on?)

## Mistakes / things that surprised me
-