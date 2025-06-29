# wifikill

A Python tool for ARP spoofing to disrupt Wi-Fi connectivity on a local network.

## Requirements
- Python 3.x
- [Scapy](https://scapy.net/) library
- Root privileges (required for sending raw packets)

## Installation
1. Clone this repository or download the script.
2. Install Scapy:
   ```bash
   pip install scapy
   ```

## Usage
The current version of the program requires you to manually enter your IP/Mask and the gateway's IP in order to work. (Comments have been left in the code regarding this)

After that, run the script with root privileges:

```bash
sudo python3 wifikill.py
```

The program will:
- Scan your local network for devices
- Continuously send spoofed ARP packets to disrupt Wi-Fi for other hosts
- Restore ARP tables when you press Ctrl+C

## Disclaimer
This tool is for educational and authorized testing purposes only. Its use on unauthorized networks is illegal and unethical.