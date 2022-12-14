import PyPDF2
from PyPDF2 import PdfFileReader
from optparse import OptionParser

def PrintMeta(fileName):
    pdfFile = PdfFileReader(fileName, 'rb')
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF MetaData For: ', str(fileName))
    for metaItem in docInfo:
        print(metaItem, ':', docInfo[metaItem])

def main():
    parser = OptionParser()
    parser.add_option("-f", dest = "fileName", help = "Specify the file name", type = "string")
    (options, args) = parser.parse_args()
    if (options.fileName == None):
        (options, args) = parser.parse_args(["-h"])
    else:
        fileName = options.fileName
    PrintMeta(fileName)

if __name__ == '__main__':
    main()
