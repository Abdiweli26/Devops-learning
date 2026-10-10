
```
Kubectl
```
Is a tool used to communicate with Kubernetes clusters every command starts with it.

```
Kubectl get nodes
```

List the machines in the clusters. Ready means its healthy

```
kubectl get pods
```
lists pods and their status


```
kubectl describe pod broken 
```

Prints pods full details. The event section at the bottom is a timeline of what kubernetes tried and what went wrong.

```
kubectl delete pod  broken
```
removes the pod

