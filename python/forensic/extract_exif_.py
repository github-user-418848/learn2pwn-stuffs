import urllib
from optparse import OptionParser
from urlparse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

def findImage(url):
    print('[+] Finding images on: ', url)
    urlContent = urllib2.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

def downloadImage(imgTag):
    try:
        print('[+] Downloading Image...')
        imgSrc = imgTag['src']
        imgContent = urllib2.urlopen(imgStc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''

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
               print('[*] ', imgFileName, ' contains GPS MetaData')
    except:
        pass

def main():
    parser = OptionParser()
    parser.add_option("-u", dest = "url", help = "Specify the url of the image", type = "string")
    (options, args) = parser.parse_args()
    if (options.url == None):
        (options, args) = parser.parse_args(["-h"])
    else:
        url = options.url
        imgTags = findImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
        testForExif(url)

if __name__ == '__main__':
    main()
