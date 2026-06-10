
# 🛡️ Splunk SOC Detection Engineering Lab

### Splunk + Sysmon + Atomic Red Team (MITRE ATT&CK Based)

---

## 📌 Overview

The **Splunk SOC Detection Engineering Lab** is a hands-on cybersecurity project designed to simulate a real-world **Security Operations Center (SOC)** environment.

It demonstrates how to:

* Collect and analyze Windows security telemetry using **Sysmon**
* Forward logs using **Splunk Universal Forwarder**
* Ingest and analyze data in **Splunk Enterprise**
* Simulate adversary techniques using **Atomic Red Team**
* Build detection rules mapped to **MITRE ATT&CK**
* Create SOC-style dashboards for threat monitoring

This project is designed for **SOC Analysts, IT Auditors, and Detection Engineers** seeking practical SIEM experience.

---

## 🎯 Objectives

* Build a complete SIEM lab environment
* Collect and analyze Windows event logs
* Deploy Sysmon for advanced endpoint telemetry
* Simulate real-world cyberattacks
* Develop SPL-based detection queries
* Map detections to MITRE ATT&CK framework
* Create SOC dashboards for monitoring and analysis

---

## 🏗️ Lab Architecture

```
Kali Linux (Attacker)
        │
        │ Attack Simulation (Atomic Red Team)
        ▼
Windows 10 (Victim Endpoint)
        │
        │ Sysmon + Windows Event Logs
        ▼
Splunk Universal Forwarder
        │
        ▼
Splunk Enterprise (Ubuntu Server)
```

---

## 🖥️ Lab Environment

| System        | Role                          | IP Address   |
| ------------- | ----------------------------- | ------------ |
| Ubuntu Server | Splunk Enterprise SIEM        | 192.168.1.10 |
| Windows 10    | Victim Endpoint (Sysmon + UF) | 192.168.1.20 |
| Kali Linux    | Attack Simulation Machine     | 192.168.1.30 |

---

## ⚙️ Technologies Used

* 🟠 Splunk Enterprise
* 🟢 Splunk Universal Forwarder
* 🔵 Sysmon (Sysinternals)
* 🔴 Atomic Red Team
* 🧠 MITRE ATT&CK Framework
* 💻 Windows Event Logging
* 🐧 Ubuntu Server
* 🐉 Kali Linux

---

## 📥 Installation Guide

### 1. Install Splunk Enterprise (Ubuntu)

```bash
sudo apt update && sudo apt upgrade -y
sudo dpkg -i splunk*.deb
```

Start Splunk:

```bash
sudo /opt/splunk/bin/splunk start --accept-license
```

Enable boot start:

```bash
sudo /opt/splunk/bin/splunk enable boot-start
```

Access Splunk:

```
http://<SERVER-IP>:8000
```

---

### 2. Enable Splunk Receiving Port

In Splunk UI:

```
Settings → Forwarding and Receiving → Configure Receiving → Add Port 9997
```

---

### 3. Install Universal Forwarder (Windows)

Configure `outputs.conf`:

```ini
[tcpout]
defaultGroup=default-autolb-group

[tcpout:default-autolb-group]
server=192.168.1.10:9997
```

---

### 4. Configure Log Collection (`inputs.conf`)

```ini
[WinEventLog://Application]
disabled=0
index=wineventlog

[WinEventLog://Security]
disabled=0
index=wineventlog

[WinEventLog://System]
disabled=0
index=wineventlog

[WinEventLog://Microsoft-Windows-Sysmon/Operational]
disabled=0
index=wineventlog
```

---

### 5. Install Sysmon

Download Sysmon from Sysinternals:

```bash
sysmon64.exe -i sysmonconfig.xml
```

Verify:

```powershell
Get-Service Sysmon64
```

---

## 📊 Splunk Index Configuration

Create index:

```
wineventlog
```

---

## ⚔️ Attack Simulation (Atomic Red Team)

Install framework:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
Install-Module Invoke-AtomicRedTeam
```

---

### Run Simulations

#### PowerShell Execution (T1059.001)

```powershell
Invoke-AtomicTest T1059.001
```

#### System Discovery (T1082)

```powershell
Invoke-AtomicTest T1082
```

#### Credential Access (T1003)

```powershell
Invoke-AtomicTest T1003
```

---

## 🔍 Detection Engineering (Splunk SPL)

### 1. PowerShell Execution Detection

```spl
index=wineventlog EventCode=1 Image="*powershell.exe*"
| table _time host User CommandLine ParentImage
```

---

### 2. Encoded PowerShell Commands

```spl
index=wineventlog CommandLine="*-enc*"
```

---

### 3. Failed Login Attempts

```spl
index=wineventlog EventCode=4625
| stats count by Account_Name, host, _time
```

---

### 4. Sysmon Process Creation Monitoring

```spl
index=wineventlog EventCode=1
| stats count by Image, ParentImage, host
```

---

## 📊 Dashboards

The following SOC dashboards were created:

* 🛡️ Security Overview Dashboard
* ⚡ PowerShell Activity Monitoring
* 🚨 Failed Login Attempts Analysis
* 🧾 Sysmon Event Timeline
* 🎯 Top MITRE ATT&CK Techniques

---

## 🧠 MITRE ATT&CK Mapping

| Detection            | Technique ID | Technique Name                  |
| -------------------- | ------------ | ------------------------------- |
| PowerShell Execution | T1059.001    | Command & Scripting Interpreter |
| System Discovery     | T1082        | System Information Discovery    |
| Credential Access    | T1003        | OS Credential Dumping           |
| Brute Force Attempts | T1110        | Brute Force                     |

---

## 📸 Screenshots

> Add screenshots in `/screenshots/`

* Splunk Dashboard Overview
* Sysmon Event Logs
* Atomic Red Team Execution
* Detection Results

---

## 📚 Key Features

* Real-world SIEM architecture simulation
* Endpoint visibility using Sysmon
* Attack emulation using Atomic Red Team
* Custom SPL detection rules
* MITRE ATT&CK-based mapping
* SOC-style dashboards

---

## 💡 Lessons Learned

* How SIEM systems ingest and normalize logs
* Importance of endpoint telemetry (Sysmon)
* Writing effective detection queries in SPL
* Mapping logs to MITRE ATT&CK techniques
* SOC investigation workflows
* Attack simulation for validation of detections

---

## 🚀 Future Improvements

* Add Wazuh integration
* Implement threat intelligence feeds
* Add alerting & correlation rules
* Build incident response playbooks
* Integrate ELK Stack comparison

---

## 👤 Author

**Bappy Sharma**
CISA | FMVA | IT Audit & Cybersecurity Professional
SOC | SIEM | Detection Engineering | IT Risk & Controls

---

## 📌 Disclaimer

This project is for **educational and cybersecurity research purposes only**. All simulations are performed in a controlled lab environment.


