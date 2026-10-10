# AWS Networking — Revision Notes

## 1. VPC

A **VPC (Virtual Private Cloud)** is a logically isolated network in AWS where I can deploy resources such as EC2 instances.

Example:

```
VPC: 10.0.0.0/16
```

The VPC CIDR defines the IP address range available inside the VPC.

---

## 2. Subnets

A **subnet** is a smaller network created from the VPC's CIDR range.

Example:

```
VPC:            10.0.0.0/16
├── Public:     10.0.0.0/24
└── Private:    10.0.1.0/26
```

A subnet exists within **one Availability Zone**.

### Public vs Private

A subnet isn't public simply because of its CIDR.

**Public subnet:** has a route to an **Internet Gateway**.

```
0.0.0.0/0 → IGW
```

**Private subnet:** does not have a direct route to an IGW. For outbound IPv4 internet access, it can route through a **NAT Gateway**.

```
0.0.0.0/0 → NAT Gateway
```

---

## 3. Route Tables

A route table determines **where network traffic should be sent**.

Example public route table:

```
10.0.0.0/16 → local
0.0.0.0/0   → Internet Gateway
```

Example private route table:

```
10.0.0.0/16 → local
0.0.0.0/0   → NAT Gateway
```

`local` handles communication **inside the VPC**, including communication between different subnets.

`0.0.0.0/0` means **all IPv4 destinations not matched by a more specific route**.

AWS chooses the **most specific matching route**.

Therefore:

```
10.0.0.24 → local
8.8.8.8   → default route
```

**Important:** being in a different subnet does **not** mean traffic needs NAT.

---

## 4. Internet Gateway (IGW)

An **Internet Gateway** connects a VPC to the internet.

Typical public path:

```
Internet
   ↕
IGW
   ↕
Public Subnet
   ↕
EC2 with Public IP
```

For direct IPv4 internet communication, an EC2 normally needs:

- Public IPv4/EIP
- Route to IGW
- Security rules allowing the traffic

---

## 5. NAT Gateway

A **NAT Gateway** allows resources in a private subnet to initiate outbound IPv4 internet connections without giving those resources public IP addresses.

```
Private EC2
    ↓
Private Route Table
0.0.0.0/0 → NAT
    ↓
NAT Gateway
    ↓
Public Route Table
0.0.0.0/0 → IGW
    ↓
Internet
```

The private EC2 keeps its **private IP**. The NAT Gateway communicates with the internet on its behalf using a public IP/EIP.

The internet cannot simply initiate a new connection through the NAT Gateway to the private EC2.

---

## 6. Security Groups

A **Security Group (SG)** is a virtual firewall associated with resources/network interfaces.

Security Groups are:

- **Stateful**
- Allow rules only
- Applied at the **resource/network-interface level**

Example:

```
Private EC2 SG

SSH | TCP 22 | Source: Bastion-SG
```

This means SSH is allowed from resources using `Bastion-SG`.

It does **not** mean every resource in the Bastion's subnet can SSH to the instance.

Because SGs are **stateful**, allowed traffic's return traffic is automatically permitted.

---

## 7. Network ACLs

A **Network ACL (NACL)** controls traffic at the **subnet level**.

NACLs are:

- **Stateless**
- Subnet-level
- Support **ALLOW and DENY**
- Process rules starting with the **lowest rule number**

Because they're stateless, inbound and outbound traffic are evaluated separately.

### SG vs NACL

```
Security Group
→ Resource/network interface
→ Stateful
→ Allow only

NACL
→ Subnet
→ Stateless
→ Allow + Deny
```

---

## 8. Bastion Host

A **Bastion Host** provides a controlled way to SSH into private instances.

```
My Mac
  ↓ SSH
Bastion Host
(Public Subnet)
  ↓ SSH using private IP
Private EC2
(Private Subnet)
```

The private EC2 doesn't need a public IP.

A secure SG setup could be:

```
Internet → Bastion: SSH from my IP only
Bastion → Private EC2: SSH from Bastion-SG only
```

---

## 9. VPC Peering

**VPC Peering** provides private communication between two VPCs.

```
VPC A ← Peering → VPC B
```

You need:

- Non-overlapping CIDRs
- Routes on both sides
- Appropriate SG/NACL rules

Peering is **non-transitive**.

If:

```
A ↔ B
B ↔ C
```

that does **not automatically mean**:

```
A ↔ C
```

---

## 10. VPC Endpoints

VPC endpoints allow private access to supported AWS services without sending traffic over the public internet.

### Gateway Endpoint

Primarily used for:

```
S3
DynamoDB
```

Works through route tables.

### Interface Endpoint

Creates private network interfaces/IPs in your VPC and uses **AWS PrivateLink**.

Used for many AWS services.

---

## 11. IPv6

IPv4 default route:

```
0.0.0.0/0
```

IPv6 default route:

```
::/0
```

IPv6 generally doesn't require NAT because IPv6 addresses can be globally routable.

For private-style **outbound-only IPv6**, AWS provides an **Egress-Only Internet Gateway**.

---

## 12. Troubleshooting Network Problems

Think through the packet path instead of randomly changing settings:

```
Source
  ↓
Route
  ↓
Security Group
  ↓
NACL
  ↓
Destination
  ↓
Port
  ↓
Application
```

Ask:

**Can traffic reach the destination?** → Routing

**Is traffic permitted?** → SG / NACL

**Is something listening on the port?** → Service

**Is the application actually responding?** → Application

Useful EC2 commands:

```
sudo systemctl status httpd
```

Checks whether Apache is running.

```
curl localhost
```

Checks whether the web server responds locally.

A **timeout is only a symptom**. It doesn't automatically prove that the Security Group, NAT, or routing is the problem.

---

## 13. Key Architecture to Remember

```
                    Internet
                       │
                       │
                      IGW
                       │
                Public Subnet
                ┌──────┴──────┐
             Bastion         NAT
                │              ↑
                │              │
                │        Private route
                │        0.0.0.0/0
                │              │
                └──────→ Private EC2
```

### Quick Memory Rules

**IGW** → VPC ↔ Internet  
**NAT** → Private resources → Internet  
**Route table** → Where does traffic go?  
**SG** → Is resource traffic allowed?  
**NACL** → Is subnet traffic allowed?  
**Bastion** → Controlled SSH path to private resources  
**VPC Endpoint** → Private access to AWS services  
**Peering** → Private connection between VPCs  
**`local`** → Traffic within the VPC  
**`0.0.0.0/0`** → Default IPv4 route

These are the networking notes I'd actually revise before an interview or before moving into your ALB assignment.