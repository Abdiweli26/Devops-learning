# Intro

Here I'll be documenting myself complete the Linux Bandit Levels 1-20 

### What is Bandit?

Bandit is a wargame designed to teach Linux command-line skills through 34 levels. You'll SSH into remote servers and solve challenges to find passwords for the next level.


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
ssh bandit2@bandit.labs.overthewire.org -p 2220
**Password**:
6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR

**Explanation**: 
I used LS to list what's under the Home Directory, I then ran Cat readme to view the password in the file

**What I learnt:**
Before attempting more advanced techniques, it's important to perform basic enumeration. Using `ls` to discover files and `cat` to read their contents is often the first step in finding valuable information on a Linux system.

#  Bandit Level 2 → Level 3


**Challenge**: 
The password for the next level is stored in a file called `--spaces in this filename--` located in the home directory

**Solution**:

`cat ./"--spaces in this filename--"`

**Username**: 
ssh bandit3@bandit.labs.overthewire.org -p 2220
**Password**:
7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME

**Explanation**: 
- Ran `ls` to view the files in the home directory.
- Identified the file named `--spaces in this filename--`.
- Used `./` to reference the file directly because its name begins with special characters.
- Wrapped the filename in quotation marks (`""`) so the spaces were treated as part of the filename rather than separate arguments.
- Read the file contents with `cat` to obtain the password.

**What I learnt:**
Learnt how to handle filenames containing both special characters and spaces by using `./` to reference the file directly and quotation marks to treat the filename as a single argument.


#  Bandit Level 3 → Level 4


**Challenge**: 
The password for the next level is stored in a hidden file in the inhere directory.

**Solution**:

`Cat ./"...Hiding-From-You"`


**Username**: 
ssh bandit4@bandit.labs.overthewire.org -p 2220
**Password**:
xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq

**Explanation**: 
- Ran `ls` to list the files and directories in the home directory.
- Noticed a directory named `inhere` and navigated into it using `cd inhere`.
- Used `ls -a` to display all files, including hidden files that begin with a dot (`.`).
- Identified the hidden file and used `cat` to read its contents.
- Retrieved the password for the next level from the hidden file.

**What I learnt:**
Learnt how to view hidden files in Linux using `ls -a` and access files that are not displayed by default, reinforcing the importance of thorough directory enumeration.

#  Bandit Level 4 → Level 5


**Challenge**: 
The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.

**Solution**:
ls


**Username**: 
ssh bandit@bandit.labs.overthewire.org -p 2220
**Password**:
E

**Explanation**: 


**What I learnt:**
