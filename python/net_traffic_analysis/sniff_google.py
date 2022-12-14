from scapy.all import *

def findGoogle(pkt):
    if pkt.haslayer(Raw):
        payload - pkt.getlayer(Raw).load
        if 'GET' in payload:
            if 'google' in payload:
                r = re.findall(r'(?!)\&q=(.*?)\&', payload)
                if r:
                    search = r[0].split('&')[0]
                    search = search.replace('q=', '').replace('+',' ').replace('%20', '')
                    print('[+] Searched For: ', search)
                    
def main():
    parser = OptionParser('usage %prog -i <interface>')
    parser.add_option('-i', dest = 'interface', type = 'string', help = 'Specify interface to listen on')
    (options, args) = parser.parse_args()
    if options.interface == None:
        (options, args) = parser.parse_args(["-h"])
    else:
        conf.iface = options.interface
    try:
        print('[*] Starting Google Sniffer')
        sniff(filter = 'tcp port 80', prn=findGoogle)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
