

# Installing Splunk Universal Forwarder on Windows

## Overview

The Splunk Universal Forwarder (UF) is a lightweight agent that collects logs from Windows systems and forwards them to a Splunk Enterprise server for indexing, searching, and analysis.

In this lab, the Windows victim machine acts as a monitored endpoint, sending Windows Event Logs and Sysmon telemetry to the Splunk Enterprise server running on Kali Linux.

---

# Lab Architecture

```text
Windows 10 Endpoint
├── Splunk Universal Forwarder
├── Sysmon
└── Atomic Red Team

          ↓ TCP 9997

Splunk Enterprise Server
(Kali Linux)

          ↓

Searches • Dashboards • Alerts • Detections
```

---

# Learning Objectives

After completing this section, you will be able to:

* Install Splunk Universal Forwarder
* Configure log forwarding
* Collect Windows Event Logs
* Forward Sysmon telemetry
* Configure inputs.conf
* Configure outputs.conf
* Verify communication with Splunk Enterprise
* Troubleshoot forwarding issues

---

# Step 1: Download Splunk Universal Forwarder

Download the appropriate Windows MSI package from the Splunk Downloads page.

Recommended Version:

```text
Splunk Universal Forwarder 10.x
Windows x64 MSI
```

Save the installer to the Windows machine.

---

# Step 2: Install Splunk Universal Forwarder

Launch the installer by double-clicking the MSI package.

Accept:

☑ I Accept the License Agreement

Click Next.

---

# Step 3: Select Data to Forward

Under:

### Windows Event Logs

Select:

* Application
* Security
* System

### Performance Monitor

Select all available options.

These logs provide the foundational telemetry required for security monitoring and threat detection.

Click Next.

---

# Step 4: Configure Splunk Credentials

Create administrative credentials for the Universal Forwarder.

Example:

```text
Username: admin
Password: ********
```

Click Next.

---

# Step 5: Configure Receiving Indexer

Specify the Splunk Enterprise server.

Example:

```text
Hostname or IP:
192.168.1.10

Receiving Port:
9997
```

Where:

| Parameter   | Description              |
| ----------- | ------------------------ |
| Hostname/IP | Splunk Enterprise Server |
| Port        | Splunk Receiving Port    |

Click Next → Install.

After installation completes, click Finish.

---

# Step 6: Verify the SplunkForwarder Service

Open Services:

```text
Start Menu → Services
```

Locate:

```text
SplunkForwarder
```

Restart the service.

---

## Verify Service Status

Open Command Prompt as Administrator:

```cmd
sc query SplunkForwarder
```

Expected:

```text
STATE : 4 RUNNING
```

This confirms the forwarder is operational.

---

# Step 7: Configure outputs.conf

Navigate to:

```text
C:\Program Files\SplunkUniversalForwarder\etc\system\local\
```

Create:

```text
outputs.conf
```

Add:

```ini
[tcpout]
defaultGroup = default-autolb-group

[tcpout:default-autolb-group]
server = 192.168.1.10:9997

[tcpout-server://192.168.1.10:9997]
```

---

## outputs.conf Explained

### [tcpout]

Defines outbound forwarding configuration.

```ini
[tcpout]
defaultGroup = default-autolb-group
```

Sets the default forwarding group.

---

### [tcpout:default-autolb-group]

```ini
[tcpout:default-autolb-group]
server = 192.168.1.10:9997
```

Specifies the destination Splunk Enterprise server.

---

### [tcpout-server://192.168.1.10:9997]

```ini
[tcpout-server://192.168.1.10:9997]
```

Creates a dedicated forwarding target.

---

# Step 8: Configure inputs.conf

Navigate to:

```text
C:\Program Files\SplunkUniversalForwarder\etc\system\local\
```

Create:

```text
inputs.conf
```

Add:

```ini
[WinEventLog://Application]
disabled = 0
index = wineventlog

[WinEventLog://Security]
disabled = 0
index = wineventlog

[WinEventLog://System]
disabled = 0
index = wineventlog

[WinEventLog://Microsoft-Windows-Sysmon/Operational]
disabled = 0
index = wineventlog
renderXml = true
```

Save the file.

---

# inputs.conf Explained

### Application Logs

```ini
[WinEventLog://Application]
```

Collects application-related events.

---

### Security Logs

```ini
[WinEventLog://Security]
```

Collects:

* Logon events
* Account activity
* Authentication failures
* Privilege escalation attempts

---

### System Logs

```ini
[WinEventLog://System]
```

Collects operating system events.

---

### Sysmon Logs

```ini
[WinEventLog://Microsoft-Windows-Sysmon/Operational]
```

Collects advanced endpoint telemetry.

Examples:

* Process Creation
* Network Connections
* File Creation
* Registry Modifications
* PowerShell Activity

---

### renderXml = true

```ini
renderXml = true
```

Ensures Sysmon events are forwarded in XML format for accurate field extraction and parsing.

---

# Step 9: Restart Splunk Universal Forwarder

Open Command Prompt as Administrator:

```cmd
net stop SplunkForwarder
net start SplunkForwarder
```

Or:

```powershell
Restart-Service SplunkForwarder
```

Verify:

```powershell
Get-Service SplunkForwarder
```

Expected:

```text
Status : Running
```

---

# Step 10: Verify Forwarding Configuration

Check configured forward servers:

```cmd
"C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe" list forward-server
```

Expected:

```text
Active forwards:
192.168.1.10:9997
```

---

# Install Splunk Add-on for Microsoft Windows

## Purpose

The Splunk Add-on for Microsoft Windows provides:

* Windows field extractions
* Event categorization
* CIM normalization
* Improved searching
* Dashboard compatibility

---

## Benefits

* Normalized field names
* Better search performance
* Security use-case support
* Enterprise Security compatibility

Install into:

```bash
/opt/splunk/etc/apps/
```

Restart Splunk after installation.

---

# Install Splunk Add-on for Sysmon

## Purpose

The Sysmon Add-on provides:

* Sysmon field extractions
* Event parsing
* CIM mapping
* Detection engineering support

Install into:

```bash
/opt/splunk/etc/apps/
```

Restart Splunk:

```bash
sudo /opt/splunk/bin/splunk restart
```

---

# Validation Checklist

| Task                     | Status |
| ------------------------ | ------ |
| Install UF               | ✅      |
| Configure outputs.conf   | ✅      |
| Configure inputs.conf    | ✅      |
| Service Running          | ✅      |
| Port 9997 Reachable      | ✅      |
| Events Visible in Splunk | ✅      |
| Sysmon Logs Ingested     | ✅      |

---

# Troubleshooting Guide

## Forwarder Not Running

Check:

```cmd
sc query SplunkForwarder
```

Expected:

```text
STATE : 4 RUNNING
```

---

## No Events Appearing in Splunk

Check connectivity:

```cmd
netstat -ano | findstr 9997
```

Verify:

* Splunk server is online
* Port 9997 is listening
* Firewall allows traffic

---

## Verify Splunk Server Listening

On Kali:

```bash
sudo netstat -tulnp | grep 9997
```

Expected:

```text
LISTEN 0 128 :::9997
```

---

## Forward Server Status

```bash
sudo /opt/splunk/bin/splunk list forward-server
```

Verify connection status.

---

## Review Splunk Logs

```bash
sudo tail -f /opt/splunk/var/log/splunk/splunkd.log
```

Useful for:

* Connection issues
* Parsing errors
* Authentication failures

---

## Sysmon Events Missing

Verify Sysmon installation:

```cmd
sysmon64 -c
```

Check:

```text
Applications and Services Logs
→ Microsoft
→ Windows
→ Sysmon
→ Operational
```

---

## Firewall Issues

Allow:

| Port | Purpose         |
| ---- | --------------- |
| 9997 | Log Forwarding  |
| 8000 | Web Interface   |
| 8089 | Management Port |

---

# Essential Splunk Commands

## Splunk Enterprise

```bash
splunk start
splunk stop
splunk restart
splunk status
```

## Forward Server Commands

```bash
splunk list forward-server
splunk add forward-server 192.168.1.10:9997
```

---

# Conclusion

At this stage, the Windows endpoint is successfully forwarding Windows Event Logs and Sysmon telemetry to Splunk Enterprise. This forms the foundation of a practical SOC lab and prepares the environment for Atomic Red Team attack simulations, threat hunting, dashboard creation, and detection engineering exercises.

