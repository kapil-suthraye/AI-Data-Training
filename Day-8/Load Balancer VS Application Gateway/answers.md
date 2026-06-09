# Azure Networking Decision Matrix – Load Balancer vs Application Gateway

## Overview

| # | Requirement | Recommended Service | Reason |
|---|-------------|--------------------|--------|
| 1 | Patient Web Portal | Application Gateway | HTTP/HTTPS web application requiring Layer 7 routing, SSL termination, WAF protection, and URL-based routing |
| 2 | Clinical API (Internal) | Application Gateway | REST API traffic over HTTP/HTTPS requiring API routing, SSL offloading, authentication integration, and security controls |
| 3 | DICOM Image Streaming | Load Balancer | High-throughput TCP traffic, non-HTTP protocol, requires Layer 4 load balancing |
| 4 | Authentication Service | Application Gateway | Web-based authentication endpoints require SSL termination, WAF, and secure Layer 7 routing |
| 5 | Legacy SOAP Lab Service | Application Gateway | SOAP uses HTTP/HTTPS and benefits from Layer 7 routing, SSL offload, and security inspection |
| 6 | Admin Dashboard | Application Gateway | Sensitive web application requiring WAF, SSL termination, path-based routing, and enhanced security |

---

# Detailed Explanation

## 1. Patient Web Portal

### Recommended: Application Gateway

### Why?
A patient portal is a browser-based application accessed via HTTP/HTTPS.

Typical requirements:

- SSL/TLS termination
- Web Application Firewall (WAF)
- URL-based routing
- Session affinity
- Protection against OWASP attacks
- HTTPS redirection

### Example Flow

```text
Internet
    |
Application Gateway + WAF
    |
Web Servers
```

### Why Not Load Balancer?

Azure Load Balancer works only at Layer 4 (TCP/UDP) and cannot:

- Inspect URLs
- Perform HTTPS redirection
- Provide WAF protection
- Route based on paths

---

## 2. Clinical API (Internal)

### Recommended: Application Gateway

### Why?

Clinical APIs are generally REST APIs exposed over HTTP/HTTPS.

Requirements:

- API endpoint routing
- SSL offloading
- JWT/OAuth authentication integration
- WAF protection
- Header inspection

### Example

```text
/api/patients
/api/appointments
/api/reports
```

Application Gateway can route requests to different backend pools based on URL paths.

### Why Not Load Balancer?

Load Balancer only forwards TCP packets and cannot route based on API endpoints.

---

## 3. DICOM Image Streaming

### Recommended: Load Balancer

### Why?

DICOM communication typically uses:

- TCP Port 104
- TCP Port 11112
- Non-HTTP protocol

Medical imaging systems:

- PACS
- CT Scanners
- MRI Machines
- Radiology Workstations

communicate using raw TCP connections.

### Example Flow

```text
MRI Scanner
      |
Azure Load Balancer
      |
PACS Servers
```

### Why Not Application Gateway?

Application Gateway only supports:

- HTTP
- HTTPS
- WebSocket

It cannot understand or process DICOM traffic.

---

## 4. Authentication Service

### Recommended: Application Gateway

### Why?

Authentication services expose endpoints such as:

```text
/login
/logout
/token
/oauth
/saml
```

Requirements:

- SSL termination
- WAF protection
- Cookie-based session affinity
- Authentication endpoint routing

### Example Flow

```text
Users
   |
Application Gateway + WAF
   |
Identity Service
```

### Benefits

- Protection against credential attacks
- Centralized SSL certificate management
- Secure authentication traffic inspection

---

## 5. Legacy SOAP Lab Service

### Recommended: Application Gateway

### Why?

SOAP services typically run on:

```text
HTTP
HTTPS
```

Example:

```text
https://lab.company.com/LabService.svc
```

Requirements:

- SSL offloading
- Layer 7 routing
- Header inspection
- Security filtering

### Example Flow

```text
Lab Systems
      |
Application Gateway
      |
SOAP Services
```

### Why Not Load Balancer?

Although Load Balancer can forward TCP traffic, it lacks:

- URL routing
- SSL termination
- Web application security

---

## 6. Admin Dashboard

### Recommended: Application Gateway

### Why?

Admin dashboards contain highly sensitive functionality such as:

- User management
- Audit logs
- Patient administration
- Configuration management

Requirements:

- WAF
- HTTPS enforcement
- URL filtering
- Session affinity
- SSL offloading

### Example

```text
/admin
/reports
/settings
```

Application Gateway can route and secure these paths independently.

### Example Flow

```text
Administrators
       |
Application Gateway + WAF
       |
Admin Portal
```

---

# Final Architecture Summary

| Service Type | Recommended Azure Service |
|--------------|--------------------------|
| Web Applications | Application Gateway |
| REST APIs | Application Gateway |
| SOAP Services | Application Gateway |
| Authentication Services | Application Gateway |
| TCP/UDP Services | Load Balancer |
| DICOM Streaming | Load Balancer |

---

# Final Answers

| Requirement | Service |
|------------|---------|
| Patient Web Portal | Application Gateway |
| Clinical API (Internal) | Application Gateway |
| DICOM Image Streaming | Load Balancer |
| Authentication Service | Application Gateway |
| Legacy SOAP Lab Service | Application Gateway |
| Admin Dashboard | Application Gateway |

## Rule of Thumb

**Use Application Gateway when traffic is HTTP/HTTPS and requires Layer 7 intelligence (routing, WAF, SSL termination).**

**Use Load Balancer when traffic is TCP/UDP or non-HTTP protocols such as DICOM, database traffic, FTP, or custom protocols.**
