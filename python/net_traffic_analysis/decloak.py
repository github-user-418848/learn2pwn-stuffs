import sys
from scapy.all import *

interface = 'wlan0mon'
hiddenNets = []
unhiddenNets = []

def sniffDot11(pkt):
    if pkt.haslayer(Dot11ProbeResp):
        addr2 = pkt.getlayer(Dot11).addr2
        if (addr2 in hiddenNets) & (addr2 not in unhiddenNets):
            netName = pkt.getlayer(Dot11ProbeResp).info
            print('[+] Decloaked Hidden SSID: ', netName, ' for MAC: ', addr2)
            unhiddenNets.append(addr2)
    if pkt.haslayer(Dot11Beacon):
        if pkt.getlayer(Dot11Beacon).info == '':
            addr2 = p.getlayer(Dot11).addr2
            if addr2 not in hiddenNets:
                print('[-] Detected Hidden SSID with MAC: ', addr2)
                hiddenNets.append(addr2)

def main():
    sniff(iface=interface, prn=sniffDot11)

if __name__ == '__main__':
    main()
