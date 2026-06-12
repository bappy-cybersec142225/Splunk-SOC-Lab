

# Installing Splunk Enterprise on Kali Linux

## Overview

Splunk Enterprise is a powerful Security Information and Event Management (SIEM) platform used for collecting, indexing, searching, analyzing, and visualizing machine-generated data.

Although Splunk is commonly deployed on enterprise Linux servers, it can also be installed on Kali Linux, making it an excellent choice for cybersecurity labs, threat hunting exercises, and detection engineering practice.

This guide walks through the complete installation and initial configuration of Splunk Enterprise on Kali Linux.

---

## Why Install Splunk on Kali Linux?

Many cybersecurity professionals use Kali Linux as a central monitoring server for home lab environments.

Typical use cases include:

* SIEM deployment
* Windows Event Log collection
* Sysmon log analysis
* Detection engineering
* Threat hunting
* Atomic Red Team testing
* Wazuh integration
* SOC analyst training

---

## Home SOC Lab Architecture

```text
Windows Endpoint
├── Sysmon
├── Splunk Universal Forwarder
└── Atomic Red Team

          ↓

Kali Linux
└── Splunk Enterprise

          ↓

Dashboards
Alerts
Threat Hunting
Detection Engineering
```

---

## Learning Objectives

After completing this installation, you will be able to:

* Deploy Splunk Enterprise on Kali Linux
* Configure Splunk as a log collection server
* Receive logs from Windows endpoints
* Create custom indexes
* Build dashboards and visualizations
* Prepare for Detection Engineering labs
* Integrate Sysmon and Atomic Red Team

---

## Prerequisites

Before starting, ensure you have:

### Hardware Requirements

| Component | Recommended         |
| --------- | ------------------- |
| CPU       | 4 Cores             |
| RAM       | 8 GB+               |
| Storage   | 50 GB+ Free Space   |
| Network   | Internet Connection |

### Software Requirements

* Kali Linux (Latest Version)
* Administrative (sudo) privileges
* Splunk Enterprise Debian package (.deb)

---

## Step 1: Download Splunk Enterprise

Visit the official Splunk download page and download the Linux Debian package.

Typical file:

```bash
splunk-10.x.x-linux-amd64.deb
```

Save the package in your Downloads directory.

---

## Step 2: Navigate to the Download Directory

Open a terminal and move to the Downloads folder.

```bash
cd ~/Downloads
```

Verify the package exists:

```bash
ls
```

---

## Step 3: Install Splunk Enterprise

Install the Debian package using dpkg.

```bash
sudo dpkg -i splunk-10.x.x-linux-amd64.deb
```

If dependency issues occur:

```bash
sudo apt --fix-broken install
```

---

## Step 4: Navigate to the Splunk Binary Directory

After installation, Splunk is installed under:

```bash
/opt/splunk
```

Move into the binary directory:

```bash
cd /opt/splunk/bin
```

This directory contains all Splunk management commands.

Examples:

```bash
splunk start
splunk stop
splunk restart
splunk status
```

---

## Step 5: Start Splunk and Accept the License

Run the following command:

```bash
sudo ./splunk start --accept-license
```

During first startup, Splunk will:

1. Display the license agreement
2. Request an administrator username
3. Request an administrator password

Example:

```text
Username: admin
Password: ********
```

Store these credentials securely.

---

## Step 6: Access the Splunk Web Interface

Open a browser and navigate to:

```text
http://<Splunk-IP>:8000
```

Examples:

```text
http://localhost:8000
http://192.168.1.10:8000
```

You should see the Splunk login page.

---

## Step 7: Sign In

Use the credentials created during the first startup process.

After successful authentication, the Splunk Home Dashboard will appear.

At this point, Splunk Enterprise is operational.

---

## Step 8: Configure Receiving Port 9997

To receive logs from Splunk Universal Forwarders:

Navigate to:

```text
Settings → Forwarding and Receiving
```

Select:

```text
Configure Receiving
```

Add TCP Port:

```text
9997
```

Save the configuration.

### Verify Listening Port

Run:

```bash
sudo ss -tulnp | grep 9997
```

Expected output:

```text
LISTEN 0 128 *:9997 *:*
```

This confirms Splunk is ready to receive forwarded logs.

---

## Step 9: Create the Windows Event Log Index

Navigate to:

```text
Settings → Indexes
```

Select:

```text
New Index
```

Create:

```text
wineventlog
```

Purpose:

* Windows Security Logs
* System Logs
* Application Logs
* Sysmon Events

Click Save.

---

## Essential Splunk Management Commands

### Start Splunk

```bash
sudo /opt/splunk/bin/splunk start
```

### Stop Splunk

```bash
sudo /opt/splunk/bin/splunk stop
```

### Restart Splunk

```bash
sudo /opt/splunk/bin/splunk restart
```

### Check Status

```bash
sudo /opt/splunk/bin/splunk status
```

### Enable Auto Start at Boot

```bash
sudo /opt/splunk/bin/splunk enable boot-start
```

---

## Installation Verification Checklist

| Task                         | Status |
| ---------------------------- | ------ |
| Download Splunk Package      | ✅      |
| Install Splunk Enterprise    | ✅      |
| Accept License Agreement     | ✅      |
| Create Administrator Account | ✅      |
| Start Splunk Service         | ✅      |
| Access Web Interface         | ✅      |
| Configure Port 9997          | ✅      |
| Create wineventlog Index     | ✅      |

---

## Next Steps

After installing Splunk Enterprise:

1. Install Splunk Universal Forwarder on Windows
2. Install Sysmon
3. Configure inputs.conf
4. Configure outputs.conf
5. Install Splunk Add-on for Microsoft Windows
6. Install Splunk Add-on for Sysmon
7. Deploy Atomic Red Team
8. Build detection searches and dashboards

These steps will transform the environment into a fully functional SOC and Detection Engineering lab.

---

## Conclusion

Splunk Enterprise is the foundation of this Home SOC Lab. By completing this installation, you now have a centralized SIEM platform capable of collecting, indexing, and analyzing security telemetry from Windows endpoints.

This setup provides an excellent environment for:

* SOC Analyst Training
* Threat Hunting
* Detection Engineering
* Blue Team Operations
* Incident Investigation
* MITRE ATT&CK Mapping
* Cybersecurity Portfolio Development

