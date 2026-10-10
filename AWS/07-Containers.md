# AWS  Containers 

Containers package an application and  it's dependencies to run consistently across environments.

Compared with Virtual Machines 
- Container's share the host's OS Kernel
- Container are lightweight, easy start up
- VM's has it's on OS
- Requires more resources

## Amazon ECS

**ECS ( Elastic Container Service)** is an orchestration service for containers

It allows you to
- Deploy containerised applications 
- Manage and run containers 
- Scale containerised workloads 
- Integrate containers with other AWS services

### EC2 Launch Type

With the EC2 Launch type , ECS runs the containers on EC2.

ECS will then be responsible for the orchestration EC2 instances such as failed tasks, stopping and starting.

You'll be responsible for the underlying EC2 instances.

## ECS Task Definition, task and service


### Task Definition 

**Task definition** is a blueprint that describes how ECS should run the tasks

It can define
- Container image
- CPU & Memory 
- Ports
- Environment variables 
- IAM roles
- one or more containers

### Task 

A task is a running instance of the task definition 

A task can contain one or more containers


### ECS service 

An **ECS Service** maintains the number of desired tasks.

ECS Service Desired Tasks = 3 
── Task 1 → App Container
── Task 2 → App Container 
── Task 3 → App Container

If a tasks fails then ECS service can launch a replacement

Task Definition = Blueprint
Task = Running workload 
Service = Maintains desired tasks

## ECR

**Elastic Container Registry**


AWS's container image registry 

Typical workflow 
 
 Dockerfile 
 ↓ 
 Build Image 
 ↓ 
 Push Image to ECR 
 ↓ 
 ECS pulls Image
 ↓ 
 ECS Task runs container 
 
 ECR = Stores images
 ECS = Runs/manages container workloads

# IAM roles for ECS

ECS tasks can use **IAM Task Roles** to access other AWS services.
Example: 
ECS Task 
↓ 
IAM Task Role 
↓ 
IAM Policy 
↓ 
S3

This avoids storing long-term AWS access keys inside containers.

## ECS + Application Load Balancer 

An ALB can distribute HTTTP/HTTPS traffic across healthy ECS tasks.

Users
↓
ALB
↓
Target Group
↓
ECS Tasks
├── Task 1
├── Task 2
└── Task 3

The load balancer uses health checks to determine which targets should receive traffic.

# ECS Service Auto Scaling 

ECS Service Auto Scaling increases/decreases the number of tasks depending on the demand and the configured scaling policies 

High demand
↓
Scale Out
↓
More ECS Tasks

Low demand
↓
Scale In
↓
Fewer ECS Tasks

Important distinction:

EC2 Auto Scaling → Scales EC2 instances
ECS Service Auto Scaling → Scales ECS tasks

## Amazon EKS 

**EKS (Elastic Kubernetes Service)** is an AWS service which manages Kubernetes 

It allows you to  run and manage Kubernetes workloads on AWS

### ECS vs EKS

ECS → AWS-native container orchestration
EKS → Kubernetes orchestration on AWS

Use ECS when you want AWS's native container orchestration service.

Use EKS when you need or already use Kubernetes.

# EKS Node Type

EKS provides different option for running workloads:

### Managed nodes
AWS helps manage the nodes

### Self-Managed nodes
You have the responsibility of managing the nodes

### AWS Fargate 

No need of managing nodes and the workload will run.

## Key Architecture

Users
↓
ALB
↓
Target Group
↓
ECS Service
↓
ECS Tasks
↓
Containers

Container images are stored in ECR.

IAM Task Roles provide ECS tasks with permissions to access AWS services.

|                                  | Managed Nodes | Fargate                           |
| -------------------------------- | ------------- | --------------------------------- |
| EC2 worker nodes visible to you? | **Yes**       | **No**                            |
| Choose/manage node capacity?     | **Yes**       | **No underlying nodes to manage** |
| AWS helps manage infrastructure? | **Yes**       | **Yes, much more of it**          |
| You focus mainly on workloads?   | Partially     | **Yes**                           |
