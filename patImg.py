#   This program is used to download patent images from the Google API and then return their metadata
#   The steps are as follows:
#   (1) generate URL's based on Patent Number and Grant Number (taken from a CSV file)
#   (2) download images from the URL (to ~/images/<PatentNumber>)
#   (3) use PIL* to get the image's natural width and height (in px)
#   (4) use os.stat to get the image's file size (in bytes)
#   (5) store results in a CSV file formatted like--
#        '''
#        Patent,Width,Height,FileSz
#        500000,3080,3005,214
#        500001,2036,2063,80.4
#        '''
#
#   *Download PIL: http://pillow.readthedocs.io/en/3.4.x/installation.html
#   Sample data:
#   https://patentimages.storage.googleapis.com/USD500000S1/USD0500000-20041221-D00000.png
#   https://patentimages.storage.googleapis.com/USD500001S1/USD0500001-20041221-D00000.png
#       https://patentimages.storage.googleapis.com/USDPatentNS1/USD0PatentN-GrantDt-D00000.png
#
#   Contributors: Jay Syz

import os
import urllib.request
from PIL import Image
import csv

def getDim(img):
    with Image.open(img) as i:
        return i.size

def getSize(img):
    stats = os.stat(img)
    return stats.st_size

def getURL(pN, gN):
    return "https://patentimages.storage.googleapis.com/USD" + pN + "S1/USD0" + pN + "-" + gN + "-D00000.png"

'''Returns a list of all patent and grant numbers from a CSV file -- [[patentN1, grantN1], [patentN2, grantN2], ...]'''
def getPNGN(cFile):
    pN = ""
    gN = ""
    arr = []
    with open(cFile, newline='') as csvfile:
        reader = csv.reader(csvfile)
        iterReader = iter(reader)
        next(iterReader)
        for row in iterReader:
            pN = row[0]
            gN = row[1]
            arr.append([pN, gN])
    return arr

'''main method'''
def main():
    results = [['Patent','Width','Height','FileSz']]
    num = 1

    for entry in getPNGN("pngdEx.csv"):
        #download the file
        urllib.request.urlretrieve(getURL(entry[0], entry[1]), "images/" + entry[0] + ".png")
        fPath = "images/" + entry[0] + ".png"
        #get dimensions
        (width, height) = getDim(fPath)
        #get size
        size = getSize(fPath)
        res = [entry[0], str(width), str(height), str(size)]
        results.append(res)
        num += 1

    #write results to the csv file
    file_writer = csv.writer(open('results.csv', 'w', newline=''))
    for x in results:
        file_writer.writerow(x)


if __name__ == '__main__':
    main()
