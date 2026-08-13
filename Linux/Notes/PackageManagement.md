# Package Management

## What is Package Management?

Package management is the process of installing, updating, upgrading, and removing software on a Linux system.

Linux distributions use package managers to automate software management and dependency handling.

### Common Package Managers

| Distribution | Package Manager |
|-------------|----------------|
| Ubuntu/Debian | `apt` |
| Fedora | `dnf` |
| RHEL | `dnf` |
| Arch Linux | `pacman` |

---

## What is a Package?

A package is a bundle containing:

- Application files
- Configuration files
- Dependencies
- Metadata

Example:

```text
Git Package
├── Executables
├── Documentation
├── Dependencies
└── Configuration Files
```

---

## apt

### What Does It Do?

`apt` is the package manager used by Debian-based distributions such as Ubuntu.

### Syntax

```bash
apt <command>
```

Most package management tasks require:

```bash
sudo
```

---

## apt update

### What Does It Do?

Updates the local package index.

This refreshes information about available packages.

### Syntax

```bash
sudo apt update
```

### Example

```bash
sudo apt update
```

### Notes

This does **not** install updates.

Think:

```text
apt update = Refresh package list
```

---

## apt upgrade

### What Does It Do?

Upgrades installed packages to newer versions.

### Syntax

```bash
sudo apt upgrade
```

### Example

```bash
sudo apt upgrade
```

### Notes

Typically run after:

```bash
sudo apt update
```

---

## apt install

### What Does It Do?

Installs software packages.

### Syntax

```bash
sudo apt install <package>
```

### Examples

Install Git:

```bash
sudo apt install git
```

Install Docker:

```bash
sudo apt install docker.io
```

Install multiple packages:

```bash
sudo apt install git curl wget
```

### Common Options

Install without prompts:

```bash
sudo apt install -y git
```

---

## apt remove

### What Does It Do?

Removes a package but keeps configuration files.

### Syntax

```bash
sudo apt remove <package>
```

### Example

```bash
sudo apt remove git
```

---

## apt purge

### What Does It Do?

Removes a package and its configuration files.

### Syntax

```bash
sudo apt purge <package>
```

### Example

```bash
sudo apt purge git
```

### Difference

```text
remove = Package removed, config remains

purge = Package + config removed
```

---

## apt autoremove

### What Does It Do?

Removes unused dependencies.

### Syntax

```bash
sudo apt autoremove
```

### Example

```bash
sudo apt autoremove
```

### Use Case

Run after uninstalling software to clean up unnecessary packages.

---

## apt search

### What Does It Do?

Searches available packages.

### Syntax

```bash
apt search <package>
```

### Example

```bash
apt search nginx
```

---

## apt show

### What Does It Do?

Displays detailed package information.

### Syntax

```bash
apt show <package>
```

### Example

```bash
apt show git
```

Shows:

- Version
- Description
- Dependencies
- Maintainer

---

## apt list

### What Does It Do?

Lists packages.

### Examples

Installed packages:

```bash
apt list --installed
```

Upgradable packages:

```bash
apt list --upgradable
```

---

## dpkg

### What Does It Do?

Installs and manages local `.deb` packages.

### Syntax

```bash
dpkg [option]
```

### Install a Package

```bash
sudo dpkg -i package.deb
```

### List Installed Packages

```bash
dpkg -l
```

### Check if Package is Installed

```bash
dpkg -l | grep git
```

---

## Installing Software Workflow

### Step 1

Refresh repository information.

```bash
sudo apt update
```

### Step 2

Install software.

```bash
sudo apt install git
```

### Step 3

Verify installation.

```bash
git --version
```

---

## Package Repositories

Repositories are online locations where packages are stored.

Example:

```text
Ubuntu Repository
        │
        ▼
Package Manager (apt)
        │
        ▼
Downloads Packages
```

---

## Dependency Management

Packages often require other packages.

Example:

```text
Docker
│
├── Dependency A
├── Dependency B
└── Dependency C
```

The package manager automatically installs required dependencies.

---

## Useful Commands

Update package index:

```bash
sudo apt update
```

Upgrade packages:

```bash
sudo apt upgrade
```

Install software:

```bash
sudo apt install git
```

Remove software:

```bash
sudo apt remove git
```

Search packages:

```bash
apt search docker
```

Display package information:

```bash
apt show docker.io
```

---

## Common Troubleshooting

### Package Not Found

Refresh repositories:

```bash
sudo apt update
```

Then search:

```bash
apt search package-name
```

---

### Broken Dependencies

Try:

```bash
sudo apt --fix-broken install
```

---

### Permission Denied

Use:

```bash
sudo
```

Example:

```bash
sudo apt install git
```

---

## Other Package Managers

### Fedora / RHEL

Install package:

```bash
sudo dnf install git
```

Update packages:

```bash
sudo dnf update
```

Remove package:

```bash
sudo dnf remove git
```

---

### Arch Linux

Install package:

```bash
sudo pacman -S git
```

Update system:

```bash
sudo pacman -Syu
```

Remove package:

```bash
sudo pacman -R git
```

---

## Revision Notes

- Package managers install and manage software.
- Ubuntu/Debian uses `apt`.
- `apt update` refreshes package information.
- `apt upgrade` installs available updates.
- `apt install` installs software.
- `apt remove` removes software.
- `apt purge` removes software and configuration files.
- `apt autoremove` removes unused dependencies.
- `apt search` searches for packages.
- `apt show` displays package information.
- `dpkg` manages local `.deb` files.

---

## Quick Revision

```bash
# Refresh package list
sudo apt update

# Upgrade packages
sudo apt upgrade

# Install package
sudo apt install git

# Remove package
sudo apt remove git

# Remove package + config
sudo apt purge git

# Remove unused dependencies
sudo apt autoremove

# Search package
apt search git

# View package details
apt show git

# List installed packages
apt list --installed

# Install local .deb package
sudo dpkg -i package.deb
```

### Most Common Commands

```bash
sudo apt update
sudo apt upgrade
sudo apt install <package>
sudo apt remove <package>
apt search <package>
```