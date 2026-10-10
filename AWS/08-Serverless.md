# AWS Serverless

## Serverless

Serverless = running applications/code without provisioning or managing the underlying servers.

Servers still exist — **AWS manages them**.

### Responsibility

**I manage:**
- Code
- Configuration
- IAM permissions
- Triggers
- Memory / timeout

**AWS manages:**
- Servers
- OS/infrastructure
- Availability
- Compute provisioning
- Scaling

---

## AWS Lambda

AWS Lambda = **serverless, event-driven compute** that runs code in response to events.

Event
↓
Lambda triggered
↓
My code runs
↓
Task completes

If there is no invocation, the function is not continuously running like an EC2 server.

### Common Triggers

- S3 upload
- API request
- EventBridge event/schedule
- Queue/message

---

## Example: S3 Thumbnail

User uploads image
↓
S3 stores image
↓
S3 event
↓
Lambda triggered
↓
My code resizes image
↓
Thumbnail saved to S3

**Remember:**

- S3 upload = event
- Lambda = compute
- My code = processing logic
- S3 = storage

Lambda doesn't create the thumbnail automatically — **I write the code that Lambda executes.**

---

## Why Lambda?

Good for **short, event-driven or intermittent workloads**.

### Lambda vs EC2

**EC2**
- Server runs continuously
- I manage the instance/OS
- More infrastructure control

**Lambda**
- Executes when invoked
- AWS manages infrastructure
- Automatically handles underlying compute scaling
- Less infrastructure management

Lambda isn't automatically better — choose based on the workload.

---

## IAM

Don't hard-code AWS credentials.

Give Lambda an **IAM execution role** with least-privilege permissions.

Example:

Lambda
↓
IAM Role
↓
Permission to write to S3

---

## Scaling

Multiple events can cause **concurrent Lambda executions**.

AWS manages the underlying compute scaling.

However:

Lambda scales
↓
More requests to dependencies
↓
Database/API could become overloaded

Always consider downstream services and concurrency limits.

---

## Failures & Monitoring

Functions can fail because of:

- Code errors
- IAM permissions
- Timeouts
- Dependency failures

Use **CloudWatch logs/metrics** to monitor:

- Invocations
- Errors
- Duration
- Throttling

Retry behaviour depends on how Lambda is invoked.

---

## Stateless

Design Lambda functions as **stateless**.

Don't rely on one invocation's local data being available to another.

Persistent data → S3 / DynamoDB / database.

---

## When NOT to Use Lambda

Consider EC2/ECS/EKS when:

- Workload runs continuously
- Workload doesn't fit Lambda's execution model/limits
- More infrastructure/runtime control is required
- Persistent services/containers make more sense

---

# Quick Recall

**Serverless?**
Run code/apps without managing servers.

**Lambda?**
Serverless, event-driven compute.

**Event-driven?**
Event → trigger → Lambda → code executes.

**Who writes the code?**
Me.

**Who manages the servers?**
AWS.

**Permissions?**
IAM execution role.

**Scaling?**
AWS scales Lambda execution; watch concurrency/dependencies.

**Monitoring?**
CloudWatch.

**State?**
Keep persistent state outside Lambda.

**Lambda vs EC2?**
Choose based on workload — Lambda isn't automatically better.