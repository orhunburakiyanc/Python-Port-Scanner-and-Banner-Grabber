# Python Port Scanner & Banner Grabber 🛡️

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Educational-orange)

## 📋 What is this?

This is a network reconnaissance tool I built to learn how port scanning actually works behind the scenes. It checks which ports are open on a target machine and tries to identify what services are running on them by grabbing their banners—basically the "hello" message services send when you connect.

Think of it as knocking on every door of a building to see which ones are unlocked and what's inside. This is exactly what tools like Nmap do, but building it from scratch helped me understand TCP connections, socket programming, and how network services identify themselves.

## What can it do?

The scanner combines speed with information gathering:

- **Concurrent scanning** - Uses multiple threads to check many ports at once instead of one-by-one (which would take forever)
- **Banner grabbing** - Connects to open ports and reads service banners to identify what's running (SSH version, web server type, FTP info, etc.)
- **Smart socket handling** - Manages connections properly with timeouts so the scan doesn't hang on unresponsive ports
- **Clean output** - Shows results in a readable format as it finds open ports

This is essentially the first step in any security assessment—reconnaissance. Before you can test security, you need to know what's exposed.

## Technologies used

Built entirely with Python 3's standard library, no external dependencies needed:

- **socket** - For creating TCP connections and communicating with remote ports
- **threading** - To scan multiple ports simultaneously and speed things up
- **sys & datetime** - For handling arguments and tracking scan duration

The core concept here is understanding the TCP three-way handshake (SYN, SYN-ACK, ACK) and how services advertise themselves through banners.

## ⚠️ Legal disclaimer

Port scanning can be illegal depending on where you do it and what you're scanning. Here's what you need to know:

- ✅ Scan your own devices and home network
- ✅ Use it in controlled lab environments or CTF challenges
- ✅ Scan systems where you have written authorization
- ❌ Never scan networks or systems you don't own
- ❌ Don't scan infrastructure without explicit permission

Many organizations consider unauthorized scanning an attack. Some countries have laws that make it a criminal offense. This tool exists to help you learn about network security—use it responsibly and legally. I'm not liable for how you choose to use it.

## 🔧 Installation & Usage

Clone the repository:

```bash
git clone https://github.com/orhunburakiyane/Python-Port-Scanner-and-Banner-Grabber.git
cd Python-Port-Scanner-and-Banner-Grabber
```

No installation needed—it uses only Python's built-in libraries. Just run it:

```bash
python3 scanner.py <target_ip> <start_port> <end_port>
```

Example - scan common ports on your localhost:

```bash
python3 scanner.py 127.0.0.1 1 1000
```

Example - scan web and database ports on a target:

```bash
python3 scanner.py 192.168.1.100 20 3306
```

The scanner will show you which ports are open and what banners it captured from them.

## 💡 What you'll learn

Working with this tool teaches you:

- How TCP connections are established and why port scanning works
- The difference between open, closed, and filtered ports
- Why services expose banners and how to interpret them
- How threading improves performance in I/O-bound operations
- The basics of network reconnaissance and enumeration
- Why hiding service version information matters for security

## Contributing

Found a bug or want to add features? Feel free to submit pull requests. Ideas for improvements:

- UDP port scanning support
- More sophisticated banner parsing
- Output to JSON/CSV for further analysis
- Stealth scanning techniques

## License

MIT License - use it for learning, modify it, break it, fix it, whatever helps you understand networking better.

---
