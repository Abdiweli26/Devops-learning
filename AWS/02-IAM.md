Identity and Access  Management


**This controls who can access AWS resources and what actions they are allowed to perform.

IAM handles
- Authentication - Who  are you?
- Authorisation - What are you allowed to do?

## IAM Users & Groups

**IAM User:** An identity within an AWS account that can be given credentials and permissions.

**IAM Group:** A collection of IAM users used to manage permissions together.

Users in a group receive the permissions from policies attached to that group.

Example:
Developers Group → Developer permissions
├── User A
├── User B
└── User C

## IAM  Policies

An **IAM policy**  is  a JSON document that defines permissions in AWS.

A policy  specifies:
- **Effect** - Allow or Deny
- **Action** -  What actions can be performed
- **Resource** - Which AWS resource those actions apply to
### Policy Inheritance

When a policy is attached to an IAM group, users within that group inherit the permissions granted by  that policy.

### Least  Privilege

Give users, groups, or roles only the minimum permissions required to perform their tasks and nothing more.

## IAM Roles

An **IAM role** is an AWS identity that can be assumed  by authorised users, applications, or AWS services.

- Roles have permissions defined through policies.
- Roles provide temporary credentials when assumed.
- They avoid the need to store permanent access keys.

Example:
ECS → assumed IAM role → Role allows access to S3

**Policy:** A JSON document that defines permissions.

**Role:** An AWS identity with permissions defined by policies that can be assumed by authorised principals, such as users or AWS services, providing temporary credentials.

## MFA

**MFA (Multi-Factor Authentication)** adds an additional authentication factor alongside a password.

It improves security because a stolen or compromised password alone is not enough to access the account.

Examples:
- Authenticator app
- Hardware security key

## AWS CLI & SDK

**AWS CLI** : A command-line tool used  to interact with and manage AWS services from a terminal.
**AWS  SDK** : Libraries for programming languages that allow applications and code to interact with AWS services programmatically.

## Password Policy

An IAM password policy defines and enforces password requirement for IAM users.

Examples
- Minimum  password length
- Required character types
- Password expiration
- Preventing password reuse

## Authentication vs Authorisation

**Authentication** : Verifies who you are 
Example:  Signing in using your username, password  and  MFA.

**Authorisation**: Determines what you are allowed to access  or  do after identity has been checked.
Example: Whether you're permitted to start or stop an EC2 instance.

## Root User

The root user is the original identity created with the AWS account and has full access to the account.

Best practices:
- Do not use the root user for everyday tasks.
- Enable MFA on the root user.
- Protect the root credentials.
- Use appropriate IAM/federated identities for normal administration.
### Access Key Credentials

**Access Key ID:** Identifies the access key.

**Secret Access Key:** Secret credential used when signing/authenticating AWS API requests.

Never expose or commit the Secret Access Key to source control.

## IAM Security Tools

**Credential Report:** Account-wide report showing IAM users and the status of their credentials, such as passwords, MFA and access keys.

**Access Advisor:** Shows service permissions and last-accessed information, helping identify unused permissions.