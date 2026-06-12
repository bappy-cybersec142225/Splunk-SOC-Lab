# Splunk-SOC-Lab ⭐

## Practical SIEM & Detection Engineering Lab

A hands-on Security Information and Event Management (SIEM) lab built using Splunk Enterprise, Splunk Universal Forwarder, Sysmon, and Atomic Red Team. This project demonstrates end-to-end log collection, attack simulation, detection engineering, and security monitoring in a Home SOC environment.

Designed for SOC Analysts, Blue Teamers, IT Auditors, Cybersecurity Professionals, and Detection Engineers seeking practical experience with enterprise-grade security monitoring.

---

## Project Objectives

This lab focuses on building a realistic Security Operations Center (SOC) environment to:

* Deploy and configure Splunk Enterprise
* Forward Windows Event Logs using Splunk Universal Forwarder
* Implement Sysmon for enhanced endpoint telemetry
* Simulate adversary techniques using Atomic Red Team
* Analyze and investigate security events
* Develop detection engineering skills
* Practice Blue Team monitoring and threat hunting
* Map detections to the MITRE ATT&CK Framework

---

## Key Learning Outcomes

### Splunk Infrastructure

* Install and configure Splunk Enterprise
* Configure Splunk Receiving Port (9997)
* Create and manage custom indexes
* Configure data inputs and forwarding

### Endpoint Monitoring

* Install Splunk Universal Forwarder on Windows
* Configure `inputs.conf`
* Configure `outputs.conf`
* Enable Windows Event Log collection
* Configure Windows Firewall rules
* Run UF service using Local System Account

### Advanced Telemetry

* Deploy Sysmon
* Implement SwiftOnSecurity Sysmon Configuration
* Install Splunk Add-on for Microsoft Windows
* Install Splunk Add-on for Sysmon

### Detection Engineering

* Generate attack telemetry using Atomic Red Team
* Validate log ingestion
* Search and analyze security events
* Create dashboards and visualizations
* Build detection use cases

---

## Lab Architecture

### Components

* Host Machine
* Splunk Enterprise Server
* Windows 10 Endpoint
* Splunk Universal Forwarder
* Sysmon
* Kali Linux Attacker Machine
* Atomic Red Team

### Example Network Layout

```text

+----------------------+
|      Host Machine    |
+----------+-----------+
           |
    Virtual Network
           |
+----------+-----------+
|   Splunk Enterprise  |
|     192.168.1.10     |
+----------+-----------+
           |
+----------+-----------+
|   Windows 10 Client  |
| Sysmon + UF Installed|
|     192.168.1.20     |
+----------+-----------+
           |
+----------+-----------+
|    Kali Linux VM     |
|     192.168.1.30     |
+----------------------+
```

---

## Technologies Used

| Technology                    | Purpose               |
| ----------------------------- | --------------------- |
| Splunk Enterprise             | SIEM Platform         |
| Splunk Universal Forwarder    | Log Collection        |
| Sysmon                        | Endpoint Telemetry    |
| SwiftOnSecurity Sysmon Config | Advanced Logging      |
| Splunk TA for Windows         | Windows Event Parsing |
| Splunk TA for Sysmon          | Sysmon Event Parsing  |
| Atomic Red Team               | Attack Simulation     |
| MITRE ATT&CK                  | Threat Mapping        |
| Windows Event Logging         | Security Monitoring   |

---

## Lab Workflow

1. Install Splunk Enterprise
2. Configure Receiving Port 9997
3. Create `wineventlog` Index
4. Install Splunk Universal Forwarder
5. Configure Forwarding
6. Install Sysmon
7. Deploy Splunk Add-ons
8. Generate Attack Activity with Atomic Red Team
9. Validate Log Ingestion
10. Create Searches, Dashboards, and Detections

---

## Skills Demonstrated

* SIEM Administration
* Security Monitoring
* Threat Detection
* Detection Engineering
* Log Management
* Incident Investigation
* MITRE ATT&CK Mapping
* Blue Team Operations
* Security Analytics
* Threat Hunting

---

## Ideal For

* SOC Analyst Preparation
* Blue Team Training
* Cybersecurity Portfolio Projects
* IT Audit Professionals
* Detection Engineers
* Security Researchers
* Students Learning SIEM Technologies

---

## Future Enhancements

* Splunk Enterprise Security (ES)
* Wazuh Integration
* Sigma Rule Conversion
* Detection-as-Code
* Automated Alerting
* Threat Intelligence Integration
* SOAR Playbooks
* Incident Response Scenarios

---

## Author

**Bappy Sharma**

* CISA | FMVA | CBCA
* Banking Professional
* IT Audit & Cybersecurity Enthusiast
* Detection Engineering Learner

---

## Disclaimer

This lab environment is intended for educational and research purposes only. All attack simulations are performed within an isolated laboratory environment.

