<div align="center">

https://img.shields.io/badge/version-7.0-brightgreen.svg
https://img.shields.io/badge/python-3.8+-blue.svg
https://img.shields.io/badge/license-Research%2520Only-red.svg
https://img.shields.io/badge/platform-Linux%2520%257C%2520macOS%2520%257C%2520Windows-lightgrey.svg

Installation • Features • Usage • Modules • Screenshots • Disclaimer
</div>
⚡ Overview

Multi-Tool v7.0 is a premium, all-in-one security research suite designed for authorized penetration testing, red-team operations, and security research. Featuring a stunning terminal UI with animations, gradients, and real-time status indicators, this tool combines 13 powerful modules including RAT, DDoS, Keylogger, Info Stealer, and network reconnaissance tools.
✨ Features
🎨 Visual Excellence

    Ultra-Premium Terminal UI with gradient banners and animations

    Emoji Icons for intuitive module navigation

    Real-time Status Indicators for running services

    Loading Animations (spinners, progress bars, typewriter effects)

    Color-Coded Output for instant readability

    Beautiful Box Framing for clean information display

🛠️ 13 Powerful Modules
Module	Icon	Description
Network Scanner	🔍	Port scanning with customizable port lists
Hash Cracker	🔐	MD5/SHA1 cracking with wordlist support
Subdomain Enumerator	🌐	Find subdomains of any domain
Port Knocker	🚪	SYN packet sequence for firewall testing
Password Generator	🔑	Generate strong, random passwords
Base64 Tool	📝	Encode/Decode Base64 strings
HTTP Headers	🌍	Fetch and display server headers
Ping Sweep	📡	Discover live hosts on a network
DNS Lookup	🌐	Resolve domains to IP addresses
DDoS Attack Suite	💀	SYN, UDP, HTTP, ICMP flood attacks
Keylogger	⌨️	Capture keystrokes with special key support
Info Stealer	📂	System info, credentials, clipboard, screenshots
RAT Controller	🖥️	Full remote administration with GUI
📦 Installation
Prerequisites
bash

# Python 3.8+ required
python3 --version

# Install system dependencies (Linux)
sudo apt-get update
sudo apt-get install python3-tk python3-pil python3-pil.imagetk scrot -y

# Install system dependencies (macOS)
brew install python-tk scrot
# OR
xcode-select --install

Install Multi-Tool
bash

# Clone the repository
git clone https://github.com/pareth5612-dev/multi-tool.git
cd multi-tool

# Install Python dependencies
pip3 install -r requirements.txt

# Make executable
chmod +x multitool.py

# Run with root privileges (recommended for full functionality)
sudo python3 multitool.py

Requirements File

Create requirements.txt:
txt

pillow>=9.0.0
pyscreenshot>=3.0
pynput>=1.7.0

🚀 Usage
Quick Start
bash

# Run the tool
sudo python3 multitool.py

# Or if you saved it elsewhere
./multitool.py

Navigation

    Main Menu: Select modules using number/letter keys

    Module Selection: Type the key and press Enter

    Back/Exit: Follow on-screen prompts or use 0 to exit

    Help: View module descriptions in the menu

Module Commands
Key	Module	Usage
1	Network Scanner	Enter target IP/domain and optional ports
2	Hash Cracker	Select hash type (md5/sha1), enter hash
3	Subdomain Enumerator	Enter domain to discover subdomains
4	Port Knocker	Enter target IP and port sequence
5	Password Generator	Specify password length
6	Base64 Tool	Choose encode/decode, enter data
7	HTTP Headers	Enter URL with http://
8	Ping Sweep	Enter network prefix (e.g., 192.168.1)
9	DNS Lookup	Enter domain to resolve
D	DDoS Suite	Select attack type, configure parameters
K	Keylogger	Start/stop logging, view logs
I	Info Stealer	Choose information to collect
R	RAT Controller	GUI for remote administration
0	Exit	Close the application
📸 Screenshots
Main Menu
text

╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ███╗   ███╗██╗   ██╗██╗  ████████╗██╗   ██╗██╗              ║
║   ████╗ ████║██║   ██║██║  ╚══██╔══╝██║   ██║██║              ║
║   ██╔████╔██║██║   ██║██║     ██║   ██║   ██║██║              ║
║   ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║██║              ║
║   ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ╚██████╔╝███████╗         ║
║   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝    ╚═════╝ ╚══════╝         ║
║                                                                  ║
║           Security Research Suite v7.0 - ULTIMATE EDITION       ║
║        For authorized penetration testing and research          ║
║    ⚡ RAT | DDoS | Keylogger | Info Stealer | Network Tools     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

  ⚡ Ready for action. Choose your weapon. ⚡

┌──────────────────────────────────────────────────────────────────┐
│ AVAILABLE MODULES                                               │
├──────────────────────────────────────────────────────────────────┤
│ [1] 🔍 Network Scanner                                          │
│ [2] 🔐 Hash Cracker                                             │
│ [3] 🌐 Subdomain Enumerator                                     │
│ [4] 🚪 Port Knocker                                             │
│ [5] 🔑 Password Generator                                       │
│ [6] 📝 Base64 Tool                                              │
│ [7] 🌍 HTTP Headers                                             │
│ [8] 📡 Ping Sweep                                               │
│ [9] 🌐 DNS Lookup                                               │
│ [D] 💀 DDoS Attack Suite                              ● RUNNING│
│ [K] ⌨️  Keylogger                                       ● ACTIVE│
│ [I] 📂 Info Stealer                                             │
│ [R] 🖥️  RAT Controller                                          │
│ [0] 🚪 Exit                                                     │
└──────────────────────────────────────────────────────────────────┘

⏱️  System Time: 14:32:15  🖥️  Host: kali  🐍 Python: 3.11.4
──────────────────────────────────────────────────────────────────────

⚡ Select module:

Module Example - Network Scanner
text

╔══════════════════════════════════════════════════════════════════╗
║ 🔍 Network Scanner                                              ║
╚══════════════════════════════════════════════════════════════════╝

🎯 Enter target IP or hostname: 192.168.1.1
🔌 Enter ports (comma-separated, or Enter for common): 

⠋ Scanning ports...

✅ Scan Complete!
┌──────────────────────────────────────────────┐
│ 🔓 Port 22 OPEN                             │
│ 🔓 Port 80 OPEN                             │
│ 🔓 Port 443 OPEN                            │
│ 🔓 Port 3306 OPEN                           │
└──────────────────────────────────────────────┘

Press Enter to continue...

Module Example - DDoS Attack
text

╔══════════════════════════════════════════════════════════════════╗
║ 💀 DDoS Attack Suite                                            ║
╚══════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────┐
│ 💀 Attack Types                              │
│  [1] SYN Flood (TCP)                        │
│  [2] UDP Flood                               │
│  [3] HTTP Flood (Layer 7)                   │
│  [4] ICMP Flood (root)                      │
│  [5] Back to Menu                           │
└──────────────────────────────────────────────┘

🎯 Select attack type: 1
🎯 Target IP or domain: 192.168.1.100
✅ Resolved 192.168.1.100 -> 192.168.1.100
🔌 Target port (default 80): 80
🧵 Threads (default 100): 200
⏱️  Duration in seconds (default 60): 30

⚠️  Starting SYN attack on 192.168.1.100:80
⚠️  Threads: 200, Duration: 30s
⚠️  Press Ctrl+C to stop

Press Enter to launch attack...

╔══════════════════════════════════════════════════════════╗
║                    ATTACK STARTED                       ║
╚══════════════════════════════════════════════════════════╝

[!] Target: 192.168.1.100:80
[!] Type: SYN flood
[!] Threads: 200
[!] Duration: 30s
[!] Started at: 14:35:22

[*] Packets: 152,847 | Rate: 76,423 pps | Bandwidth: 39.1 Mbps | Errors: 0 | Elapsed: 2.0s

🎯 Module Deep Dive
🔍 Network Scanner

    Purpose: Identify open ports on target systems

    Features:

        Pre-configured common ports list

        Custom port specification

        Multi-threaded scanning

        Real-time results display

💀 DDoS Attack Suite

    Attack Types:

        SYN Flood: TCP SYN packet flood for state exhaustion

        UDP Flood: High-volume UDP packet flood

        HTTP Flood: Layer 7 application-level attacks

        ICMP Flood: Ping flood (requires root)

    Features:

        Configurable thread count

        Duration control

        Real-time statistics (PPS, bandwidth)

        Domain resolution support

⌨️ Keylogger

    Purpose: Keyboard input capture for monitoring

    Features:

        Full keystroke logging

        Special key support (Shift, Ctrl, Alt, F1-F12, arrows)

        Auto-flush to disk (every 100 keystrokes)

        Log viewing and management

        Timestamped log files

📂 Info Stealer

    Collected Data:

        System Information: OS, hostname, IP, environment variables

        Browser Credentials: Chrome, Firefox, Edge, Brave

        Clipboard Content: Current clipboard data

        Screenshots: Full screen captures

    Output: JSON report with all collected data

🖥️ RAT Controller

    Purpose: Remote administration with GUI

    Features:

        Multi-client support

        Command execution

        Screen capture streaming

        File browser

        Client management (start/stop/kill)

        Key simulation

🛡️ Security & Disclaimer
<div align="center"> ⚠️ **IMPORTANT NOTICE** ⚠️ </div>

This tool is designed for authorized security research and penetration testing ONLY.

    Do NOT use on systems you do not own or have explicit written permission to test.

    Do NOT use for illegal activities, harassment, or unauthorized access.

    Do NOT distribute or use in malicious campaigns.

By using this tool, you agree to:

    Use only on systems you own or have explicit authorization

    Comply with all applicable laws and regulations

    Accept full responsibility for your actions

    Not use for any illegal or unethical purposes

The developers assume no liability for misuse or illegal activities.
📜 License

Research & Educational Use Only

This software is provided for authorized security research, penetration testing, and educational purposes only. Redistribution, modification, or commercial use requires explicit permission.
🤝 Contributing

Contributions for security research enhancements are welcome:

    Fork the repository

    Create your feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some AmazingFeature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

Please ensure all contributions maintain the ethical use policy.
📞 Support

    Issues: Report bugs via GitHub Issues

    Documentation: Refer to this README

    Security Research: For authorized security testing only

⭐ Acknowledgments

    Built with Python 3

    Terminal UI powered by ANSI escape codes

    Icons and emojis for enhanced UX

    Inspired by professional security tools

<div align="center">

⬆ Back to Top

Made with ❤️ for the security research community

Use responsibly. Hack ethically. Stay secure.
</div>
📁 File Structure
text

multi-tool/
├── multitool.py          # Main application
├── rat_client.py         # Generated RAT client payload
├── logs/                 # Keylogger logs (auto-created)
│   └── keylog_*.txt
├── stolen_data/          # Info stealer output (auto-created)
│   ├── report_*.json
│   └── screenshot_*.png
└── README.md             # This file

🧪 Quick Test
bash

# Quick test without installing
python3 multitool.py

# Check if all modules are available
python3 -c "import pynput, PIL, pyscreenshot; print('✅ All dependencies installed')"

Version: ](url)](url)](url)](url)](url)
Last Updated: July 2026
Status: Active Development
<div align="center"> ⚠️ **For authorized security research and penetration testing only** ⚠️ </div>
