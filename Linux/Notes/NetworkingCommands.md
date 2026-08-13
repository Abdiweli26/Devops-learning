# Networking Commands

## What are Networking Commands?

Networking commands are used to troubleshoot connectivity issues, inspect network configuration, test communication with other systems, and manage remote connections.

These commands are commonly used by System Administrators, Network Engineers, and DevOps Engineers.

---

## ip

### What Does It Do?

Displays and manages network interfaces, IP addresses, and routing information.

### Syntax

```bash
ip [option]
```

### View IP Addresses

```bash
ip addr
```

or

```bash
ip a
```

### Example Output

```text
192.168.1.100/24
```

### View Routing Table

```bash
ip route
```

---

## hostname

### What Does It Do?

Displays the current computer hostname.

### Syntax

```bash
hostname
```

### Example

```bash
hostname
```

Output:

```text
linux-server
```

### View IP Associated With Hostname

```bash
hostname -I
```

---

## ping

### What Does It Do?

Tests network connectivity between your machine and another device.

### Syntax

```bash
ping <host>
```

### Examples

Ping Google:

```bash
ping google.com
```

Ping an IP address:

```bash
ping 8.8.8.8
```

### Common Options

Send 4 packets only:

```bash
ping -c 4 google.com
```

---

## curl

### What Does It Do?

Transfers data to and from servers.

Commonly used to test APIs and websites.

### Syntax

```bash
curl <url>
```

### Examples

View webpage source:

```bash
curl https://google.com
```

View HTTP headers:

```bash
curl -I https://google.com
```

Download a file:

```bash
curl -O https://example.com/file.txt
```

---

## wget

### What Does It Do?

Downloads files from the internet.

### Syntax

```bash
wget <url>
```

### Example

```bash
wget https://example.com/file.zip
```

### Resume Download

```bash
wget -c https://example.com/file.zip
```

---

## ssh

### What Does It Do?

Creates a secure remote connection to another machine.

### Syntax

```bash
ssh user@hostname
```

### Examples

Connect using hostname:

```bash
ssh abdi@server1
```

Connect using IP:

```bash
ssh abdi@192.168.1.10
```

Specify a port:

```bash
ssh -p 2222 abdi@192.168.1.10
```

---

## scp

### What Does It Do?

Securely copies files between systems.

### Syntax

```bash
scp source destination
```

### Examples

Copy local file to remote machine:

```bash
scp notes.txt user@server:/home/user
```

Copy file from remote machine:

```bash
scp user@server:/home/user/file.txt .
```

Copy directory:

```bash
scp -r folder user@server:/home/user
```

---

## ss

### What Does It Do?

Displays network connections and listening ports.

### Syntax

```bash
ss [options]
```

### Examples

View all connections:

```bash
ss
```

View listening ports:

```bash
ss -tuln
```

### Common Options

```text
-t = TCP
-u = UDP
-l = Listening sockets
-n = Numeric output
```

---

## netstat

### What Does It Do?

Displays network statistics and active connections.

### Syntax

```bash
netstat
```

### Example

```bash
netstat -tuln
```

### Notes

Modern Linux systems typically use:

```bash
ss
```

instead.

---

## nslookup

### What Does It Do?

Queries DNS servers.

### Syntax

```bash
nslookup domain
```

### Example

```bash
nslookup google.com
```

Output:

```text
142.250.x.x
```

---

## dig

### What Does It Do?

Performs detailed DNS lookups.

### Syntax

```bash
dig domain
```

### Example

```bash
dig google.com
```

Query MX records:

```bash
dig google.com MX
```

Query DNS server:

```bash
dig @8.8.8.8 google.com
```

---

## traceroute

### What Does It Do?

Shows the path packets take to reach a destination.

### Syntax

```bash
traceroute host
```

### Example

```bash
traceroute google.com
```

### Use Case

Troubleshooting network delays and routing issues.

---

## route

### What Does It Do?

Displays the routing table.

### Example

```bash
route -n
```

### Modern Alternative

```bash
ip route
```

---

## arp

### What Does It Do?

Displays the ARP cache.

### Example

```bash
arp -a
```

### Use Case

View known devices on the local network.

---

## nc (Netcat)

### What Does It Do?

Reads and writes network connections.

Often called the "Swiss Army Knife" of networking.

### Check a Port

```bash
nc -zv google.com 443
```

### Check SSH Port

```bash
nc -zv 192.168.1.10 22
```

---

## telnet

### What Does It Do?

Tests connectivity to a specific port.

### Example

```bash
telnet google.com 80
```

### Notes

Mostly replaced by:

```bash
nc
```

and

```bash
ssh
```

---

## Useful Troubleshooting Workflow

### Check IP Address

```bash
ip addr
```

### Test Local Network

```bash
ping 192.168.1.1
```

### Test Internet Access

```bash
ping 8.8.8.8
```

### Test DNS Resolution

```bash
nslookup google.com
```

### Check Open Ports

```bash
ss -tuln
```

### Check Remote Connectivity

```bash
nc -zv server.com 443
```

---

## Revision Notes

- `ip` → Network interfaces and routes
- `hostname` → Display hostname
- `ping` → Test connectivity
- `curl` → Transfer data / test APIs
- `wget` → Download files
- `ssh` → Secure remote access
- `scp` → Secure file transfer
- `ss` → View network connections
- `netstat` → Legacy network statistics
- `nslookup` → DNS lookup
- `dig` → Advanced DNS queries
- `traceroute` → Display packet path
- `arp` → View ARP table
- `nc` → Port testing and troubleshooting

---

## Quick Revision

```bash
ip addr

hostname
hostname -I

ping google.com
ping -c 4 google.com

curl -I https://google.com

wget https://example.com/file.zip

ssh user@