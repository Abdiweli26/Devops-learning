# **Intro:**

I’ve created my EC2 instance and pointed its Public IPv4 address to a domain I bought on Cloudflare. Here I’ll show you how I created it and launched it. 

# **Live Example**

https://abdiwelia45.org/
---
#**How to Create an EC2+DOMAIN+DNS**

**Step 1**

Go to AWS and create an account.

**Step 2**

Open the EC2 console on the AWS account and Click “Launch Instance”
![[Pasted image 20260804214842.png|525]]

**Step 3**
Keep everything as default except the following.
- Pick a an AMI( Amamzon machine image) I chose Ubuntu.
- Under network settings tick allow SSH traffic from, if you'll be SSHing from your terminal click my IP address or if your SSHing from a VM for example add a customer IP
- Tick Allow HTTPS and HTTP
Launch the instance and keep a copy of the key downloaded.
**Step 4**

Buy a Domain or create on using Route 53, I used Cloudflare. If your using Cloudlfare once you've bought the Domain name find it in the Cloudflare console and underneath DNS records add a record. Choose type A and enter the IPV4 address of the EC2 in the box. You can find the IP address of the EC2 in the console by clicking on the running Instance.

**Step 5** 

Now after some time you should see the Welcome page of Nginx. To modify this you must SSH into the EC2 instance on your terminal

**Step 6**
Use the these two commands to SSH into the EC2, edit it your details

`chmod 400 ~/Downloads/your-key.pem` 
`ssh -i ~/Downloads/your-key.pem ubuntu@YOUR_PUBLIC_IP`


**Step 7**

Install Ngnix, you can also go further to edit the HTML file in /etc/ to create a nice page heres mine below
```
sudo yum install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```


