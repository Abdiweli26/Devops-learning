
## Scalability

**Scalability** is the ability of a system to adjust its resources to handle changes in workload or demand.

Two main approaches:

- **Vertical Scaling** → Change the capacity of an existing server
- **Horizontal Scaling** → Add or remove servers

## High Availability 

**High Availability (HA)** means designing a system to remain available even when part of the  infrastructure fails.

In AWS, this can be achieved by running resources across multiple Availability Zones, reducing single points of failure.

## Load Balancing

A load balancer receives incoming traffic and routes it to healthy targets within configured target groups.

This helps improve:
- Scalability
- Availability 
- Fault tolerance

Application Load Balancer
          ↓
     Target Group
      ↙   ↓   ↘
    EC2  EC2  EC2

Targets can include: 
- EC2 instances 
- IP addresses 
- Lambda function

Target groups also define health-check settings for their targets.
### Load Balancer Health Checks

A load balancer periodically performs health  checks on its targets.

- Healthy target → Receives traffic
- Unhealthy target → Traffic is not routed to it
- Recovered target → Can receive traffic again after passing health checks

### Application Load Balancer (ALB)

An **Application Load Balancer** operates at Layer 7 and routes application traffic such as:

 - HTTP - Port 80
 - HTTPS - Port 443

example.com/images/*  ──→ Target Group A
example.com/api/*     ──→ Target Group B

ALB Security Group
Inbound: HTTPS 443 ← Internet (0.0.0.0/0)

EC2 Security Group
Inbound: HTTP 80 ← ALB Security Group

When setting up the security groups you must ensure that communication is direct from the  user to the instance.  It should be like this 


User enters example.com
        ↓
       DNS 
        ↓
       ALB ──→ Here  the security group should allow  all traffic on the ports you need.
        ↓
   Target Group (Instance )
        ↓
    Healthy EC2
        ↓
    ( Instance )  ──→ Here you ensure that the security group ensure traffic is only allowed through application port and you'd set the  source to the ALB's security group.

### ALB Path-Based Routing 

An Application Load Balancer can route  traffic to different target  groups based on the URL path.

Example:
- `/images/*` → Image target group 
- `/api/*` → API target group

This is called  **Path-based Routing**

api.example.com → API Target Group
shop.example.com → Shop Target Group

ALB = Layer 7 → can inspect HTTP requests → can make smarter routing decisions.


# Network Load Balancer 

- Operates at **Layer 4 -Transport  Layer**
- Handles **TCP, UDP AND TLS traffic **
- Designed for high performance, low latency traffic 
- Routes based on network level information such as IP and Ports

## SSL/TLS 

**Secure Socket Layers**
**Transport Layer Security** 

- SSL/TLS are you used to encrypt data in transit between systems 
- Uses certificates to establish secure connections 
- Certificates verify the identity of the servers
- TLS is the modern version of SSL
## SNI 

Server Name Indication 
- Allows load balancers to support multIple SSL/TLS for multiple domain names  
- It helps the load balancer select the correct certificate by using the hostname requested by the client 

### SSL  VS TLS

- SSL - Secure  Socker Layer- older/depracated
- TLS- Transport Layer Security - modern standard 
- TLS protects data in transit through encryption 
- People still commonly say "SSL  certificates"  even though modern systems use TLS 

### Auto Scaling Group (ASG)

An auto scaling group manages the number of instances due to the demand

- Scale in - removes  instances
- Scale out  - Adds  instances
- Help maintain availability and performances  
- Help ensure unnecessary costs are reduced.

### ASG Capacity 

- Minimum - The lowest number of instances the ASG maintains 
- Desired  - The current number of instances is maintaining 
- Maximum  - The highest number of instance the ASG can scale out to

### Cloudwatch  and Auto Scaling 

Cloudwatch monitors metrics such as CPU utilisation.

CloudWatch alarms can trigger scaling actions when configured threshold are met.

Example: - 
- High CPU → ASG scales out → Adds instances 
- Low CPU → ASG scales in → Removes instances