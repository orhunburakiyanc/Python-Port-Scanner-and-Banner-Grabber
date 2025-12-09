# Python Port Scanner & Banner Grabber

## Overview
This project is a custom network reconnaissance tool developed to understand the fundamentals of **TCP/IP networking** and **socket programming**. It scans a target IP address for open ports using multi-threading for efficiency and attempts to retrieve service banners (Banner Grabbing) to identify running applications and versions.

It serves as a practical implementation of **Reconnaissance**, the first phase of the Cyber Kill Chain.

## Features
* **Multi-threading:** Scans multiple ports concurrently to significantly reduce scan time.
* **Banner Grabbing:** Connects to open ports to capture service headers (e.g., SSH, FTP, HTTP versions).
* **Socket Management:** Implements efficient socket creation and timeout handling.
* **Clean CLI Output:** Provides clear, readable feedback on open ports and services.

## Technologies Used
* **Language:** Python 3
* **Libraries:** `socket`, `threading`, `sys`, `datetime`
* **Concepts:** TCP Handshake, Socket Programming, Concurrency.

## ⚠️ Legal Disclaimer
**For Educational Purposes Only.**
This tool is created to demonstrate network scanning concepts. It is intended to be used on networks you own or have explicit permission to test. Unauthorized scanning of third-party networks is illegal and unethical. The author accepts no responsibility for unauthorized use.

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/orhunburakiyane/Python-Port-Scanner-and-Banner-Grabber.git](https://github.com/orhunburakiyane/Python-Port-Scanner-and-Banner-Grabber.git)
   cd Python-Port-Scanner-and-Banner-Grabber

2. **Run the scanner**
   ```bash
   python scanner.py <target_ip>
