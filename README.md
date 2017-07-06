# PatentImages

### Python 3 program that downloads images from the Google API and analyzes their metadata.

The steps the program takes are as follows:
1. generate URL's based on Patent Number and Grant Number (taken from a CSV file)
2. download images from the URL (to ~/images/<PatentNumber>)
3. use PIL* to get the image's natural width and height (in px)
4. use os.stat to get the image's file size (in bytes)
5. store results in a CSV file formatted like--

```
Patent,Width,Height,FileSz
500000,3080,3005,214
500001,2036,2063,80.4
```


*Download [PIL](http://pillow.readthedocs.io/en/3.4.x/installation.html)

Sample data:

https://patentimages.storage.googleapis.com/USD500000S1/USD0500000-20041221-D00000.png
https://patentimages.storage.googleapis.com/USD500001S1/USD0500001-20041221-D00000.png
https://patentimages.storage.googleapis.com/USDPatentNS1/USD0PatentN-GrantDt-D00000.png

**Feel free to download the program and use it for yourself!**
