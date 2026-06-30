# Python Network & Port Scanner

A simple Python-based Network and Port Scanner that scans IP addresses, discovers active hosts, and checks for open TCP ports.

---

## Features

- Scan a single IP address
- Scan a range of IP addresses
- Detect active hosts
- Multi-threaded port scanning
- Detect common services
- Export scan results
- Easy-to-use command line interface

---

## Project Structure

```
PortScanner/
│
├── main.py
├── scanner.py
├── network.py
├── services.py
├── report.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/Python-Port-Scanner.git
```

Go into the project

```bash
cd Python-Port-Scanner
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## Technologies Used

- Python 3
- Socket Programming
- Threading
- ipaddress
- argparse

---

## Example Output

```
Scanning 192.168.1.10...

Port 22  -> Open (SSH)
Port 80  -> Open (HTTP)
Port 443 -> Open (HTTPS)
```

---

## Educational Purpose

This project is intended for educational purposes only.

Scan only systems you own or have explicit permission to test.

---

## Future Improvements

- Banner Grabbing
- OS Detection
- Service Version Detection
- GUI using Tkinter
- HTML Reports
- CSV Export
- Faster Multi-threading

---

## Author

Your Name

GitHub:
https://github.com/sumitbgmi