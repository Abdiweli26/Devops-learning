# Amazon EC2

**Amazon EC2  (Elastic Compute Cloud)** is an AWS service used to and  run virtual services, called EC2 Instances in the cloud.

When launching an instance, you can configure resources such as:
- Operating system
- CPU
- Memory
- Storage
- Networking  
### EC2 vs EC2 Instance

**EC2:** The AWS service used to create and manage virtual servers.

**EC2 Instance:** A virtual server running within EC2.

### EC2 Configuration

When launching an EC2 instance, you can configure:
- CPU (vCPU)
- Memory (RAM)
- Storage
- Operating system / AMI
- Networking
- Security

### AMI

**AMI (Amazon Machine Image):** A template used to launch EC2 instances. It can contain the operating system, software and configuration needed by the instance.

AMI = blueprint/template
EC2 instance = server created from that blueprint

###  EC2 Sizing 

EC2 instance can be selected based on resources such as:
- CPU 
- Memory (RAM)
- Storage
- Network performances

### EC2 Configuration 

When launching EC2 you can choose:
- AMI / Operating System
- Instance type (CPU & RAM) (SIZING)
- Storage
- Networking
- Security settings
## EC2 Instance Types

AWS provides different EC2 instance types because workloads have different resource requirements.

For example:
- Some workloads require more CPU
- Some require more memory (RAM)
- Some require higher storage performance
- Some need a balance of resources
### Instance Type Categories

- **General Purpose** → Balanced CPU and memory
- **Compute Optimized** → CPU-intensive workloads
- **Memory Optimized** → RAM-intensive workloads
- **Storage Optimized** → High-performance storage workloads
### EC2 Purchasing Options

**On-Demand**
- Pay for usage with no long-term commitment
- Good for short-term or unpredictable workloads

**Savings Plans / Reserved Instances**
- Longer-term commitment for lower costs
- Good for predictable, steady workloads

**Spot Instances**
- Uses spare AWS capacity at a large discount
- Can be interrupted by AWS
- Good for flexible, fault-tolerant workloads

**Dedicated Hosts**
- Physical server dedicated to one customer
- Useful for certain compliance or software licensing requirements
### EC2 Web Server Access

For users to reach a web server running on EC2, the Security Group must allow the required inbound traffic.

- HTTP → Port 80
- HTTPS → Port 443
- SSH → Port 22
### Stop vs Terminate

**Stop**
- Shuts down the EC2 instance
- Instance can be started again
- EBS data is normally preserved

**Terminate**
- Permanently deletes the EC2 instance
- The same instance cannot be restarted
- Root EBS volume is typically deleted by default