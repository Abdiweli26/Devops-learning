## Security Groups

A **Security Group** acts as a virtual firewall that controls allowed inbound and outbound network traffic for AWS resources such as EC2 instances.

- **Inbound rules** → traffic allowed into the resource
- **Outbound rules** → traffic allowed out of the resource

### Inbound vs Outbound

**Inbound:** Controls traffic entering the resource.
Example: Allowing SSH (22) from your IP to an EC2 instance.

**Outbound:** Controls traffic leaving the resource.
Example: Allowing an EC2 instance to connect to the internet.

### Common Ports

- SSH → 22
- HTTP → 80
- HTTPS → 443
- RDP → 3389

### Restricting SSH

For better security, restrict SSH (port 22) to trusted IP addresses rather than `0.0.0.0/0`.

`0.0.0.0/0` = Any IPv4 address
`Your-IP/32` = Only that specific IPv4 address


### Public vs Private IPv4

**Public IPv4**
- Routable over the internet
- Globally unique

**Private IPv4**
- Used within private networks
- Not directly routable over the public internet
- The same private address ranges can be reused by different private networks
### Private IP & Security Groups

A private IPv4 address is not directly routable over the public internet.

A Security Group controls whether traffic is allowed, but it does not make a private IP publicly reachable.

Network path/routing and Security Group permissions are separate concepts.
### IPv4 vs IPv6

**IPv4**
- 32-bit addresses
- Around 4.3 billion possible addresses
- Example: `192.168.1.10`

**IPv6**
- 128-bit addresses
- Vastly larger address space
- Introduced largely because of IPv4 address exhaustion
- Example: `2001:db8::1`
### Elastic IP

An **Elastic IP (EIP)** is a static public IPv4 address in AWS.

It can be associated with resources such as EC2 instances when a consistent public IP address is required.

Example:
Normal Public IPv4 → May change
Elastic IP → Static



Internet
   │
   │ Public IP
   ▼
┌─────────────────────┐
│ Security Group      │ ← Is the traffic allowed?
├─────────────────────┤
│ EC2 Instance        │
│ Private IP          │
└─────────────────────┘

Routing → Can the traffic reach the destination?
Security Group → Is the traffic allowed?
Port → Which service/application is the traffic for?