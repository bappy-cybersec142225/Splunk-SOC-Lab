Splunk Enterprise Installation & Configuration Guide (Kali Linux)
Lab Environment
OS: Kali Linux
Splunk Version: Splunk Enterprise
Hostname: splunk-server
IP Address: Kali Linux IP

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

## GitHub Documentation Structure



