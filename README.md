# 🛡️ SentinelEDR

**SentinelEDR** is a Python-based Endpoint Detection and Response (EDR) platform designed to monitor endpoint activity, identify suspicious processes and network behavior, calculate security risk, and expose security telemetry through a FastAPI-based interface.

The project demonstrates practical cybersecurity engineering concepts including endpoint monitoring, threat detection, automated testing, API development, persistent alert storage, and CI/CD.

---

## 🎯 Project Goals

SentinelEDR was built to demonstrate how a lightweight endpoint security platform can:

* Monitor running processes
* Monitor active network connections
* Detect suspicious endpoint behavior
* Identify potentially malicious processes
* Detect suspicious network activity
* Generate security alerts
* Calculate endpoint risk
* Store security events
* Provide security telemetry through REST APIs
* Automate testing through CI

The project is intended as a **portfolio and learning project for cybersecurity / SOC / blue-team engineering**.

---

## 🚀 Features

### 🔍 Endpoint Monitoring

* Live process enumeration
* Process IDs and usernames
* Process monitoring through `psutil`
* Active network connection monitoring
* Local and remote endpoint information
* Endpoint security telemetry

### 🛡️ Threat Detection

* Suspicious process detection
* Suspicious network activity detection
* Rule-based detection logic
* Alert generation
* Severity classification
* Risk scoring

### 🌐 Security API

Built with **FastAPI** and provides endpoints for:

| Endpoint         | Description                           |
| ---------------- | ------------------------------------- |
| `GET /`          | Endpoint security dashboard           |
| `GET /scan`      | Run endpoint security scan            |
| `GET /processes` | Retrieve running processes            |
| `GET /network`   | Retrieve active network connections   |
| `GET /alerts`    | Retrieve detected security alerts     |
| `GET /docs`      | Interactive Swagger API documentation |

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      Endpoint        │
                         │   Windows System     │
                         └──────────┬───────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
              Process Monitor              Network Monitor
                     │                             │
                     ▼                             ▼
              Process Data                 Network Data
                     │                             │
                     └──────────────┬──────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Detection Engine   │
                         │                      │
                         │ Process Detector     │
                         │ Network Detector     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Risk Scoring      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Alert Storage      │
                         │     SQLite DB        │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
             FastAPI REST API                Security Dashboard
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
                              Security Analyst
```

---

## 🖥️ Security Dashboard

SentinelEDR includes a web-based endpoint security dashboard providing visibility into endpoint telemetry.

The dashboard displays:

* Number of running processes
* Network connections
* Detected threats
* Overall endpoint risk
* Recent alerts
* Live processes
* Network connections
* Endpoint scan status

### Dashboard

![SentinelEDR Dashboard](dashboard.png)

---

## 📡 API Documentation

SentinelEDR exposes its functionality through a REST API using FastAPI.

Interactive Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### API Documentation

![SentinelEDR API Documentation](api-docs.png)

---

## 🔎 API Endpoints

### Dashboard

```http
GET /
```

Returns the SentinelEDR web dashboard.

### Run Security Scan

```http
GET /scan
```

Runs an endpoint security scan and returns the scan results.

### Processes

```http
GET /processes
```

Returns information about running processes.

Example information includes:

```text
PID
Process name
Username
```

### Network

```http
GET /network
```

Returns active network connections detected on the endpoint.

### Alerts

```http
GET /alerts
```

Returns security alerts generated by the detection engine.

### Swagger Documentation

```http
GET /docs
```

Provides interactive API documentation generated by FastAPI.

---

## 🧠 Detection Capabilities

SentinelEDR uses rule-based detection logic to identify suspicious endpoint behavior.

### Process Detection

The process detection engine can evaluate endpoint processes and identify suspicious characteristics.

Example detection categories include:

* Suspicious process names
* Unexpected processes
* Potentially malicious processes
* Elevated or unusual process activity

### Network Detection

The network detection engine analyzes active connections for suspicious characteristics.

Potential detection signals include:

* Suspicious remote connections
* Unexpected network activity
* Unusual connection patterns
* Potentially risky endpoints

---

## ⚠️ Risk Scoring

Detected activity can contribute to an overall endpoint risk assessment.

Example risk levels:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

The risk level can be used to prioritize security investigation.

---

## 🧪 Testing

SentinelEDR includes automated tests using `pytest`.

Run the test suite:

```powershell
py -m pytest -v
```

Tests cover detection functionality and help ensure that changes do not break existing security logic.

Example:

```text
============================= test session starts =============================

tests/test_process_detector.py

PASSED
PASSED
PASSED
PASSED

============================== tests passed ================================
```

---

## 🔄 Continuous Integration

The project uses **GitHub Actions** to automatically run tests when changes are pushed or pull requests are created.

CI performs:

1. Python environment setup
2. Dependency installation
3. Test execution
4. Build validation

Workflow:

```text
Developer
    │
    ▼
Git Push / Pull Request
    │
    ▼
GitHub Actions
    │
    ▼
Install Dependencies
    │
    ▼
Run pytest
    │
    ▼
PASS / FAIL
```

---

## 📁 Project Structure

```text
SentinelEDR/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── app/
│   ├── core/
│   │   ├── network_monitor.py
│   │   ├── process_monitor.py
│   │   └── scanner.py
│   │
│   ├── detectors/
│   │   ├── network_detector.py
│   │   └── process_detector.py
│   │
│   ├── storage/
│   │   └── database.py
│   │
│   ├── templates/
│   │   └── dashboard.html
│   │
│   └── api.py
│
├── tests/
│   ├── __init__.py
│   └── test_process_detector.py
│
├── dashboard.png
├── api-docs.png
├── README.md
└── .gitignore
```

---

## 🛠️ Technology Stack

| Technology     | Purpose                          |
| -------------- | -------------------------------- |
| Python         | Core development                 |
| FastAPI        | REST API                         |
| Uvicorn        | ASGI server                      |
| psutil         | Process and network monitoring   |
| SQLite         | Alert/event storage              |
| Pytest         | Automated testing                |
| Git            | Version control                  |
| GitHub         | Source control and collaboration |
| GitHub Actions | Continuous integration           |
| HTML/CSS       | Security dashboard               |

---

## ▶️ Running SentinelEDR

### 1. Clone the repository

```powershell
git clone https://github.com/Fuzzy4-arch/SentinelEDR.git
```

```powershell
cd SentinelEDR
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install fastapi uvicorn psutil pytest
```

### 5. Start the API server

```powershell
py -m uvicorn app.api:app --reload
```

### 6. Open the dashboard

```text
http://127.0.0.1:8000/
```

### 7. Open API documentation

```text
http://127.0.0.1:8000/docs
```

---

## 🔬 Example Workflow

A typical SentinelEDR scan follows this process:

```text
Endpoint
   │
   ▼
Collect Processes
   │
   ▼
Collect Network Connections
   │
   ▼
Run Detection Rules
   │
   ▼
Generate Alerts
   │
   ▼
Calculate Risk
   │
   ▼
Store Results
   │
   ▼
Expose Through API
   │
   ▼
Display On Dashboard
```

---

## 🔐 Security Considerations

SentinelEDR is designed as a defensive security project.

When deploying or extending the project:

* Do not commit credentials
* Do not commit API keys
* Do not commit authentication tokens
* Do not commit private keys
* Do not expose sensitive endpoint information
* Review screenshots before publishing them
* Use environment variables for sensitive configuration
* Restrict API access when deploying outside localhost

The current implementation is intended primarily for **local testing, education, and portfolio demonstration**.

---

## 🚧 Future Improvements

Potential improvements include:

* Real-time process monitoring
* Real-time network monitoring
* File integrity monitoring
* Windows Event Log integration
* Windows Defender integration
* Process hash collection
* VirusTotal integration
* YARA-based detection
* MITRE ATT&CK technique mapping
* Authentication and authorization
* WebSocket-based live telemetry
* Alert severity improvements
* Advanced risk scoring
* Threat investigation pages
* Endpoint isolation capabilities
* Multi-endpoint monitoring
* Centralized SOC dashboard
* Docker deployment
* Production database support

---

## 🎯 Cybersecurity Skills Demonstrated

This project demonstrates practical experience with:

* Endpoint Detection and Response
* Blue-team security engineering
* Security monitoring
* Threat detection
* Process analysis
* Network monitoring
* Rule-based detection
* Risk assessment
* Security alerting
* REST API development
* Python development
* Database integration
* Automated testing
* Continuous Integration
* Git/GitHub
* Security-focused software architecture

---

## ⚠️ Disclaimer

SentinelEDR is an educational and portfolio project intended for authorized systems and environments.

It should not be considered a replacement for a production-grade EDR solution.

Only use SentinelEDR on systems you own or have explicit permission to monitor.

---

## 👨‍💻 Project

**SentinelEDR — Endpoint Detection and Response Platform**

Built with Python, FastAPI, psutil, SQLite, Pytest, and GitHub Actions.

**Repository:** [Fuzzy4-arch/SentinelEDR](https://github.com/Fuzzy4-arch/SentinelEDR)
