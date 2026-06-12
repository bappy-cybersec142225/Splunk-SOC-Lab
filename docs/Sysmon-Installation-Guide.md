# Sysmon Installation and Configuration Guide

## Overview

Sysmon (System Monitor) is a free Windows system service and device driver from Microsoft's Sysinternals Suite that provides detailed visibility into endpoint activity. It extends native Windows logging by generating rich telemetry that is invaluable for threat hunting, incident response, detection engineering, and SOC operations.

Unlike standard Windows Event Logs, Sysmon captures detailed information about:

* Process creation
* Network connections
* File creation and modification
* Registry changes
* Driver loading
* DLL loading
* PowerShell activity
* Process injection
* DNS queries
* File hashes

When integrated with Splunk Enterprise, Sysmon becomes one of the most valuable sources of security telemetry in a Home SOC Lab.

---

# Why Use Sysmon?

Windows Event Logs alone often do not provide sufficient visibility for modern threat detection.

Sysmon enhances endpoint monitoring by:

* Recording detailed process execution
* Tracking network communications
* Monitoring registry modifications
* Capturing file creation events
* Supporting advanced threat hunting
* Providing telemetry for MITRE ATT&CK detections

Many SOC analysts and detection engineers rely on Sysmon as a foundational endpoint visibility tool.

---

# Lab Architecture

```text
Windows 10 Endpoint
├── Sysmon
├── Splunk Universal Forwarder
└── Atomic Red Team

          ↓

Splunk Enterprise
(Kali Linux)

          ↓

Searches • Dashboards • Detections
```

---

# Learning Objectives

After completing this guide, you will be able to:

* Install Sysmon
* Deploy a production-quality Sysmon configuration
* Validate Sysmon event generation
* Forward Sysmon logs to Splunk
* Monitor endpoint telemetry
* Prepare for Atomic Red Team attack simulations

---

# Prerequisites

Before installing Sysmon, download the following components.

## Required Files

### Sysmon Installer

Download Sysmon from the Microsoft Sysinternals Suite.

Files included:

```text
Sysmon.exe
Sysmon64.exe
```

Use:

```text
Sysmon64.exe
```

for 64-bit Windows systems.

---

## Sysmon Configuration File

Sysmon requires an XML configuration file.

Popular options include:

### Olaf Hartong Sysmon Modular

Provides:

* Well-maintained configuration
* Modular deployment
* ATT&CK-aligned monitoring

### SwiftOnSecurity Sysmon Configuration

One of the most widely used Sysmon configurations for SOC and lab environments.

Provides:

* Reduced noise
* Useful security telemetry
* Threat hunting visibility

Recommended for this project:

```text
sysmonconfig-export.xml
```

---

# Prepare Installation Files

Create a working directory:

```text
C:\Sysmon
```

Place the following files inside:

```text
C:\Sysmon
│
├── Sysmon64.exe
└── sysmonconfig.xml
```

---

# Installing Sysmon

## Silent Installation with Configuration File

Open Command Prompt as Administrator.

Navigate to:

```cmd
cd C:\Sysmon
```

Install Sysmon:

```cmd
Sysmon64.exe -accepteula -i sysmonconfig.xml
```

### Command Explanation

| Parameter        | Description                                 |
| ---------------- | ------------------------------------------- |
| -accepteula      | Automatically accepts the Sysinternals EULA |
| -i               | Installs Sysmon                             |
| sysmonconfig.xml | Loads the selected configuration            |

Expected result:

```text
Sysmon installed.
SysmonDrv installed.
Sysmon service started.
```

---

# Verify Sysmon Installation

## Check Service Status

Run:

```cmd
sc query Sysmon64
```

Expected:

```text
STATE : 4 RUNNING
```

This confirms Sysmon is active.

---

# View Sysmon Configuration

## Display Configuration Schema

```cmd
Sysmon64.exe -s
```

Purpose:

* Shows all supported Sysmon event types
* Displays XML schema information

---

## Display Active Configuration

```cmd
Sysmon64.exe -c
```

Purpose:

* Displays the currently loaded configuration
* Confirms rules were applied successfully

---

# Validate Sysmon Logging

Open:

```text
Event Viewer
```

Navigate to:

```text
Applications and Services Logs
    └── Microsoft
         └── Windows
              └── Sysmon
                   └── Operational
```

You should immediately see events being generated.

---

# Common Sysmon Event IDs

| Event ID | Description        |
| -------- | ------------------ |
| 1        | Process Creation   |
| 3        | Network Connection |
| 7        | Image Loaded       |
| 8        | CreateRemoteThread |
| 11       | File Creation      |
| 13       | Registry Value Set |
| 22       | DNS Query          |
| 25       | Process Tampering  |

These events provide the telemetry used for threat detection.

---

# View Sysmon Events with PowerShell

Display the first 10 Sysmon events:

```powershell
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" |
Select-Object -First 10
```

Expected output:

```text
TimeCreated
Id
ProviderName
Message
```

This confirms Sysmon is successfully generating events.

---

# Integrating Sysmon with Splunk

Ensure the following stanza exists inside the Universal Forwarder inputs.conf:

```ini
[WinEventLog://Microsoft-Windows-Sysmon/Operational]
disabled = 0
index = wineventlog
renderXml = true
```

### Why renderXml = true?

```ini
renderXml = true
```

Benefits:

* Preserves complete event structure
* Improves field extraction
* Enables Splunk TA for Sysmon parsing
* Supports CIM normalization

---

# Verify Sysmon Events in Splunk

Search:

```spl
index=wineventlog sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"
```

Expected result:

```text
Sysmon Event ID 1
Process Creation
```

If events appear, Sysmon telemetry is successfully reaching Splunk.

---

# Updating Sysmon Configuration

To update an existing configuration:

```cmd
Sysmon64.exe -c sysmonconfig.xml
```

Expected:

```text
Configuration updated.
```

No reboot required.

---

# Uninstall Sysmon

If necessary:

```cmd
Sysmon64.exe -u
```

Expected:

```text
Sysmon service stopped.
Sysmon removed.
```

---

# Troubleshooting Guide

## No Sysmon Events Generated

Verify service status:

```cmd
sc query Sysmon64
```

If stopped:

```cmd
net start Sysmon64
```

---

## Sysmon Log Not Visible

Check:

```text
Event Viewer
→ Applications and Services Logs
→ Microsoft
→ Windows
→ Sysmon
→ Operational
```

If missing, reinstall Sysmon.

---

## No Sysmon Events in Splunk

Verify:

```cmd
splunk.exe list forward-server
```

Confirm:

* Forwarder connected
* inputs.conf configured
* Splunk receiving port active

---

## Verify Splunk Receiving Port

On Kali Linux:

```bash
sudo netstat -tulnp | grep 9997
```

Expected:

```text
LISTEN :::9997
```

---

## Review Splunk Logs

```bash
sudo tail -f /opt/splunk/var/log/splunk/splunkd.log
```

Check for:

* Parsing errors
* Connection failures
* Authentication issues

---

# Detection Engineering Use Cases

Sysmon enables detection of:

* PowerShell attacks
* Credential dumping
* Process injection
* Lateral movement
* Malicious network connections
* Persistence mechanisms
* Living-off-the-land techniques
* Atomic Red Team simulations

These detections form the foundation of a modern SOC monitoring environment.

---

# Conclusion

Sysmon is one of the most important telemetry sources in any security monitoring environment. By combining Sysmon, Splunk Universal Forwarder, and Splunk Enterprise, you create a powerful detection engineering lab capable of monitoring endpoint activity, validating attack simulations, and supporting advanced threat hunting exercises.

At this stage, your Windows endpoint is generating high-quality telemetry that will be used throughout the remainder of the Splunk-SOC-Lab project.

