# Learning Kubernetes

Documenting my progress learning Kubernetes.

## The hierarchy

- **Cluster:** the whole system, made up of several nodes
- **Node:** one machine in the cluster, runs multiple pods
- **Pod:** the smallest unit in Kubernetes, contains one or more containers
- **Container:** the packaged app that actually runs

Cluster → Node → Pod → Container