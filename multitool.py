#!/usr/bin/env python3
"""
Multi-Tool v7.0 - Ultimate Security Research Suite
Premium Terminal UI with Advanced Visual Design
For authorized penetration testing and security research only
"""

import os
import sys
import time
import socket
import threading
import subprocess
import hashlib
import base64
import re
import json
import random
import string
import struct
import io
import queue
import signal
import platform
import sqlite3
import shutil
import math
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.parse import urlparse

# ============================================
# ULTRA PREMIUM COLOR SYSTEM
# ============================================
class Colors:
    # Standard colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Bold variants
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    RESET = '\033[0m'
    
    # Custom gradients (simulated)
    @staticmethod
    def gradient_text(text, start_color, end_color):
        """Simulate gradient by alternating colors per character"""
        result = ""
        chars = list(text)
        for i, char in enumerate(chars):
            progress = i / len(chars) if chars else 0
            if progress < 0.5:
                result += start_color + char
            else:
                result += end_color + char
        return result + Colors.RESET

# ============================================
# ANIMATION ENGINE
# ============================================
class Animator:
    @staticmethod
    def loading_bar(duration=2, message="Processing"):
        """Display an animated loading bar"""
        chars = ['░', '▒', '▓', '█']
        for i in range(101):
            filled = int(i / 2)
            bar = '█' * filled + '░' * (50 - filled)
            print(f"\r{Colors.CYAN}{message}... {Colors.GREEN}[{bar}] {Colors.YELLOW}{i}%{Colors.RESET}", end="")
            time.sleep(duration / 100)
        print()
    
    @staticmethod
    def spinner(duration=1.5, message="Loading"):
        """Display a spinning animation"""
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        start = time.time()
        i = 0
        while time.time() - start < duration:
            print(f"\r{Colors.CYAN}{frames[i % len(frames)]} {message}...{Colors.RESET}", end="")
            i += 1
            time.sleep(0.08)
        print()
    
    @staticmethod
    def typewriter(text, delay=0.03, color=Colors.GREEN):
        """Typewriter effect for text"""
        for char in text:
            print(f"{color}{char}{Colors.RESET}", end="", flush=True)
            time.sleep(delay)
        print()
    
    @staticmethod
    def pulse(text, duration=2):
        """Pulsing text effect"""
        colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.MAGENTA]
        start = time.time()
        i = 0
        while time.time() - start < duration:
            print(f"\r{colors[i % len(colors)]}{text}{Colors.RESET}", end="")
            i += 1
            time.sleep(0.15)
        print()

# ============================================
# ULTRA PREMIUM BANNER
# ============================================
class Banner:
    @staticmethod
    def display():
        """Display the ultimate premium banner"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Animated gradient banner
        banner_lines = [
            "╔══════════════════════════════════════════════════════════════════╗",
            "║                                                                  ║",
            "║   ███╗   ███╗██╗   ██╗██╗  ████████╗██╗   ██╗██╗              ║",
            "║   ████╗ ████║██║   ██║██║  ╚══██╔══╝██║   ██║██║              ║",
            "║   ██╔████╔██║██║   ██║██║     ██║   ██║   ██║██║              ║",
            "║   ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║██║              ║",
            "║   ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ╚██████╔╝███████╗         ║",
            "║   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝    ╚═════╝ ╚══════╝         ║",
            "║                                                                  ║",
            "║              ██████╗ ███████╗██╗   ██╗██╗██╗  ██╗              ║",
            "║              ██╔══██╗██╔════╝██║   ██║██║╚██╗██╔╝              ║",
            "║              ██████╔╝█████╗  ██║   ██║██║ ╚███╔╝               ║",
            "║              ██╔══██╗██╔══╝  ██║   ██║██║ ██╔██╗               ║",
            "║              ██████╔╝███████╗╚██████╔╝██║██╔╝ ██╗              ║",
            "║              ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝              ║",
            "║                                                                  ║",
            "║           Security Research Suite v7.0 - ULTIMATE EDITION       ║",
            "║        For authorized penetration testing and research          ║",
            "║    ⚡ RAT | DDoS | Keylogger | Info Stealer | Network Tools     ║",
            "║                                                                  ║",
            "╚══════════════════════════════════════════════════════════════════╝"
        ]
        
        # Print with gradient colors
        colors = [Colors.CYAN, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]
        for i, line in enumerate(banner_lines):
            color = colors[i % len(colors)]
            if i == 0 or i == len(banner_lines) - 1:
                print(f"{Colors.BOLD}{Colors.CYAN}{line}{Colors.RESET}")
            elif "█" in line and "║" in line:
                # Gradient effect on the logo
                if "███" in line:
                    print(f"{Colors.BOLD}{Colors.CYAN}{line[:8]}{Colors.RESET}{Colors.BOLD}{Colors.MAGENTA}{line[8:24]}{Colors.RESET}{Colors.BOLD}{Colors.CYAN}{line[24:]}{Colors.RESET}")
                else:
                    print(f"{Colors.DIM}{Colors.CYAN}{line}{Colors.RESET}")
            else:
                print(f"{color}{line}{Colors.RESET}")
            time.sleep(0.01)  # Slight animation
        
        print()
        
        # Subtitle with pulse effect
        Animator.pulse("  ⚡ Ready for action. Choose your weapon. ⚡  ", duration=1)
        print()

# ============================================
# ULTRA PREMIUM MENU
# ============================================
class PremiumMenu:
    @staticmethod
    def display(modules, keylogger_running=False, ddos_running=False, rat_running=False):
        """Display premium menu with status indicators"""
        
        # Top decorative line
        print(f"{Colors.BOLD}{Colors.CYAN}┌──────────────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}│{Colors.RESET} {Colors.BOLD}{Colors.WHITE}AVAILABLE MODULES{Colors.RESET}{' ' * 45}{Colors.BOLD}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}├──────────────────────────────────────────────────────────────────┤{Colors.RESET}")
        
        # Module list with icons and colors
        modules_display = [
            ("1", "🔍 Network Scanner", Colors.GREEN),
            ("2", "🔐 Hash Cracker", Colors.YELLOW),
            ("3", "🌐 Subdomain Enumerator", Colors.BLUE),
            ("4", "🚪 Port Knocker", Colors.MAGENTA),
            ("5", "🔑 Password Generator", Colors.CYAN),
            ("6", "📝 Base64 Tool", Colors.WHITE),
            ("7", "🌍 HTTP Headers", Colors.BLUE),
            ("8", "📡 Ping Sweep", Colors.GREEN),
            ("9", "🌐 DNS Lookup", Colors.CYAN),
            ("D", "💀 DDoS Attack Suite", Colors.RED),
            ("K", "⌨️  Keylogger", Colors.YELLOW),
            ("I", "📂 Info Stealer", Colors.MAGENTA),
            ("R", "🖥️  RAT Controller", Colors.GREEN),
            ("0", "🚪 Exit", Colors.RED),
        ]
        
        for key, name, color in modules_display:
            status = ""
            if key == "K" and keylogger_running:
                status = f"{Colors.GREEN}● ACTIVE{Colors.RESET}"
            elif key == "D" and ddos_running:
                status = f"{Colors.RED}● RUNNING{Colors.RESET}"
            elif key == "R" and rat_running:
                status = f"{Colors.GREEN}● ACTIVE{Colors.RESET}"
            
            padding = " " * (50 - len(name) - len(status))
            print(f"{Colors.BOLD}{Colors.CYAN}│{Colors.RESET} {Colors.BOLD}{color}[{key}]{Colors.RESET} {name}{padding}{status} {Colors.BOLD}{Colors.CYAN}│{Colors.RESET}")
        
        # Bottom decorative line
        print(f"{Colors.BOLD}{Colors.CYAN}└──────────────────────────────────────────────────────────────────┘{Colors.RESET}")
        print()
        
        # System status bar
        uptime = datetime.now().strftime("%H:%M:%S")
        print(f"{Colors.DIM}{Colors.CYAN}⏱️  System Time: {Colors.WHITE}{uptime}{Colors.RESET}  ", end="")
        print(f"{Colors.DIM}{Colors.CYAN}🖥️  Host: {Colors.WHITE}{socket.gethostname()}{Colors.RESET}  ", end="")
        print(f"{Colors.DIM}{Colors.CYAN}🐍 Python: {Colors.WHITE}{sys.version[:10]}{Colors.RESET}")
        print(f"{Colors.DIM}{Colors.CYAN}─" * 70 + f"{Colors.RESET}\n")

# ============================================
# MODULE IMPORTS (All existing modules)
# ============================================
# [All previous module classes go here - NetworkScanner, HashCracker, etc.]
# For brevity, I'll include just the structure. In the final file, all modules are present.

# ============================================
# ULTRA PREMIUM MAIN APPLICATION
# ============================================
class MultiToolUltra:
    def __init__(self):
        self.running = True
        self.keylogger_running = False
        self.ddos_running = False
        self.rat_running = False
        
        # Initialize engines (existing code from v6.0)
        self.ddos_engine = DDOSEngine()
        self.keylogger = KeyloggerEngine()
        self.info_stealer = InfoStealerEngine()
        
        # Module registry
        self.modules = {
            "1": {"name": "Network Scanner", "func": self.menu_network_scan, "icon": "🔍"},
            "2": {"name": "Hash Cracker", "func": self.menu_hash_crack, "icon": "🔐"},
            "3": {"name": "Subdomain Enumerator", "func": self.menu_subdomain_enum, "icon": "🌐"},
            "4": {"name": "Port Knocker", "func": self.menu_port_knock, "icon": "🚪"},
            "5": {"name": "Password Generator", "func": self.menu_password_gen, "icon": "🔑"},
            "6": {"name": "Base64 Tool", "func": self.menu_base64, "icon": "📝"},
            "7": {"name": "HTTP Headers", "func": self.menu_http_headers, "icon": "🌍"},
            "8": {"name": "Ping Sweep", "func": self.menu_ping_sweep, "icon": "📡"},
            "9": {"name": "DNS Lookup", "func": self.menu_dns_lookup, "icon": "🌐"},
            "D": {"name": "DDoS Attack Suite", "func": self.menu_ddos, "icon": "💀"},
            "K": {"name": "Keylogger", "func": self.menu_keylogger, "icon": "⌨️"},
            "I": {"name": "Info Stealer", "func": self.menu_info_stealer, "icon": "📂"},
            "R": {"name": "RAT Controller", "func": self.menu_rat, "icon": "🖥️"},
            "0": {"name": "Exit", "func": self.exit, "icon": "🚪"}
        }
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def show_module_header(self, title, icon="⚡"):
        """Display premium module header"""
        print(f"{Colors.BOLD}{Colors.CYAN}╔══════════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}║{Colors.RESET} {Colors.BOLD}{Colors.WHITE}{icon} {title}{Colors.RESET}{' ' * (60 - len(title) - len(icon))}{Colors.BOLD}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    # ===== MENU FUNCTIONS (from v6.0) =====
    # All menu_* functions from v6.0 go here with enhanced visual output
    
    def menu_network_scan(self):
        self.show_module_header("Network Scanner", "🔍")
        target = input(f"{Colors.CYAN}🎯 Enter target IP or hostname: {Colors.RESET}")
        ports = input(f"{Colors.CYAN}🔌 Enter ports (comma-separated, or Enter for common): {Colors.RESET}")
        if ports:
            port_list = [int(p.strip()) for p in ports.split(',') if p.strip()]
        else:
            port_list = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
        
        Animator.spinner(1, "Scanning ports")
        open_ports = NetworkScanner.scan_ports(target, port_list)
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}✅ Scan Complete!{Colors.RESET}")
        print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
        if open_ports:
            for port in open_ports:
                print(f"{Colors.CYAN}│{Colors.RESET} {Colors.GREEN}🔓 Port {port} OPEN{Colors.RESET}{' ' * (35 - len(str(port)))}{Colors.CYAN}│{Colors.RESET}")
        else:
            print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}⚠️  No open ports found{Colors.RESET}{' ' * 19}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_hash_crack(self):
        self.show_module_header("Hash Cracker", "🔐")
        hash_type = input(f"{Colors.CYAN}🔢 Hash type (md5/sha1): {Colors.RESET}").lower()
        target_hash = input(f"{Colors.CYAN}🔑 Enter hash: {Colors.RESET}")
        wordlist = input(f"{Colors.CYAN}📂 Wordlist path (Enter for default): {Colors.RESET}")
        if not wordlist:
            wordlist = "/usr/share/wordlists/rockyou.txt"
        
        Animator.spinner(1.5, "Cracking hash")
        if hash_type == "md5":
            HashCracker.crack_md5(target_hash, wordlist)
        elif hash_type == "sha1":
            HashCracker.crack_sha1(target_hash, wordlist)
        else:
            print(f"{Colors.RED}❌ Unsupported hash type{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_subdomain_enum(self):
        self.show_module_header("Subdomain Enumerator", "🌐")
        domain = input(f"{Colors.CYAN}🌍 Enter domain: {Colors.RESET}")
        enumerator = SubdomainEnumerator(domain)
        
        Animator.spinner(2, "Enumerating subdomains")
        enumerator.enumerate()
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}✅ Found {len(enumerator.subdomains)} subdomains{Colors.RESET}")
        if enumerator.subdomains:
            print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
            for sub in enumerator.subdomains[:10]:
                print(f"{Colors.CYAN}│{Colors.RESET} {Colors.GREEN}🌐 {sub}{Colors.RESET}{' ' * (35 - len(sub))}{Colors.CYAN}│{Colors.RESET}")
            if len(enumerator.subdomains) > 10:
                print(f"{Colors.CYAN}│{Colors.RESET} {Colors.DIM}... and {len(enumerator.subdomains) - 10} more{Colors.RESET}{' ' * 16}{Colors.CYAN}│{Colors.RESET}")
            print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_port_knock(self):
        self.show_module_header("Port Knocker", "🚪")
        target = input(f"{Colors.CYAN}🎯 Enter target IP: {Colors.RESET}")
        ports = input(f"{Colors.CYAN}🔌 Enter ports (comma-separated): {Colors.RESET}")
        port_list = [int(p.strip()) for p in ports.split(',') if p.strip()]
        
        Animator.spinner(1, "Knocking on ports")
        PortKnocker.knock(target, port_list)
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_password_gen(self):
        self.show_module_header("Password Generator", "🔑")
        length = input(f"{Colors.CYAN}📏 Password length (default 16): {Colors.RESET}")
        length = int(length) if length else 16
        
        Animator.spinner(0.5, "Generating password")
        password = PasswordGenerator.generate(length)
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}✅ Password Generated!{Colors.RESET}")
        print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET} {Colors.BOLD}{Colors.WHITE}{password}{Colors.RESET}{' ' * (35 - len(password))}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_base64(self):
        self.show_module_header("Base64 Tool", "📝")
        action = input(f"{Colors.CYAN}🔄 Encode or decode? (e/d): {Colors.RESET}").lower()
        data = input(f"{Colors.CYAN}📝 Enter data: {Colors.RESET}")
        
        if action == 'e':
            Base64Tool.encode(data)
        elif action == 'd':
            Base64Tool.decode(data)
        else:
            print(f"{Colors.RED}❌ Invalid action{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_http_headers(self):
        self.show_module_header("HTTP Headers", "🌍")
        url = input(f"{Colors.CYAN}🌐 Enter URL (with http://): {Colors.RESET}")
        
        Animator.spinner(1, "Fetching headers")
        HTTPHeaders.fetch(url)
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_ping_sweep(self):
        self.show_module_header("Ping Sweep", "📡")
        network = input(f"{Colors.CYAN}🌐 Enter network prefix (e.g., 192.168.1): {Colors.RESET}")
        
        Animator.spinner(3, "Pinging network")
        alive = NetworkScanner.ping_sweep(network)
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}✅ Found {len(alive)} alive hosts{Colors.RESET}")
        if alive:
            print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
            for ip in alive[:10]:
                print(f"{Colors.CYAN}│{Colors.RESET} {Colors.GREEN}💻 {ip}{Colors.RESET}{' ' * (35 - len(ip))}{Colors.CYAN}│{Colors.RESET}")
            if len(alive) > 10:
                print(f"{Colors.CYAN}│{Colors.RESET} {Colors.DIM}... and {len(alive) - 10} more{Colors.RESET}{' ' * 16}{Colors.CYAN}│{Colors.RESET}")
            print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_dns_lookup(self):
        self.show_module_header("DNS Lookup", "🌐")
        domain = input(f"{Colors.CYAN}🌍 Enter domain: {Colors.RESET}")
        
        Animator.spinner(0.5, "Resolving DNS")
        NetworkScanner.dns_lookup(domain)
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_ddos(self):
        self.show_module_header("DDoS Attack Suite", "💀")
        if self.ddos_engine.running:
            print(f"{Colors.YELLOW}⚠️  Attack currently running{Colors.RESET}")
            if input(f"{Colors.CYAN}Stop attack? (y/n): {Colors.RESET}").lower() == 'y':
                self.ddos_engine.stop_attack()
                self.ddos_engine.running = False
                self.ddos_running = False
            input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
            return
        
        print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET} {Colors.BOLD}{Colors.RED}💀 Attack Types{Colors.RESET}{' ' * 32}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[1]{Colors.RESET} SYN Flood (TCP)      {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[2]{Colors.RESET} UDP Flood             {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[3]{Colors.RESET} HTTP Flood (Layer 7)   {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[4]{Colors.RESET} ICMP Flood (root)      {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[5]{Colors.RESET} Back to Menu          {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
        
        choice = input(f"\n{Colors.CYAN}🎯 Select attack type: {Colors.RESET}")
        if choice == '5':
            return
        
        target = input(f"{Colors.CYAN}🎯 Target IP or domain: {Colors.RESET}")
        try:
            target_ip = socket.gethostbyname(target)
            print(f"{Colors.GREEN}✅ Resolved {target} -> {target_ip}{Colors.RESET}")
        except:
            target_ip = target
        
        port = input(f"{Colors.CYAN}🔌 Target port (default 80): {Colors.RESET}")
        port = int(port) if port else 80
        
        threads = input(f"{Colors.CYAN}🧵 Threads (default 100): {Colors.RESET}")
        threads = int(threads) if threads else 100
        
        duration = input(f"{Colors.CYAN}⏱️  Duration in seconds (default 60): {Colors.RESET}")
        duration = int(duration) if duration else 60
        
        attack_types = {'1': 'syn', '2': 'udp', '3': 'http', '4': 'icmp'}
        attack_type = attack_types.get(choice)
        if not attack_type:
            print(f"{Colors.RED}❌ Invalid choice{Colors.RESET}")
            input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
            return
        
        kwargs = {}
        if attack_type == 'http':
            path = input(f"{Colors.CYAN}📂 Path (default /): {Colors.RESET}")
            kwargs['path'] = path if path else '/'
        
        print(f"\n{Colors.YELLOW}⚠️  Starting {attack_type.upper()} attack on {target_ip}:{port}{Colors.RESET}")
        print(f"{Colors.YELLOW}⚠️  Threads: {threads}, Duration: {duration}s{Colors.RESET}")
        print(f"{Colors.RED}⚠️  Press Ctrl+C to stop{Colors.RESET}")
        input(f"\n{Colors.CYAN}Press Enter to launch attack...{Colors.RESET}")
        
        self.ddos_engine.start_attack(target_ip, port, attack_type, threads, duration, **kwargs)
        self.ddos_running = True
        
        try:
            while self.ddos_engine.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.ddos_engine.stop_attack()
            self.ddos_engine.running = False
            self.ddos_running = False
        
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_keylogger(self):
        self.show_module_header("Keylogger", "⌨️")
        if not HAS_PYNPUT:
            print(f"{Colors.RED}❌ pynput not installed. Run: pip install pynput{Colors.RESET}")
            input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
            return
        
        if self.keylogger.running:
            print(f"{Colors.GREEN}✅ Keylogger is RUNNING{Colors.RESET}")
            print(f"{Colors.CYAN}📂 Log file: {self.keylogger.log_file}{Colors.RESET}")
            print(f"\n{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
            print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[1]{Colors.RESET} Stop Keylogger       {Colors.CYAN}│{Colors.RESET}")
            print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[2]{Colors.RESET} View Logs            {Colors.CYAN}│{Colors.RESET}")
            print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[3]{Colors.RESET} Clear Logs           {Colors.CYAN}│{Colors.RESET}")
            print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[4]{Colors.RESET} Back to Menu         {Colors.CYAN}│{Colors.RESET}")
            print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
            
            choice = input(f"\n{Colors.CYAN}🎯 Select option: {Colors.RESET}")
            if choice == '1':
                self.keylogger.stop()
                self.keylogger_running = False
            elif choice == '2':
                self.view_keylogger_logs()
            elif choice == '3':
                self.clear_keylogger_logs()
            else:
                input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
            return
        
        if input(f"{Colors.CYAN}⌨️  Start keylogger? (y/n): {Colors.RESET}").lower() == 'y':
            filename = input(f"{Colors.CYAN}📂 Custom filename (Enter for auto): {Colors.RESET}")
            if self.keylogger.start(filename if filename else None):
                self.keylogger_running = True
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def view_keylogger_logs(self):
        logs = self.keylogger.view_logs()
        if not logs:
            print(f"{Colors.YELLOW}⚠️  No logs found{Colors.RESET}")
            input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
            return
        
        print(f"\n{Colors.CYAN}📂 Available logs:{Colors.RESET}")
        for i, log in enumerate(logs, 1):
            print(f"  {Colors.YELLOW}[{i}]{Colors.RESET} {log}")
        
        choice = input(f"\n{Colors.CYAN}Select log to view (0 to cancel): {Colors.RESET}")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(logs):
                content = self.keylogger.get_log_content(logs[idx])
                if content:
                    print(f"\n{Colors.BOLD}{Colors.GREEN}┌─── {logs[idx]} ───┐{Colors.RESET}")
                    print(content)
                    print(f"{Colors.BOLD}{Colors.GREEN}└─────────────────────┘{Colors.RESET}")
                else:
                    print(f"{Colors.RED}❌ Could not read log{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def clear_keylogger_logs(self):
        logs = self.keylogger.view_logs()
        if not logs:
            print(f"{Colors.YELLOW}⚠️  No logs to clear{Colors.RESET}")
            input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
            return
        
        if input(f"{Colors.RED}⚠️  Delete ALL logs? (y/n): {Colors.RESET}").lower() == 'y':
            for log in logs:
                try:
                    os.remove(os.path.join(self.keylogger.log_path, log))
                except:
                    pass
            print(f"{Colors.GREEN}✅ Logs cleared{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_info_stealer(self):
        self.show_module_header("Info Stealer", "📂")
        print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[1]{Colors.RESET} System Information    {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[2]{Colors.RESET} Browser Credentials   {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[3]{Colors.RESET} Clipboard Content     {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[4]{Colors.RESET} Screenshot            {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[5]{Colors.RESET} 🚀 COLLECT ALL        {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[6]{Colors.RESET} View Reports          {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.YELLOW}[7]{Colors.RESET} Back to Menu          {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
        
        choice = input(f"\n{Colors.CYAN}🎯 Select option: {Colors.RESET}")
        
        if choice == '1':
            Animator.spinner(1, "Collecting system info")
            info = self.info_stealer.get_system_info()
            print(f"\n{Colors.BOLD}{Colors.GREEN}✅ System Information{Colors.RESET}")
            print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
            for key, value in info.items():
                print(f"{Colors.CYAN}│{Colors.RESET} {Colors.WHITE}{key}:{Colors.RESET} {Colors.CYAN}{str(value)[:30]}{Colors.RESET}{' ' * (35 - len(str(value)[:30]))}{Colors.CYAN}│{Colors.RESET}")
            print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
            
        elif choice == '2':
            Animator.spinner(1.5, "Extracting browser credentials")
            creds = self.info_stealer.get_browser_credentials()
            if creds:
                print(f"\n{Colors.BOLD}{Colors.GREEN}✅ Found {len(creds)} credentials{Colors.RESET}")
                for c in creds[:5]:
                    print(f"  {Colors.CYAN}🔑 {c['browser']}{Colors.RESET}: {c['url']} - {c['username']}")
            else:
                print(f"{Colors.YELLOW}⚠️  No credentials found{Colors.RESET}")
            
        elif choice == '3':
            Animator.spinner(0.5, "Capturing clipboard")
            clip = self.info_stealer.get_clipboard_content()
            if clip:
                print(f"\n{Colors.BOLD}{Colors.GREEN}✅ Clipboard Content{Colors.RESET}")
                print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET} {Colors.WHITE}{clip[:50]}{Colors.RESET}{' ' * (35 - len(clip[:50]))}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}⚠️  No clipboard content{Colors.RESET}")
            
        elif choice == '4':
            Animator.spinner(1, "Capturing screenshot")
            screenshot = self.info_stealer.get_screenshot()
            if screenshot:
                print(f"{Colors.GREEN}✅ Screenshot saved: {screenshot}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}⚠️  Screenshot failed{Colors.RESET}")
            
        elif choice == '5':
            Animator.spinner(2, "Collecting ALL data")
            self.info_stealer.collect_all()
            
        elif choice == '6':
            reports = self.info_stealer.view_reports()
            if not reports:
                print(f"{Colors.YELLOW}⚠️  No reports found{Colors.RESET}")
            else:
                print(f"\n{Colors.CYAN}📂 Available reports:{Colors.RESET}")
                for i, report in enumerate(reports, 1):
                    print(f"  {Colors.YELLOW}[{i}]{Colors.RESET} {report}")
                choice2 = input(f"\n{Colors.CYAN}Select report to view (0 to cancel): {Colors.RESET}")
                if choice2.isdigit():
                    idx = int(choice2) - 1
                    if 0 <= idx < len(reports):
                        report_path = os.path.join(self.info_stealer.output_dir, reports[idx])
                        with open(report_path, 'r') as f:
                            data = json.load(f)
                            print(f"\n{Colors.BOLD}{Colors.GREEN}┌─── {reports[idx]} ───┐{Colors.RESET}")
                            print(json.dumps(data, indent=2, default=str)[:500])
                            print(f"{Colors.BOLD}{Colors.GREEN}└─────────────────────┘{Colors.RESET}")
        
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def menu_rat(self):
        self.show_module_header("RAT Controller", "🖥️")
        print(f"{Colors.GREEN}🖥️  Starting RAT Controller GUI...{Colors.RESET}")
        print(f"{Colors.YELLOW}⚠️  GUI will open in a new window{Colors.RESET}")
        self.rat_running = True
        time.sleep(1)
        rat = RATServerGUI()
        rat.run()
        self.rat_running = False
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
    
    def exit(self):
        print(f"\n{Colors.BOLD}{Colors.RED}┌──────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.RED}│              EXITING...                        │{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.RED}└──────────────────────────────────────────────┘{Colors.RESET}")
        
        if self.ddos_engine.running:
            self.ddos_engine.stop_attack()
            self.ddos_engine.running = False
        if self.keylogger.running:
            self.keylogger.stop()
            self.keylogger_running = False
        
        Animator.spinner(1, "Shutting down")
        print(f"\n{Colors.GREEN}✅ Goodbye!{Colors.RESET}")
        self.running = False
    
    def run(self):
        while self.running:
            self.clear_screen()
            Banner.display()
            PremiumMenu.display(
                self.modules,
                keylogger_running=self.keylogger_running,
                ddos_running=self.ddos_engine.running,
                rat_running=self.rat_running
            )
            
            choice = input(f"{Colors.BOLD}{Colors.CYAN}⚡ Select module: {Colors.RESET}").upper()
            
            if choice in self.modules:
                self.clear_screen()
                Banner.display()
                self.modules[choice]['func']()
            else:
                print(f"\n{Colors.RED}❌ Invalid choice!{Colors.RESET}")
                time.sleep(0.8)

# ============================================
# ENTRY POINT
# ============================================
if __name__ == "__main__":
    # Check for root
    if os.geteuid() != 0:
        print(f"{Colors.YELLOW}⚠️  Some modules require root privileges{Colors.RESET}")
        print(f"{Colors.YELLOW}⚠️  Run with sudo for full functionality{Colors.RESET}")
        time.sleep(1)
    
    # Check dependencies
    missing = []
    try:
        import PIL
    except:
        missing.append("pillow")
    try:
        import pynput
    except:
        missing.append("pynput")
    
    if missing:
        print(f"{Colors.RED}❌ Missing dependencies: {', '.join(missing)}{Colors.RESET}")
        print(f"{Colors.YELLOW}📦 Install with: pip install {' '.join(missing)}{Colors.RESET}")
        time.sleep(2)
    
    # Launch ultra premium tool
    tool = MultiToolUltra()
    try:
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}⚠️  Interrupted by user{Colors.RESET}")
        sys.exit(0)
