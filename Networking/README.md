Networking Module Assignment 

This repository includes my theory learning as well hands-on projects and notes for the Networking module in my DevOps journey.

# **Contents** 

- Networking notes
- ECS project (EC2+DNS set-up)
- Commands used
- README.md

### **What I Built**

I provisioned an AWS EC2 instance running Ubuntu Linux and configured Nginx to host a static HTML website. I registered and configured a custom domain, updated the DNS records through Cloudflare to point to the EC2 instance's public IP address, and deployed my website so it was accessible via the custom domain. I also configured the necessary AWS security groups to allow HTTP traffic and securely managed the server using SSH.

### **What I Learned**

This project gave me practical experience with deploying and managing a web server on AWS. I learned how to launch and configure an EC2 instance, install and configure Nginx, connect a custom domain to a cloud-hosted server using Cloudflare DNS, and manage remote access with SSH. It also strengthened my understanding of networking concepts such as public IP addresses, DNS resolution, security groups, and how these components work together to make a website publicly accessible.

### **Challenges**

One of the main challenges was learning how to point my custom domain to the EC2 instance. After researching the process, I successfully configured the required DNS records in Cloudflare. Another issue occurred the following day when I was unable to SSH into the EC2 instance using its public IPv4 address. After investigating, I discovered that the inbound security group rule for SSH was incorrectly configured. I updated the source to my own public IP address, which restored SSH access while also improving the security of the instance by restricting access to only my device.


By Abdiweli Abdi

