## EBS (Elastic Block Store)

An **EBS volume** is persistent block storage that can be attached to an EC2 instance.

Think of it as a virtual hard drive/SSD.

- Stores data used by an EC2 instance
- Data persists when an instance is stopped and started
- Can be used as the instance's root volume or additional storage
### EBS Persistence

- EC2 stopped → EBS data remains
- EC2 started again → EBS data is still available
- EC2 terminated → Root EBS volume is typically deleted by default
- EBS volumes can be configured to persist after termination

## AMI (Amazon Machine Image)

An **AMI** is a template used to launch EC2 instances.

It can contain:
- Operating system
- Software
- Configuration

You can use existing AMIs or create custom AMIs for your own requirements.

## EFS (Elastic File System)

Amazon EFS is a managed shared file system.

- Multiple EC2 instances can access the same file system
- Useful when multiple servers need access to the same files
- Automatically scales its storage capacity as files are added or removed

### EBS vs EFS

EBS → Block storage, similar to a virtual hard drive
EFS → Shared file storage accessible by multiple instances