Splunk Enterprise Installation & Configuration Guide (Kali Linux)

# Step 1: Download Splunk Enterprise
Visit the official Splunk download page:
[Splunk Enterprise Download Page](https://www.splunk.com/en_us/download/splunk-enterprise.html?utm_source=chatgpt.com)
Download the **Linux .deb package**.
Example file:
splunk-10.4.0-linux-amd64.deb

# Step 2: Open Terminal
cd ~/Downloads
ls
Expected Output:
splunk-10.4.0-linux-amd64.deb

# Step 3: Install Splunk Enterprise

Run:
sudo dpkg -i splunk-10.x.x-linux-amd64.deb

If dependency issues appear:
sudo apt --fix-broken install -y

Then reinstall:

sudo dpkg -i splunk-10.4.0-linux-amd64.deb

Splunk installation successful

# Step 4: Verify Installation
Check installation directory:
ls /opt/splunk
Expected:

bin
etc
var
share

# Step 5: Start Splunk
Move to Splunk bin directory:
cd /opt/splunk/bin
Start Splunk:
sudo ./splunk start


# Step 6: Accept License

First startup asks:
sudo /opt/splunk/bin/splunk start --accept-license
Do you agree with this license? [y/n]
y
Press Enter.

# Step 7: Create Admin Account

Splunk will request:

Create administrator username:

Example:
admin
Then:
Create new password:

Example:
CyberLab@2026

# Step 8: Enable Auto Start
Configure Splunk to start automatically after reboot:
sudo /opt/splunk/bin/splunk enable boot-start
Enter:
y

# Step 9: Check Splunk Status
sudo /opt/splunk/bin/splunk status

Expected:
splunkd is running

# Step 10: Open Splunk Web Interface

Check Kali IP:
ip a


Example:
192.168.1.100

Open browser:
http://localhost:8000

# Step 11: Login
Username: admin
Password: YourPassword

# Step 12: Verify Splunk Version

From terminal:

sudo /opt/splunk/bin/splunk version

Expected:
Splunk Enterprise 10.4.0

# Essential Management Commands

### Start Splunk
sudo /opt/splunk/bin/splunk start

### Stop Splunk
sudo /opt/splunk/bin/splunk stop

### Restart Splunk
sudo /opt/splunk/bin/splunk restart

### Check Status
sudo /opt/splunk/bin/splunk status

# Verification Checklist

| Task                      | Status |
| ------------------------- | ------ |
| Download .deb file        | ✅      |
| Install Splunk Enterprise | ✅      |
| Accept License            | ✅      |
| Create Admin User         | ✅      |
| Enable Boot Start         | ✅      |
| Open Web Interface        | ✅      |
| Login Successfully        | ✅      |


Install Splunk Universal Forwarder on Windows Victim Machine

Objective
Install and configure the Splunk Universal Forwarder on a Windows victim machine and forward Windows logs to the Splunk Enterprise server.
Lab Environment
| Component      | IP Address     | OS            |
| -------------- | -------------- | ------------- |
| Splunk Server  | 192.168.1.10   | Kali Linux    |
| Victim Machine | 192.168.1.20   | Windows 10/11 |
| Splunk UF      | Latest Version | Windows       |


Step 1: Download Splunk Universal Forwarder

https://www.splunk.com/en_us/download/universal-forwarder.html?

splunkforwarder-10.4.0-x64-release.msi

Step 2: Install Universal Forwarder

Double-click the MSI file.

Accept License
✓ Accept License Agreement

Local System Installation

Local System

Administrator Credentials

Username: admin
Password: StrongPassword123!

Installation Path

C:\Program Files\SplunkUniversalForwarder

Step 3: Verify Installation

Open PowerShell as Administrator.

cd "C:\Program Files\SplunkUniversalForwarder\bin"
.\splunk.exe status

Step 4: Start Universal Forwarder

.\splunk.exe start
y
.\splunk.exe enable boot-start

