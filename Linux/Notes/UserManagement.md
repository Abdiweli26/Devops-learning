# User Management

## Quick Revision

| Command | Purpose |
|----------|----------|
| whoami | Display current user |
| id | Display user and group information |
| groups | Show user groups |
| users | Show logged-in users |
| who | Display logged-in users |
| useradd | Create a user |
| usermod | Modify a user |
| userdel | Delete a user |
| passwd | Change password |
| groupadd | Create a group |
| groupdel | Delete a group |
| chage | Manage password expiry |
| su | Switch user |
| sudo | Run commands as another user |

### Most Common Commands

```bash
whoami

id

groups

sudo command

su username

passwd

useradd username

userdel username
```

---

# What is User Management?

Linux is a multi-user operating system.

Each user:

- Has a username
- Has a unique User ID (UID)
- Belongs to one or more groups
- Has permissions that control access to files and resources

---

## User and Group Structure

```text
Linux System
     │
     ├── Users
     │
     └── Groups
```

Example:

```text
abdi
 ├── UID: 1001
 └── Group: developers

nginx
 ├── UID: 998
 └── Group: nginx
```

---

# whoami

## What Does It Do?

Displays the currently logged-in user.

### Syntax

```bash
whoami
```

### Example

```bash
whoami
```

Output:

```text
abdi
```

---

# id

## What Does It Do?

Displays detailed user information.

### Syntax

```bash
id
```

### Example

```bash
id
```

Output:

```text
uid=1000(abdi)
gid=1000(abdi)
groups=1000(abdi),27(sudo)
```

### Useful Option

View another user:

```bash
id username
```

---

# groups

## What Does It Do?

Displays groups the user belongs to.

### Syntax

```bash
groups
```

### Example

```bash
groups
```

Output:

```text
abdi sudo docker
```

---

# users

## What Does It Do?

Displays currently logged-in users.

### Syntax

```bash
users
```

### Example

```bash
users
```

Output:

```text
abdi admin
```

---

# who

## What Does It Do?

Displays information about users currently logged into the system.

### Syntax

```bash
who
```

### Example

```bash
who
```

Output:

```text
abdi pts/0 2025-08-05 09:00
```

---

# passwd

## What Does It Do?

Changes a user's password.

### Syntax

```bash
passwd
```

### Example

Change your password:

```bash
passwd
```

Change another user's password:

```bash
sudo passwd username
```

---

# useradd

## What Does It Do?

Creates a new user.

### Syntax

```bash
sudo useradd username
```

### Example

```bash
sudo useradd john
```

### Create Home Directory

```bash
sudo useradd -m john
```

or

```bash
sudo adduser john
```

### Common Options

```bash
-m
```

Create home directory.

```bash
-s
```

Specify shell.

Example:

```bash
sudo useradd -m -s /bin/bash john
```

---

# adduser

## What Does It Do?

Friendly version of `useradd`.

### Example

```bash
sudo adduser john
```

Prompts for:

- Password
- Full name
- Additional information

---

# usermod

## What Does It Do?

Modifies an existing user.

### Syntax

```bash
sudo usermod [options] username
```

### Add User to Group

```bash
sudo usermod -aG docker john
```

### Change Login Name

```bash
sudo usermod -l johnsmith john
```

### Common Options

```bash
-aG
```

Append user to group.

```bash
-l
```

Change username.

---

# userdel

## What Does It Do?

Deletes a user.

### Syntax

```bash
sudo userdel username
```

### Example

```bash
sudo userdel john
```

### Delete User and Home Directory

```bash
sudo userdel -r john
```

---

# Group Management

## What are Groups?

Groups allow multiple users to share permissions.

Example:

```text
developers
 ├── John
 ├── Sarah
 └── Abdi
```

---

# groupadd

## What Does It Do?

Creates a new group.

### Syntax

```bash
sudo groupadd groupname
```

### Example

```bash
sudo groupadd developers
```

---

# groupdel

## What Does It Do?

Deletes a group.

### Syntax

```bash
sudo groupdel groupname
```

### Example

```bash
sudo groupdel developers
```

---

# gpasswd

## What Does It Do?

Manages group memberships.

### Add User to Group

```bash
sudo gpasswd -a john developers
```

### Remove User from Group

```bash
sudo gpasswd -d john developers
```

---

# su

## What Does It Do?

Switches to another user account.

### Syntax

```bash
su username
```

### Example

```bash
su john
```

### Switch to Root

```bash
su -
```

---

# sudo

## What Does It Do?

Runs commands with elevated privileges.

### Syntax

```bash
sudo command
```

### Examples

```bash
sudo apt update
```

```bash
sudo useradd john
```

### Notes

Users require membership of the sudo group.

---

# Root User

## What is Root?

The root user is the administrator account.

Characteristics:

- Full system access
- Can modify any file
- Can manage users
- Can install software

Display root account:

```bash
id root
```

---

# chage

## What Does It Do?

Manages password expiration.

### Syntax

```bash
sudo chage username
```

### Example

```bash
sudo chage john
```

### View Expiry Information

```bash
sudo chage -l john
```

---

# Important User Files

## /etc/passwd

Stores user account information.

View:

```bash
cat /etc/passwd
```

Example:

```text
john:x:1001:1001:/home/john:/bin/bash
```

---

## /etc/shadow

Stores encrypted passwords.

View:

```bash
sudo cat /etc/shadow
```

### Notes

Only root can access this file.

---

## /etc/group

Stores group information.

View:

```bash
cat /etc/group
```

---

# User Management Workflow

Create user:

```bash
sudo adduser john
```

Add user to sudo group:

```bash
sudo usermod -aG sudo john
```

Verify group membership:

```bash
groups john
```

Switch user:

```bash
su john
```

Delete user:

```bash
sudo userdel -r john
```

---

# Practical Examples

Display current user:

```bash
whoami
```

View user details:

```bash
id
```

Display groups:

```bash
groups
```

Create a user:

```bash
sudo adduser devops
```

Add user to Docker group:

```bash
sudo usermod -aG docker devops
```

Change password:

```bash
passwd
```

Delete user:

```bash
sudo userdel -r devops
```

---

# Common Interview Questions

### What is the difference between `su` and `sudo`?

```text
su   = Switch user account

sudo = Run a command as another user (usually root)
```

---

### What is the root user?

```text
Administrator account with unrestricted access.
```

---

### What file stores user information?

```text
/etc/passwd
```

---

### What file stores encrypted passwords?

```text
/etc/shadow
```

---

# Revision Notes

- Linux is a multi-user operating system.
- Every user has a UID.
- Users belong to groups.
- Root is the administrator account.
- `whoami` → Current user.
- `id` → User and group information.
- `groups` → Display group membership.
- `useradd` / `adduser` → Create users.
- `usermod` → Modify users.
- `userdel` → Delete users.
- `groupadd` → Create groups.
- `groupdel` → Delete groups.
- `passwd` → Change passwords.
- `su` → Switch user.
- `sudo` → Execute commands with elevated privileges.

---

## Quick Commands

```bash
whoami

id

groups

who

passwd

sudo adduser john

sudo usermod -aG docker john

sudo groupadd developers

sudo userdel -r john

sudo groupdel developers

su john

sudo apt update

cat /etc/passwd

cat /etc/group
```