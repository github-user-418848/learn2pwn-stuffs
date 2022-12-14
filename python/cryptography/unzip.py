from optparse import OptionParser
from threading import Thread
import zipfile, time, sys

def Unzip(zip_target, bunch_of_words, arch_name, verbose):
    zip_Loc = zipfile.ZipFile(zip_target)
    word_Loc = open(bunch_of_words).read()
    key = "No match found"
    words_matched = 0
    max_words = (len(word_Loc.split('\n')))
    for lines in word_Loc.split('\n'):
        try:
            words_matched = words_matched + 1
            print("Scanning word ", words_matched, " of ", max_words, ' ' * 35, end = "\r")
            zip_Loc.read(arch_name, pwd = bytes(lines, "UTF-8"))
            key = lines
            break
        except:
                print("Key: ", lines, ' ' * 30 ,end = '\r')
    print("List Count: ", max_words, ' ' * 35, "\nscanning complete\nTime Elapsed: ", time.perf_counter(), "\nKey: ", key, end = "\r" ,)
    zip_Loc.close
    
def main():
    parser = OptionParser()
    parser.add_option("-a", "--archive", dest="archive_name", help="Archive's name under zip file", type="string")
    parser.add_option("-u", "--unzip", dest="zipfile", help="Specify zip file", type="string")
    parser.add_option("-w", "--wordlist", dest="wordlistfile", help="Specify wordlist file", type="string")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default=True, help="Don't print status messages (default value: True)")
    (options, args) = parser.parse_args()
    if (options.wordlistfile == None) | (options.zipfile == None) | (options.archive_name == None):
        DisplayBanner()
        (options, args) = parser.parse_args(["-h"])
    else:
        arch_name = options.archive_name
        zip_target = options.zipfile
        bunch_of_words = options.wordlistfile
        verbose = options.verbose
    DisplayBanner()
    Unzip(zip_target, bunch_of_words, arch_name, verbose)
##    t = Thread(target = Unzip, args = (zip_target, bunch_of_words, arch_name, verbose))
##    t.start()

def DisplayBanner():
    print('''                          
+-------------------------------------------------------------------+
|    ____  _____  ____  ____  ____  ____  ____  _  _  ____  ____    |
|   |_   ||_   _||  o ||  __||  o ||  o ||  __|| || /| ___||  o |   |
|    /  /  _| |_ |  __|| |__ |   < |  _ || |__ |   < | __| |   <    |
|   |____||_____||_|   |____||_|\_\|_||_||____||_|\_\|____||_|\_\   |
|                                                                   |
+-------------------------------------------------------------------+

''')

if __name__ == '__main__':
    main()
