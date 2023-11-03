"""TCP SYN network port scanner"""

from multiprocessing import Pool
import sys
from scapy.all import IP, TCP, sr1

class Target:
    """Target host"""
    target = ""
    verbose = False

    def __init__(self, target):
        self.target = target
        self.ports = []

    def tcp_syn_scan(self, port: int):
        """Check if port is open using TCP SYN"""
        packet = IP(dst=self.target) / TCP(dport=port, flags='S')
        resp = sr1(packet, timeout=2, verbose=0)
        if resp is not None and resp[TCP].flags == 'SA':
            if self.verbose:
                print(f"Host {self.target} port {port} is open")
            return port

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("example12 [-v] [-a] <target>")
        sys.exit(1)

    max_ports = 1024
    t = Target(sys.argv[-1])

    for f in sys.argv[1:-1]:
        if f == "-v":
            t.verbose = True
        elif f == "-a":
            max_ports = 65535

    t.verbose = True
    with Pool(30) as p:
        ports = p.map(t.tcp_syn_scan, range(1, max_ports))

        print(f"Scan report for {t.target}")
        if len(ports) == 0:
            print("No ports open")
        else:
            print("PORT      STATE")
        for p in ports:
            if p is None:
                continue
            print(f"{f'{p}/tcp':<10}open")
