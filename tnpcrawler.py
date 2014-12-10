from urllib2 import urlopen, URLError
from BeautifulSoup import BeautifulSoup as soup
import re

url = "http://www.tp.iitkgp.ernet.in/notice/notice.php?sr_no="

def main():
    for i in range(13380, 13500):
        URL = url+str(i)
        try :
            # print "trying to open: ",URL
            page = urlopen(URL).read()
            head = soup(page).findAll('b')

            # if 'ctc' in head:
            #     print soup(page)
            heading = re.search('(<b>)([\W\w]*)(</b>)',str(head[0])).group(2)
            print i
            if any(i in heading.lower() for i in ["bosch","rbei","result","day 3","day three"]): # Add whatever you are looking for in this list
                print URL
                print heading, head[1], str(i)
                print
                # print soup(page)
                # print head
                # print "\n\n"

        except URLError:
            pass

if __name__ == '__main__':
    main()
