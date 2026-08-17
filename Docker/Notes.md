Here you'll find all my notes pertaining to Docker


# What is a container 

A container is a light-weight virtualisation used to package ,manage and deploy applications and their dependencies.

**Benefits** 
- It's light weight meaning it needs fewer resources in comparison to a VM which needs an operating system, however containers share the OS kernel of the host machine they run on
- Less disk space
- Less CPU
- Quick start
- Cost effective 


## What is Docker?

Docker is an open-source containerisation platform used to build, manage, deploy and package containers.

### Key Components 

#### Docker Engine

Docker engine is a core container runtime used to manage,  run containers in a host machine 

#### Docker Hub

Docker Hub is a cloud-based registry used to store, share and distribute Docker images.

Docker Hub = Image store
Docker Engine = Container Runtime
Container = Running Instance
Image = Blueprint


# Docker Structure

Docker Host
│
├── Container 1
│   └── Application / Backend
│
└── Container 2
    └── Database



                    Docker Host
                         │
                  app-network
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          ▼
          Frontend    Backend    Database
          Container   Container  Container
              │          │          │
              │          └──────────┘
              │              │
              └──────────────┘

**Why separate them?**

Imagine your application is a website.

You could have:

- Frontend container → serves the website
- Backend container → handles application logic/API
- Database container → stores data

Each container has a specific responsibility.

The backend might need to talk to the database:

Backend Container
       │
       │  database:3306
       ▼
Database Container

Don't think of Docker as:

"I put my entire application inside one container."

Think:

"I can package different services into separate containers and connect those containers together."

That's one of the reasons Docker becomes particularly useful for multi-container applications.

And later, when you learn Docker Compose, you'll see how you can define something like:

`frontend`
`backend`
`database`
`network`
`volumes`

in one configuration and bring the whole application up together.



# Containers vs Virtual Machines

## 🐳 Containers

A **container** packages an application and its dependencies so it can run consistently across different environments.

- **Lightweight** — uses fewer resources than a VM.
- **Shares the host OS kernel** — containers don't need their own full operating system/kernel.
- **Fast startup** — usually starts in seconds.
- **Process-level isolation** — applications/processes are isolated from each other.
- **Portable** — can run anywhere a compatible container runtime is available.
- **Cheaper** — lower resource usage means you can run more containers on the same hardware.

---

## 🖥️ Virtual Machines

A **virtual machine (VM)** emulates a complete computer and runs its own operating system.

- **Heavier** — requires more CPU, RAM and storage.
- **Has its own OS/kernel** — each VM runs a complete operating system.
- **Slower startup** — typically takes longer to boot.
- **Stronger isolation** — VMs are isolated at the virtual-machine level.
- **Less lightweight/portable** — moving a VM can involve moving the entire OS and its virtual disk.
- **More expensive** — each VM requires additional resources.

---

## ⚖️ Quick Comparison

| Feature | 🐳 Container | 🖥️ Virtual Machine |
|---|---|---|
| **Startup** | Very fast — seconds | Slower — seconds to minutes |
| **Resources** | Low | Higher |
| **OS** | Shares host kernel | Own OS & kernel |
| **Isolation** | Process/OS-level | Stronger VM-level isolation |
| **Portability** | Very portable | Less lightweight to move |
| **Cost** | Lower | Higher |
| **Best for** | Applications & services | Running complete operating systems |

---

## 🔑 Key Concept

> **Containers share the host kernel.**
>
> **VMs have their own kernel.**

### Architecture

**VM:**

`Hardware → Hypervisor → VM → Guest OS → Application`

**Container:**

`Hardware → Host OS → Container Runtime → Container → Application`

---

## 🧠 Simple Analogy

**VM = renting an entire house**

You get your own operating system and resources.

**Container = renting a room in a house**

You have your own isolated space, but share the underlying resources.

---

### Remember

> **Containers are lightweight because they don't need to carry a complete operating system with them.**


# Understanding the Dockerfile

From
- Specifies the base image to use for the Docker image
Run
- Executes commands in the container
Copy
-  Copies files from the host machine into the container
Workdir
- Sets the working directory for subsequent instructions 
CMD
- Specifies the command to run when the container starts


# Containerising Web Application 

`docker build -t hello-flask .` 

```
docker build
```
Initiates the docker build process

```
-t
```
tags the image with the name that follows

```
.
```
Point it to the current working directory 


# Docker Networking 


**Bridge Network**

This is the default network that allows containers that are connected to a network bridge to communicated with one another.

Similarly rooms in one house may communicate with each other using intercoms.

**Host Network**

When a containers using the host's machines network, it's as if your container is plugged directly into your home network.

**None network**

When a container is completed isolated from all networks. 

# Linking Containers together

Example
```
docker network create my-custom-network
```

A Docker network provides a network where containers can communicate with each other.

              my-network
        ┌─────────────────────┐
        │                     │
   ┌────▼────┐           ┌────▼─────┐
   │  web    │ ────────→ │ database │
   └─────────┘           └──────────┘

Containers on a user-defined Docker network can communicate with each other using container/service names, which Docker resolves to their IP addresses.

`docker run -d --name mydb --network my-custom-network -e MYSQL_Root_PASSWORD=my-secret-pw mysql:8`


`docker run -d --name mydb
This runs a containers for the SQL database 

`--network my-custom-network`
This attaches it to the network we created 

`-e MYSQL_Root_PASSWORD=my-secret-pw mysql:8`
This then sets the password and sets the MYSQL version that we're using.


# Docker Compose 

**Introduction** 

**Docker Compose:** A tool for defining and running **multi-container applications**. It allows you to configure multiple services in a `compose.yaml` file and manage them together.

**Key features**
- Docker-compose.yml file
- Commands 
- Networking 
**Docker Compose = Configuration + Multi-container management + Networking + Storage**

And one important terminology point:

> Docker Compose doesn't just "run multiple containers." It manages **services** that together make up a multi-container application.

A `compose.yaml` file might define `web`, `app`, and `db` as three services, with each service typically running in its own container.

**Why is Docker Compose important in DevOps?**

- Makes development and testing easier 
- Ensures consistency 
- Enhances Teamwork

# Docker Registries

Docker registry is a service used to store, manage and distribute Docker images


**Importance of Docker registries in DevOps**

- Streamlines workflow
- Helps with consistency 


# Important Docker Commands to know 

```
docker system prune
```

This stops all containers, any networks not being used by at least one container, dangling images and dangling build cache.

## Check Docker

`docker --version`
Shows the installed Docker version.

`docker info`
Shows information about the Docker Engine and environment.

### Images


**List images**

`docker images`
or
`docker image ls`


**Pull an image**

`docker pull nginx`

**Build an image**

`docker build -t myapp .`

Build an image from docker file

`docker rmi myapp`

#### Containers

**Run a container** 
`docker run nginx`

**Creates and starts a container from an image.**
```
docker run -d -p 8080:80 --name web nginx
```
- `-d` → detached/background mode
- `-p 8080:80` → maps host port `8080` to container port `80`
- `--name web` → gives the container a name
**List running containers:**

`docker ps`

List all containers:

`docker ps -a`

**Stop a container:**

`docker stop web`

**Start an existing container:**

`docker start web`

**Restart a container:**

`docker restart web`

**Remove a container:**
```
docker rm web
```

##### Inspect & Troubleshoot

**View container logs:**
`docker logs web`

**Follow logs in real time:**
`docker logs -f web`

**View container details:**

`docker inspect web`

**View resource usage:**

`docker stats`

|Command|Purpose|
|---|---|
|`docker pull`|Download an image|
|`docker images`|List images|
|`docker build`|Build an image|
|`docker run`|Create + start a container|
|`docker ps`|List running containers|
|`docker ps -a`|List all containers|
|`docker stop`|Stop a container|
|`docker start`|Start a stopped container|
|`docker rm`|Remove a container|
|`docker rmi`|Remove an image|
|`docker logs`|View container logs|
|`docker exec`|Run a command inside a container|
|`docker inspect`|Inspect container/image configuration|
|`docker push`|Upload an image to a registry|
|`docker compose up`|Start a multi-container application|
|`docker compose down`|Stop/remove a Compose application|

# Docker Swarm vs Kubernetes


| Docker Swarm                             | Kubernetes                                    |
| ---------------------------------------- | --------------------------------------------- |
| No Auto Scaling                          | Auto Scaling                                  |
| Good Community                           | Great Active Community                        |
| Easy to start a Cluster                  | Difficult to start a cluster                  |
| Limited to the Docker API's capabilities | Not limited to the Docker API's Capabilities  |
|                                          |                                               |
