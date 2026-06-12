# Atomic Red Team Installation and Detection Validation Guide

## Overview

Atomic Red Team is an open-source security testing framework developed by Red Canary that enables defenders to validate security controls through small, controlled security tests mapped to the MITRE ATT&CK Framework.

Unlike traditional penetration testing tools, Atomic Red Team focuses on individual ATT&CK techniques ("atomics") that can be safely executed in a controlled lab environment to verify logging, monitoring, detection, and alerting capabilities.

In this Splunk SOC Lab, Atomic Red Team is used to generate realistic security telemetry that can be captured by Sysmon, forwarded through Splunk Universal Forwarder, and analyzed in Splunk Enterprise.

---

# Learning Objectives

After completing this guide, you will be able to:

* Understand the purpose of Atomic Red Team
* Install Invoke-AtomicRedTeam
* Deploy Atomic Red Team in a lab environment
* Generate detection telemetry
* Validate Sysmon logging
* Verify Splunk log ingestion
* Map events to the MITRE ATT&CK Framework
* Develop detection engineering use cases

---

# What is Atomic Red Team?

Atomic Red Team provides a collection of small, self-contained tests that simulate adversary behaviors aligned with MITRE ATT&CK techniques.

These tests help security teams answer questions such as:

* Are security logs being generated?
* Is Sysmon capturing the activity?
* Are logs reaching Splunk?
* Are detections triggering correctly?
* Can SOC analysts investigate the activity?

---

# Architecture

```text
MITRE ATT&CK Technique
          ↓
Atomic Test
          ↓
Windows Endpoint
          ↓
Sysmon Event Generation
          ↓
Splunk Universal Forwarder
          ↓
Splunk Enterprise
          ↓
Detection Validation
```

---

# Why SOC Analysts Use Atomic Red Team

## Detection Validation

Confirms whether existing security monitoring controls detect known adversary techniques.

## Detection Engineering

Supports the creation and tuning of:

* Splunk Searches
* Correlation Rules
* Detection Logic
* SOC Playbooks

## Threat Hunting

Provides known activity patterns for testing hunt queries.

## Purple Team Exercises

Creates collaboration opportunities between offensive and defensive teams.

## Audit and Compliance

Demonstrates effectiveness of security monitoring controls during security assessments and audits.

---

# Common ATT&CK Techniques Observed

| MITRE ID | Technique Category                |
| -------- | --------------------------------- |
| T1059    | Command and Scripting Interpreter |
| T1547    | Boot or Logon Autostart Execution |
| T1053    | Scheduled Task                    |
| T1110    | Brute Force                       |
| T1021    | Remote Services                   |
| T1070    | Indicator Removal                 |
| T1562    | Impair Defenses                   |

These techniques are frequently referenced when validating SOC monitoring capabilities.

---

# Lab Environment

```text
Windows 10 Endpoint
├── Sysmon
├── Splunk Universal Forwarder
└── Atomic Red Team

          ↓

Splunk Enterprise
(Kali Linux)

          ↓

Searches
Dashboards
Alerts
Detection Rules
```

---

# Prerequisites

Before installing Atomic Red Team, ensure the following components are operational:

* Splunk Enterprise
* Splunk Receiving Port 9997
* Splunk Universal Forwarder
* Sysmon
* Windows Event Log Collection
* PowerShell 5.1 or later
* Internet Connectivity

---

# Step 1: Review Microsoft Defender Settings

Some Atomic Red Team files may be flagged by endpoint security products because they simulate attacker behavior.

Before downloading the project:

1. Open Windows Security
2. Navigate to:

```text
Virus & Threat Protection
```

3. Review current protection settings
4. Ensure you understand your organization's security policies

> Important: Only perform Atomic Red Team testing inside an isolated lab environment that you own and control.

---

# Step 2: Download Atomic Red Team

Download the project from the official repository:

```text
https://github.com/redcanaryco/atomic-red-team
```

Download the ZIP archive and save it locally.

---

# Step 3: Download Invoke-AtomicRedTeam

Download the PowerShell execution framework:

```text
https://github.com/redcanaryco/invoke-atomicredteam
```

This framework simplifies managing and executing Atomic Red Team tests.

---

# Step 4: Create a Working Directory

Create a dedicated folder:

```text
C:\AtomicRedTeam
```

Example structure:

```text
C:\AtomicRedTeam
│
├── atomic-red-team
└── invoke-atomicredteam
```

---

# Step 5: Extract the Files

Extract both repositories into the working directory.

Verify the Atomic tests directory exists:

```text
atomic-red-team
└── atomics
```

The atomics folder contains all ATT&CK technique definitions.

---

# Step 6: Install Required PowerShell Modules

Open PowerShell as Administrator.

Install required modules:

```powershell
Install-Module -Name Invoke-AtomicRedTeam, powershell-yaml -Scope CurrentUser
```

During installation you may be prompted to:

* Install NuGet Provider
* Trust PowerShell Gallery

Accept the prompts as appropriate.

---

# Step 7: Install Invoke-AtomicRedTeam Framework

Install the framework:

```powershell
IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1')
Install-AtomicRedTeam
```

Successful installation provides access to Atomic Red Team management functions.

---

# Validate Installation

Verify the framework is available:

```powershell
Get-Command *Atomic*
```

You should see available Atomic Red Team commands listed.

---

# Detection Validation Workflow

The primary purpose of Atomic Red Team in this lab is detection validation.

Workflow:

```text
Generate Test Activity
          ↓
Sysmon Captures Events
          ↓
Universal Forwarder Collects Logs
          ↓
Splunk Receives Events
          ↓
SOC Analyst Investigates
          ↓
Detection Logic Improved
```

---

# Verifying Events in Splunk

After generating test activity, search for related Sysmon events:

```spl
index=wineventlog
sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
```

Useful fields:

* EventCode
* ProcessName
* CommandLine
* ParentProcessName
* User
* Computer

---

# MITRE ATT&CK Mapping

Atomic Red Team is directly aligned with the MITRE ATT&CK Framework.

Benefits include:

* ATT&CK coverage analysis
* Detection gap identification
* Security control validation
* Threat hunting exercises
* Purple team operations

---

# Troubleshooting

## PowerShell Module Installation Fails

Verify:

```powershell
Get-ExecutionPolicy
```

Check internet connectivity and PowerShell Gallery access.

---

## No Sysmon Events Generated

Verify Sysmon is running:

```cmd
sc query Sysmon64
```

Expected:

```text
STATE : 4 RUNNING
```

---

## No Events in Splunk

Verify:

* Port 9997 is listening
* Universal Forwarder is connected
* inputs.conf is configured correctly
* Sysmon logs exist locally

---

## Verify Forwarder Status

```cmd
splunk.exe list forward-server
```

Expected:

```text
Active forwards:
<splunk-server>:9997
```

---

# Skills Demonstrated

This lab helps develop practical skills in:

* Security Operations Center (SOC) Monitoring
* Threat Hunting
* Detection Engineering
* Incident Response
* MITRE ATT&CK Mapping
* Security Analytics
* Security Control Validation
* IT Security Auditing

---

# Conclusion

Atomic Red Team is a powerful validation framework that bridges the gap between security monitoring and real-world adversary behavior. When combined with Sysmon, Splunk Universal Forwarder, and Splunk Enterprise, it creates a realistic SOC training environment that supports detection engineering, threat hunting, incident response, and security monitoring.

By integrating Atomic Red Team into this Splunk SOC Lab, defenders can continuously test and improve their ability to detect, investigate, and respond to security events in a controlled environment.

