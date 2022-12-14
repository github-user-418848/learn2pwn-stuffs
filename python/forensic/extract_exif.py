from optparse import OptionParser
from os.path import basename
from PIL import Image
from PIL.ExifTags import TAGS
import subprocess

def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print('[+] ', imgFileName, ' contains GPS MetaData')
                print('[*] Opening exiftool.exe...')
                sendCmd = '''exiftool.exe "''' + imgFileName + '''"'''
                subprocess.run(sendCmd, shell = True)
    except:
        print('[-] ', imgFileName, ' does not contain any GPS MetaData')

def main():
    parser = OptionParser()
    parser.add_option("-u", dest = "url", help = "Specify the filename of the image", type = "string")
    (options, args) = parser.parse_args()
    if (options.url == None):
        (options, args) = parser.parse_args(["-h"])
    else:
        url = options.url
        testForExif(url)

if __name__ == '__main__':
    main()
