# Azure Messaging Decision Matrix – Queue vs Service Bus Topic

## Overview

In Azure messaging architectures:

### Use Queue When:

* One producer sends a message to one consumer.
* Work must be processed exactly once.
* Commands/tasks are distributed among workers.
* Point-to-point communication is required.

### Use Service Bus Topic When:

* One producer sends a message to multiple consumers.
* Publish/Subscribe (Pub/Sub) pattern is required.
* Multiple systems need the same event.
* Event-driven architecture is used.

---

# Decision Matrix

| ID | Integration                     | Recommended Service | Reason                                                                    |
| -- | ------------------------------- | ------------------- | ------------------------------------------------------------------------- |
| A  | Settlement Command              | Queue               | Command sent to a single settlement processor for execution               |
| B  | Payment Received Broadcast      | Service Bus Topic   | Event must be consumed by multiple downstream systems                     |
| C  | SMS / Push Notifications        | Queue               | Notification tasks are distributed to notification workers for processing |
| D  | Fraud Score Request             | Queue               | Request/response workflow targeting a single fraud engine                 |
| E  | Account State Change Events     | Service Bus Topic   | Multiple services may need to react to account status changes             |
| F  | End-of-Day Reconciliation Batch | Queue               | Batch processing workload handled by dedicated reconciliation workers     |

---

# Detailed Explanation

## A. Settlement Command

### Recommended: Queue

### Why?

A settlement command represents an instruction that must be executed once by a specific service.

Example:

```text
"Settle Payment #12345"
```

Only the Settlement Processor should handle this command.

### Architecture

```text
Payment Service
      |
      v
Settlement Queue
      |
      v
Settlement Processor
```

### Why Queue?

* Point-to-point messaging
* Guaranteed processing
* Single consumer execution
* Prevents duplicate settlement

### Why Not Topic?

A settlement command should not be processed by multiple services because duplicate settlement may occur.

---

## B. Payment Received Broadcast

### Recommended: Service Bus Topic

### Why?

When a payment is received, multiple systems may need to know about it.

Examples:

* Notification Service
* Analytics Service
* Fraud Monitoring
* Audit Service
* Loyalty Program

### Architecture

```text
Payment Service
        |
        v
 Payment Topic
   /    |    \
  /     |     \
SMS   Audit  Analytics
```

### Benefits

* One event published
* Multiple subscribers
* Loose coupling
* Easy onboarding of new consumers

### Why Not Queue?

A queue delivers the message to only one consumer, which would prevent other systems from receiving the event.

---

## C. SMS / Push Notifications

### Recommended: Queue

### Why?

Notification delivery is a background task.

Example:

```text
Send SMS to Customer
Send Push Notification
Send Email
```

A notification worker processes each task.

### Architecture

```text
Application
     |
     v
Notification Queue
     |
     v
Notification Worker
```

### Benefits

* Smooth handling of traffic spikes
* Retry support
* Decoupled processing
* Single execution per notification

### Why Not Topic?

Typically a notification request should be processed once by the notification service.

---

## D. Fraud Score Request

### Recommended: Queue

### Why?

A fraud score request is a command sent to a fraud analysis engine.

Example:

```text
Calculate Fraud Score
for Transaction #98765
```

Only one fraud service should process the request.

### Architecture

```text
Payment Service
      |
      v
Fraud Request Queue
      |
      v
Fraud Engine
```

### Benefits

* Reliable request processing
* Workload buffering
* Single consumer execution

### Why Not Topic?

Multiple fraud engines processing the same request could generate inconsistent results.

---

## E. Account State Change Events

### Recommended: Service Bus Topic

### Why?

Account state changes are events.

Examples:

```text
Account Activated
Account Suspended
Account Closed
Account Frozen
```

Many systems may need these events.

Examples of subscribers:

* CRM System
* Billing System
* Audit Service
* Compliance Service
* Notification Service

### Architecture

```text
Account Service
        |
        v
 Account Topic
  /   /   \   \
CRM Billing Audit Notifications
```

### Benefits

* Event-driven architecture
* Multiple consumers
* Easy future expansion
* Decoupled services

### Why Not Queue?

Only one consumer would receive the event, causing other systems to miss important account changes.

---

## F. End-of-Day Reconciliation Batch

### Recommended: Queue

### Why?

Reconciliation jobs are work items that must be processed by a dedicated reconciliation engine.

Example:

```text
Reconcile Transactions
for 09-Jun-2026
```

### Architecture

```text
Scheduler
    |
    v
Reconciliation Queue
    |
    v
Reconciliation Worker
```

### Benefits

* Reliable execution
* Retry capability
* Workload management
* Sequential processing

### Why Not Topic?

A reconciliation batch is a command/task, not an event for multiple subscribers.

---

# Architecture Summary

| Pattern              | Azure Service     |
| -------------------- | ----------------- |
| Command Processing   | Queue             |
| Background Jobs      | Queue             |
| Task Distribution    | Queue             |
| Request/Response     | Queue             |
| Event Broadcasting   | Service Bus Topic |
| Publish/Subscribe    | Service Bus Topic |
| Event-Driven Systems | Service Bus Topic |

---

# Final Answers

| ID | Integration                     | Service           |
| -- | ------------------------------- | ----------------- |
| A  | Settlement Command              | Queue             |
| B  | Payment Received Broadcast      | Service Bus Topic |
| C  | SMS / Push Notifications        | Queue             |
| D  | Fraud Score Request             | Queue             |
| E  | Account State Change Events     | Service Bus Topic |
| F  | End-of-Day Reconciliation Batch | Queue             |

## Rule of Thumb

### Queue

Use when a message represents a **command or task** that should be processed by **exactly one consumer**.

### Service Bus Topic

Use when a message represents an **event** that should be delivered to **multiple subscribers** using the Publish/Subscribe pattern.
