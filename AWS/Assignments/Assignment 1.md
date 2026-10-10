

# AWS VPC & Networking Project

Contents

1. Project Overview
2. Architecture Overview
3. VPC Configuration
4. Subnet Configuration
   4.1 Public Subnet
   4.2 Private Subnet
5. Internet Gateway
6. Route Tables
   6.1 Public Route Table
   6.2 Private Route Table
7. NAT Gateway & Elastic IP
8. EC2 Instances
   8.1 Public EC2 Instance
   8.2 Private EC2 Instance
9. Security Groups
10. Bastion Host
11. CloudWatch Detailed Monitoring
12. Connectivity Testing
13. Troubleshooting & Issues Resolved
14. Key Learnings
15. Conclusion


## 1. Project Overview

The aim of this assignment was to build a custom AWS network containing both public and private resources.

I created a custom VPC and divided the network into a public subnet and a private subnet. I then configured route tables, an Internet Gateway and a NAT Gateway to control how resources communicate internally and with the internet.

EC2 instances were deployed across the two subnets, with security groups used to control access. I also implemented a Bastion Host to provide SSH access to the private EC2 instance without exposing the private instance directly to the internet.

As additional tasks, I configured CloudWatch Detailed Monitoring and tested outbound internet connectivity from the private EC2 instance.

## 2. Architecture Overview

The environment was designed around three main traffic flows:

```
Public internet access:
Public EC2 -> Internet Gateway -> Internet

Private outbound access:
Private EC2 -> NAT Gateway -> Internet Gateway -> Internet

Administrative access:
My Mac -> Bastion Host -> Private EC2
```

The main network ranges used were:

```
VPC:            10.0.0.0/16
Public subnet:  10.0.0.0/24
Private subnet: 10.0.1.0/26
```

This design keeps the private EC2 instance off the public internet while still allowing controlled administrative access and outbound internet connectivity.

## 3. VPC Configuration

I created a custom VPC called `Custom-VPC` using the IPv4 CIDR block:

```
10.0.0.0/16
```

The `/16` range provides the overall private address space from which smaller subnet ranges can be created. DNS resolution was also enabled on the VPC.

![[Pasted image 20260930103936.png]]
_Figure 1 – Custom VPC configured with the `10.0.0.0/16` CIDR._


## 4. Subnet Configuration

I divided the VPC into separate public and private subnets so that resources with different connectivity requirements could be isolated from each other.

### 4.1 Public Subnet

I created `Public-Subnet1` using:

```
10.0.0.0/24
```

The subnet was created in `eu-west-2b`. A `/24` provides 256 total IPv4 addresses in the CIDR range.

The public subnet is associated with a route table that contains a default route to the Internet Gateway. Resources that require public connectivity, including the Bastion Host and NAT Gateway, were placed in this subnet.

![[Pasted image 20260930103959.png]]
_Figure 2 – Public subnet and associated public route table._


### 4.2 Private Subnet

I created `Private-subnet1` using:

```
10.0.1.0/26
```

The subnet was also created in `eu-west-2b`. A `/26` provides 64 total IPv4 addresses.

The private EC2 instance was deployed into this subnet without a public IPv4 address. Internet-bound traffic from this subnet is routed through the NAT Gateway instead of directly through the Internet Gateway.

![[Pasted image 20260930104014.png]]
_Figure 3 – Private subnet and associated private route table._

## 5. Internet Gateway

I created an Internet Gateway and attached it to `Custom-VPC`.

The Internet Gateway provides a path between the VPC and the public internet for resources that have the required public addressing, routing and security configuration.

Attaching an Internet Gateway by itself does not make a subnet public. The subnet must also be associated with a route table containing a route to the Internet Gateway.

![[Pasted image 20260930104027.png]]
_Figure 4 – Internet Gateway attached to `Custom-VPC`._

---

## 6. Route Tables

I configured separate route tables for the public and private subnets so that each subnet handled internet-bound traffic differently.

### 6.1 Public Route Table

The public route table contains:

```
Destination     Target
10.0.0.0/16     local
0.0.0.0/0       Internet Gateway
```

The `10.0.0.0/16 -> local` route allows communication between resources inside the VPC.

The `0.0.0.0/0 -> Internet Gateway` route provides the default path for IPv4 traffic destined outside the VPC.

![[Pasted image 20260930104041.png]]
_Figure 5 – Public route table with the local VPC route and default Internet Gateway route._

### 6.2 Private Route Table

The private route table contains:

```
Destination     Target
10.0.0.0/16     local
0.0.0.0/0       NAT Gateway
```

The local route handles communication inside the VPC, while the default route sends external IPv4 traffic to the NAT Gateway.

This allows the private EC2 instance to initiate outbound internet connections without receiving a public IPv4 address.

![[Pasted image 20260930104050.png]]
_Figure 6 – Private route table using the NAT Gateway as its default route._

---

## 7. NAT Gateway & Elastic IP

I deployed a public NAT Gateway into `Public-Subnet1`.

The NAT Gateway was assigned a public IPv4 address using an Elastic IP so that it could communicate with the internet on behalf of resources in the private subnet.

The private EC2 instance itself remains private and does not require a public IPv4 address.

```
Private EC2
    |
    v
Private Route Table
0.0.0.0/0 -> NAT Gateway
    |
    v
NAT Gateway
(Public Subnet + Elastic IP)
    |
    v
Internet Gateway
    |
    v
Internet
```

![[Pasted image 20260930104101.png]]
_Figure 7 – Public NAT Gateway deployed in `Public-Subnet1` with public IPv4 connectivity._

---

## 8. EC2 Instances

I deployed EC2 instances into both the public and private parts of the network.

### 8.1 Public EC2 Instance

The Public EC2 instance was deployed into `Public-Subnet1` and was assigned a public IPv4 address.

This allows it to use the public subnet's route through the Internet Gateway when the relevant security group rules permit the traffic.

CloudWatch Detailed Monitoring was also enabled on this instance.

![[Pasted image 20260930104116.png]]
_Figure 8 – Public EC2 instance deployed in `Public-Subnet1`._

### 8.2 Private EC2 Instance

The Private EC2 instance was deployed into `Private-subnet1`.

Its private IPv4 address was:

```
10.0.1.61
```

The instance was not assigned a public IPv4 address. Administrative access therefore had to travel through the Bastion Host instead of connecting directly from the internet.

Outbound internet connectivity was provided separately through the NAT Gateway.

![[Pasted image 20260930104129.png]]
_Figure 9 – Private EC2 instance with no public IPv4 address._

---

## 9. Security Groups

I used separate security groups to control access between the resources.

The Bastion security group allows SSH on TCP port `22` from my own public IP using a `/32` source.

The private EC2 security group allows SSH from the Bastion security group. This provides a controlled path to the private instance without exposing SSH directly to the internet.

```
My device
   |
   | SSH / TCP 22
   v
Bastion-SG
   |
   | SSH / TCP 22
   v
PrivateEC2SG
```


![[Pasted image 20260930104145.png]]
_Figure 10 – Bastion security group restricting SSH access to a specific `/32` source._

![[Pasted image 20260930104158.png]]
_Figure 11 – Private EC2 security group allowing SSH from the Bastion security group._

---

## 10. Bastion Host

As a bonus task, I implemented a Bastion Host in the public subnet.

The Bastion Host had the private IPv4 address:

```
10.0.0.24
```

I first connected from my Mac to the Bastion Host and then connected from the Bastion Host to the private EC2 instance using its private IPv4 address.

I used SSH agent forwarding so that my private SSH key remained on my local Mac instead of being copied onto the Bastion Host.

```
Mac
 |
 | SSH
 v
Bastion Host
10.0.0.24
 |
 | Internal VPC SSH
 v
Private EC2
10.0.1.61
```

![[Pasted image 20260930104210.png]]
_Figure 12 – Bastion Host deployed in the public subnet._

---

## 11. CloudWatch Detailed Monitoring

I enabled CloudWatch Detailed Monitoring on the Public and Private EC2 instances.

The EC2 instance details showed `Monitoring: detailed`, and I used the Monitoring tab to view metrics including CPU utilisation, network traffic, packet activity and CPU credit metrics.

![[Pasted image 20260930104220.png]]
_Figure 13 – EC2 monitoring metrics displayed through CloudWatch._

---

## 12. Connectivity Testing

After configuring the environment, I tested the network to confirm that the private EC2 instance was reachable through the Bastion Host and could initiate outbound internet connections.

While connected to the private EC2 instance, I ran:

```
hostname -I
```

The instance returned:

```
10.0.1.61
```

This confirmed that I was operating from the private EC2 instance.

I then tested outbound HTTPS connectivity:

```
curl -I https://google.com
```

The request successfully received:

```
HTTP/2 301
```

A `301` is an HTTP redirect response. The important point for this test is that the private EC2 instance successfully established an HTTPS connection to an external web server and received a response.

This validated the path:

```
Private EC2
    |
    v
Private Route Table
    |
    v
NAT Gateway
    |
    v
Internet Gateway
    |
    v
Internet
```

![[Pasted image 20260930104235.png]]
_Figure 14 – Private EC2 address confirmation and successful outbound HTTPS connectivity._

---

## 13. Troubleshooting & Issues Resolved

### Issue 1 – Unable to SSH into the Private EC2 Instance

When I initially attempted to SSH from the Bastion Host to the private EC2 instance, the connection timed out.

I checked the network path, including:

- EC2 instance status
- Security group rules
- Network ACL rules
- VPC and subnet configuration
- Route tables

I identified an incorrect route in the private route table. Traffic destined for the VPC CIDR was being sent towards the NAT Gateway instead of using the local VPC route.

The correct internal route was:

```
10.0.0.0/16 -> local
```

The internet route was configured separately as:

```
0.0.0.0/0 -> NAT Gateway
```

After correcting the route, SSH access from the Bastion Host to the private EC2 instance worked successfully.

**What I learned:** internal VPC traffic and internet-bound traffic require different routes. The VPC CIDR should remain local, while the default route handles traffic leaving the VPC.

### Issue 2 – Private EC2 Had No Outbound Internet Access

After SSH access was working, I tested outbound internet connectivity from the private EC2 instance. The initial HTTPS request timed out.

I followed the expected packet path:

```
Private EC2
    -> Private Route Table
    -> NAT Gateway
    -> Internet Gateway
    -> Internet
```

I discovered that the original NAT Gateway had been created in the private subnet.

I recreated the NAT Gateway in `Public-Subnet1`, assigned public IPv4 connectivity through an Elastic IP, and updated the private route table so that:

```
0.0.0.0/0 -> NAT Gateway
```

After making the change, the outbound HTTPS test succeeded.

**What I learned:** the private EC2 instance does not need to be in the same subnet as the NAT Gateway. The VPC's routing allows the private subnet to send traffic to a NAT Gateway in the public subnet.

---

## 14. Key Learnings

The main concepts I learned from this assignment were:

- A VPC provides the overall isolated network and private address space.
- Subnets divide the VPC into smaller network segments.
- A subnet is not public simply because an instance has a public IP; routing to an Internet Gateway is also required.
- `10.0.0.0/16 -> local` is used for traffic inside the VPC.
- `0.0.0.0/0` represents the default IPv4 route for destinations that do not match a more specific route.
- Public subnet internet traffic can route through an Internet Gateway.
- Private EC2 instances can use a NAT Gateway for outbound internet access without having public IPv4 addresses.
- A public NAT Gateway uses public IPv4 connectivity when communicating with the internet.
- Security groups control which traffic is allowed to reach AWS resources.
- A Bastion Host provides a controlled administrative path to private resources.
- SSH agent forwarding allows a local SSH key to be used through a Bastion Host without storing the private key on the Bastion.
- CloudWatch provides visibility into EC2 metrics.
- Network troubleshooting becomes easier when the packet path is checked component by component.

A useful summary of the routing design is:

```
Internal VPC traffic:
10.0.0.0/16 -> local

Public subnet internet traffic:
0.0.0.0/0 -> Internet Gateway

Private subnet outbound internet traffic:
0.0.0.0/0 -> NAT Gateway
```

---

## 15. Conclusion

This assignment gave me practical experience building and troubleshooting an AWS VPC rather than only learning the networking concepts theoretically.

I successfully created separate public and private network segments, configured Internet Gateway and NAT Gateway routing, deployed EC2 instances with different connectivity requirements, controlled access using security groups, implemented a Bastion Host and enabled CloudWatch Detailed Monitoring.

I also validated the environment through SSH and outbound connectivity testing.

The troubleshooting process reinforced how route tables, subnets, Internet Gateways, NAT Gateways and security groups work together to determine how network traffic moves through AWS.