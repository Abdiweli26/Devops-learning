# AWS DNS & CloudFront — Revision Notes

## 1. DNS

**DNS (Domain Name System)** translates human-readable domain names into IP addresses.

```
example.com → 93.184.216.34
```

Without DNS, users would need to remember IP addresses instead of domain names.

---

## 2. DNS Lookup Process

If the answer isn't already cached:

```
User enters example.com
        ↓
DNS Resolver
        ↓
Root DNS Server
        ↓
.com TLD Server
        ↓
Authoritative DNS Server
        ↓
IP address returned
        ↓
Browser connects to destination
```

### Root Server

Points the resolver towards the appropriate **TLD server**.

### TLD Server

Handles extensions such as:

```
.com
.org
.net
.uk
```

It tells the resolver which **authoritative name server** is responsible for the domain.

### Authoritative DNS Server

Holds the DNS records for the domain and provides the final DNS answer.

---

# 3. DNS Records

### A Record

Maps a hostname to an **IPv4 address**.

```
example.com → 192.0.2.10
```

### AAAA Record

Maps a hostname to an **IPv6 address**.

### CNAME

Maps one hostname to another hostname.

```
www.example.com → example.com
```

### MX

Specifies the mail servers responsible for receiving email for a domain.

---

# 4. TTL

**TTL (Time To Live)** determines how long a DNS response can remain cached before it needs to be refreshed.

```
TTL = 300 seconds
```

A longer TTL means fewer DNS lookups but changes take longer to propagate through caches.

A shorter TTL allows changes to be picked up sooner.

---

# 5. Route 53

**Amazon Route 53** is AWS's DNS service.

A **Hosted Zone** is a container for the DNS records belonging to a domain.

```
Hosted Zone: example.com

A      example.com
CNAME  www.example.com
MX     example.com
```

### Public Hosted Zone

DNS records are resolvable over the internet.

### Private Hosted Zone

DNS records are available within associated VPCs.

---

# 6. Route 53 Alias

A Route 53 **Alias record** can point a domain to supported AWS resources.

For example:

```
app.example.com
       ↓
Route 53 Alias
       ↓
Application Load Balancer
```

This will be relevant in your ALB assignment when you get to the bonus section.

---

# 7. Route 53 Routing Policies

### Simple

Standard DNS routing to a resource.

### Weighted

Splits traffic according to configured weights.

```
70% → Server A
30% → Server B
```

### Latency

Routes users toward the AWS Region that provides the lowest latency.

### Failover

Used for active/passive disaster recovery.

```
Primary healthy?
      ↓
     Yes → Primary

Primary unhealthy?
      ↓
     No → Secondary
```

Route 53 **health checks** can help determine when failover should occur.

---

# CloudFront

## 8. What is CloudFront?

**Amazon CloudFront is AWS's Content Delivery Network (CDN).**

It improves performance by delivering content through **edge locations** closer to users.

Without CloudFront:

```
London User ──────────────→ Origin
```

With CloudFront:

```
London User
     ↓
Nearby CloudFront Edge
     ↓
Cached content
```

This reduces the distance requests may need to travel to retrieve content.

---

# 9. Origin

The **origin** is the original source CloudFront retrieves content from.

Examples include:

```
S3
ALB
Web server
```

For this architecture:

```
User
 ↓
CloudFront
 ↓
ALB       ← CloudFront Origin
 ↓
EC2
```

The **ALB is the origin**, not the EC2 instance, because CloudFront communicates directly with the ALB.

---

# 10. Edge Locations

CloudFront has **edge locations** distributed geographically.

Content can be cached at these locations so users can receive it closer to where they are.

```
User
 ↓
Nearby Edge Location
 ↓
Origin (when required)
```

---

# 11. Cache Hit vs Cache Miss

### Cache Hit

CloudFront already has the requested object cached.

```
User
 ↓
CloudFront
 ↓
Cache HIT ✅
 ↓
Return content
```

No request to the origin is needed for that cached response.

**HIT = "I have it."**

### Cache Miss

CloudFront doesn't have the requested object available in that cache.

```
User
 ↓
CloudFront
 ↓
Cache MISS ❌
 ↓
Origin
 ↓
Fetch content
 ↓
Cache content
 ↓
Return to user
```

**MISS = "I need to fetch it."**

---

# 12. CloudFront TTL

TTL determines **how long content remains cached before the cached copy expires**.

For example:

```
logo.png
TTL = 1 hour
```

A longer TTL can reduce requests to the origin.

A shorter TTL allows frequently changing content to refresh sooner.

---

# 13. CloudFront Invalidation

Imagine:

```
CloudFront → old logo.png
Origin     → new logo.png
```

CloudFront may continue serving its cached version until it expires.

An **invalidation** allows you to expire cached content early rather than waiting for its normal TTL.

```
Update logo.png
      ↓
Create invalidation
      ↓
Old cached object invalidated
      ↓
CloudFront fetches updated version when requested
```

Remember:

**TTL = when cache normally expires**

**Invalidation = expire it early**

---

# 14. Private S3 + CloudFront

An S3 bucket doesn't need to be publicly accessible just because the website content is public.

A better architecture is:

```
Internet
   ↓
CloudFront
   ↓
Private S3 Bucket
```

Users:

```
User → S3 directly ❌

User → CloudFront → S3 ✅
```

**Origin Access Control (OAC)** can allow CloudFront to access a private S3 origin.

---

# 15. CloudFront vs ALB

Don't confuse these two.

### CloudFront

```
CDN
↓
Edge locations
↓
Caching
↓
Faster global content delivery
```

### ALB

```
Receives application traffic
↓
Checks target health
↓
Distributes requests
↓
EC2-1 / EC2-2
```

They can work together:

```
Users
  ↓
CloudFront
  ↓
ALB
 ↙  ↘
EC2  EC2
```

**Easy memory rule:**

**Route 53** → _Where should this domain resolve?_  
**CloudFront** → _Can I deliver/cache this closer to the user?_  
**ALB** → _Which healthy backend should receive this request?_

---

## Quick Revision

```
DNS       = Domain name → destination
Route 53  = AWS DNS service
A         = Hostname → IPv4
AAAA      = Hostname → IPv6
CNAME     = Hostname → hostname
MX        = Mail server
Alias     = Route 53 → supported AWS resource

CloudFront = CDN
Edge       = Location close to users
Origin     = Original source of content
Cache HIT  = CloudFront has it
Cache MISS = CloudFront fetches it
TTL        = How long it's cached
Invalidation = Expire cache early
OAC        = CloudFront access to private S3
```