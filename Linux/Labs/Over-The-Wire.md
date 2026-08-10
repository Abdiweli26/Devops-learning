# Intro

Here I'll be documenting myself complete the Linux Bandit Levels 1-20 

### What is Bandit?

Bandit is a wargame designed to teach Linux command-line skills through 34 levels. You'll SSH into remote servers and solve challenges to find passwords for the next level.

```
## Bandit Level 0
```

bash

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
# Password: bandit0
```

Once logged in, read the README file to find the password for Level 1:

bash

```bash
cat README
# Use this password to SSH as bandit1
```


#  Bandit Level 0 


**Challenge**: 
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

**Solution**:
SSH bandit0@bandit.labs.overthewire.org -p 2220

**Password**:
Bandit0


#  Bandit Level 0 → Level 1


**Challenge**: 
The password for the next level is stored in a file called **-** located in the home directory
**Solution**:
`ls 
Cat readme`

**Username**: 
ssh bandit1@bandit.labs.overthewire.org -p 2220
**Password**:
6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR

**Explanation**: 
I used LS to list what's under the Home Directory, I then ran Cat readme to view the password in the file

**What I learnt:**
Before attempting more advanced techniques, it's important to perform basic enumeration. Using `ls` to discover files and `cat` to read their contents is often the first step in finding valuable information on a Linux system.

#  Bandit Level 1 → Level 2


**Challenge**: 
The password for the next level is stored in a file called **-** located in the home directory

**Solution**:
`ls` 
`Cat ./-`

**Username**: 
ssh bandit1@bandit.labs.overthewire.org -p 2220

**Password**:
PK8fYLZg2hnHSz83plBL1iEPKdD3QToB

**Explanation**: 
```
I ran ls to list the files, The file "-" showed. To view files with special characters I ran ./ before the file name.
```

**What I learnt:**

Learnt how to access files with special names by prefixing them with `./`, allowing me to read the contents of the file named - after locating it with `ls`.

# Bandit Level 2  → Level 3

**Challenge**: 
The password for the next level is stored in a file called `--spaces in this filename--` located in the home directory

**Solution**:
```
cat ./"--spaces in this filename--"
.```

**Username**: 
ssh bandit2@bandit.labs.overthewire.org -p 2220
**Password**:
7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME

**Explanation**: 
ls to view the list of files in the home directory
You'll then see --spaces in this filename--
To open this you'll need a combo of ./ and "", becuase to view files with special characters we use ./ but to view a file name with spaces you can either use \ to fill the space or put the file in quotation.
This file has both hence why I used./ & ""

**What I learnt:**
Learnt how to handle filenames containing special characters and spaces by using ./ to reference the file directly and quotation marks ("") to treat the filename as a single argument, allowing me to access and read the file successfully.



