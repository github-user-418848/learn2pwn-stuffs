from fileinput import filename
from optparse import OptionParser
import sys, sqlite3, os

greenColor="\033[1;32;40m"

def open(db):
    conn = sqlite3.connect(db)
    tbls = conn.cursor()
    indxs = conn.cursor()
    
    for tbl in tbls.execute('''SELECT tbl_name FROM sqlite_master WHERE type=="table"'''):
        print("+", "-"*len(tbl[0]), "+")
        print("|", tbl[0], "|")
        print("+", "-"*len(tbl[0]), "+")
        
        for col in indxs.execute("SELECT * FROM " + tbl[0]):
            for i in range(len(col)):
                if col[i]:
                    print(" --", col[i])

def main():
    
    INFO = '''
    SSSSSSSSSSSSS
    SSSSSSSSSSSSSSSSSSSSSSSSSSS
    SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS             SSSSSSSSSSS
SSSSSSSSSSSSSSS                 SSSSSSSSSSS
SSSSSSSSSSSSS        SSSSSS      SSSSSSSSSSS
SSSSSSSSSSSSS      SSSSSSSSS     SSSSSSSSSSSS
SSSSSSSSSSSS      SSSSSSSSSS    SSSSSSSSSSSSS    +------------+
SSSSSSSSSSSSS       SSSSSSSSSSSSSSSSSSSSSSSSS    | Skype Dump |
SSSSSSSSSSSSSSS         SSSSSSSSSSSSSSSSSSSSS    +------------+
SSSSSSSSSSSSSSSSSS          SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS          SSSSSSSSSSSSSS
SSSSSSSSSSSSS    SSSSSSSSS      SSSSSSSSSSSSS
SSSSSSSSSSSSS     SSSSSSSSS     SSSSSSSSSSSSS
SSSSSSSSSSSS      SSSSSSS      SSSSSSSSSSSSSS
SSSSSSSSSSSS                  SSSSSSSSSSSSSS
SSSSSSSSSSSSS              SSSSSSSSSSSSSSSS
    SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
        SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
            SSSSSSSSSSSSSSSSSSSSSSSSSSSS
                        SSSSSSSSSSSSSS
    '''

    print(INFO)

    parser = OptionParser()
    parser.add_option("-f", dest="filepath", help="Specify the path of the db file", type="string")
    (options, args) = parser.parse_args()
    
    if options.filepath:
        f = options.filepath
        open(f)
    else:
        (options.args) = parser.parse_args(["-h"])

if __name__ == '__main__':
    main()