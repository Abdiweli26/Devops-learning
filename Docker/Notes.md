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

