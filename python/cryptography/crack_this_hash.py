from optparse import OptionParser
import hashlib, time

def crackThis(hashcode, wordlst):
    wordResult = "No match found"
    wordlstPath = str(open(wordlst).read())
    wordLength = len(wordlstPath.split('\n'))
    print("List Count: ", wordLength, " words")
    num = 0
    for words in wordlstPath.split('\n'):
        if hashlib.sha1(bytes(words, 'utf-8')).hexdigest() == hashcode:
            wordResult = str(words)
            break
        if hashlib.sha256(bytes(words, 'utf-8')).hexdigest() == hashcode:
            wordResult = str(words)
            break
        if hashlib.sha384(bytes(words, 'utf-8')).hexdigest() == hashcode:
            wordResult = str(words)
            break
        if hashlib.sha512(bytes(words, 'utf-8')).hexdigest() == hashcode:
            wordResult = str(words)
            break
        if hashlib.md5(bytes(words, 'utf-8')).hexdigest() == hashcode:
            wordResult = str(words)
            break
        if hashlib.blake2b(bytes(words, 'utf-8')).hexdigest() == hashcode:
            wordResult = str(words)
            break
        if hashlib.blake2s(bytes(words, 'utf-8')).hexdigest() == hashcode:
            wordResult = str(words)
            break
        num = num + 1
        print("Scanning word ", num, " of ", wordLength, ' ' * 2, end = '\r')
    print("\nScanning Complete")
    time.sleep(1)
    print("Key: ", wordResult)
    time.sleep(1)

def main():
    usage = ("usage: %prog [SYPNOSIS] -H <hashcode> -m <hash algorithm> -w <wordlist file>" + 
    "\n\n+-----------------+\n| Hash Algorithms |\n+-----------------+\n" +
    "| 1 = SHA1        |\n| 2 = SHA256      |\n| 3 = SHA384      |\n| 4 = SHA512      |\n" +
    "| 5 = MD5         |\n| 6 = BLAKE2B     |\n| 7 = BLAKE2S     |\n+-----------------+")
    parser = OptionParser(usage)
    parser.add_option("-H", dest = "hashcode", help = "Hash code target", type = "string")
    parser.add_option("-w", dest = "wordlst", help = "Specify wordlist file location", type = "string")
    (options, args) = parser.parse_args()
    if (options.hashcode == None) | (options.wordlst == None):
        (options, args) = parser.parse_args(["-h"])
    else:
        hashcode = options.hashcode
        wordlst = options.wordlst
    crackThis(hashcode, wordlst)
    print("Time Elapsed: ", time.perf_counter())
    
if __name__ == '__main__':
    main()
