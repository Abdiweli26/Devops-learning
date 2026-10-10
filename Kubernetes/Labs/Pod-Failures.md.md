
## ImagePullBackOff

**Command that broke it:** `kubectl run broken --image=nginx:doesnotexist`
**Symptom:** ImagePullBBackOff
**Where I found the cause:** I ran the command kubectl describe pod broken and this broke down what happening when the pod began running. In the bottom in the event section is where i found the cause.
**What I'd ask a customer:**  I'd ask the customer to run the command kubectl describe pod broken and paste the events section at the bottom, i'd also ask for the exact image and tag and which registry its from.


## Pending

**Command that broke it:**
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: pending-pod
spec:
  containers:
  - name: nginx
    image: nginx
    resources:
      requests:
        memory: "64Gi"
EOF
```
The pod requests 64Gi of memory, far more than the node has.

**Symptom:** `kubectl get pods` showed STATUS `Pending`, READY `0/1`, RESTARTS `0`. It stayed that way and never started.

**Where I found the cause:** `kubectl describe pod pending-pod`, in the Events section. A Warning with reason `FailedScheduling` and a message saying insufficient memory: 0/1 nodes were available, because none had enough free memory for the pod's request.

**Why there's no Last State:** the pod was never placed on a node, so no container has run yet. The Node line in `describe` shows `<none>`.

**What I'd ask a customer:**
"To see why Kubernetes couldn't start the pod, please run these and paste the full output (not a screenshot or summary):
- `kubectl get pods -n <namespace>`
- `kubectl describe pod <pod-name> -n <namespace>`, including the Events section at the bottom, especially the Reason and Message

Also: how much memory does the pod request, and how much is free on your nodes? Has the request or the node size changed recently?"

## OOMKilled

**Command that broke it:**
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: oom-pod
spec:
  containers:
  - name: stress
    image: polinux/stress
    command: ["stress"]
    args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]
    resources:
      limits:
        memory: "100Mi"
EOF
```
The container tries to use 150MB of memory, but its limit is 100Mi.

**Symptom:** `kubectl get pods` showed STATUS `OOMKilled`, then `CrashLoopBackOff`, READY `0/1`, with RESTARTS rising. The container started, was killed, and restarted repeatedly.

**Where I found the cause:** `kubectl describe pod oom-pod`, in the Last State section: State `Terminated`, Reason `OOMKilled`, Exit Code `137`. The Events section only showed `BackOff` (Back-off restarting failed container stress), which is the symptom of the restarts, not the cause.

**What I'd ask a customer:**
"To see why the container keeps restarting, please run these and paste the full output (not a screenshot or summary):
- `kubectl get pods -n <namespace>`
- `kubectl describe pod <pod-name> -n <namespace>`, including the Last State section (Reason and Exit Code) and the Events at the bottom

Also: what memory limit is set on the container? Has the workload changed recently, for example batch size, model size, or context length?"

## CrashLoopBackOff (app error)

**Command that broke it:**
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: crash-pod
spec:
  containers:
  - name: app
    image: busybox
    command: ["sh", "-c", "echo 'starting up'; echo 'FATAL: cannot find config file' >&2; exit 1"]
EOF
```
The container starts an app that prints an error about a missing config file and exits with code 1.

**Symptom:** `kubectl get pods` alternated between `CrashLoopBackOff` and `Error`, READY `0/1`, RESTARTS rising.

**Where I found the cause:** `kubectl logs crash-pod` showed "starting up" followed by "FATAL: cannot find config file". `kubectl describe pod crash-pod` showed a node assigned, Last State `Terminated` with Reason `Error` and Exit Code `1` (the app exited itself with an error). Events showed the container created and started, then `BackOff` (restarting failed container). The Events only show the restart pattern. The cause is in the logs.

**What I'd ask a customer:**
"To see why the container keeps restarting, please run these and paste the full output (not a screenshot or summary):
- `kubectl get pods -n <namespace>`
- `kubectl logs <pod-name> -n <namespace> --previous` (the logs from the run that crashed)
- `kubectl describe pod <pod-name> -n <namespace>`, including the Last State (Reason and Exit Code) and the Events

Also: has the config, image version, or environment changed recently?"