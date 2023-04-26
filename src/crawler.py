#!/usr/bin/python3  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag
import requests
import sys
import time
INDENTATION = '    '


# print("\tTODO: delete each TODO message as you fulfill it", file=sys.stderr)  	  	  

# print("\tTODO: Change the parameters that crawl takes.", file=sys.stderr)  	  	  
def crawl(url, depth, maxDepth, set):  	  	  
    """  	  	  
    Given an absolute URL, print each hyperlink found within the document.  	  	  
    This function will need more parameters.  	  	  

    Your task is to make this into a recursive function that follows hyperlinks  	  	  
    until one of two base cases are reached:  	  	  

    0) No new, unvisited links are found  	  	  
    1) The maximum depth of recursion is reached  	  	  
    """
    if depth > maxDepth:
        return
    if url in set:
        return
    parse = urlparse(url)
    if not parse.scheme or not parse.netloc:
        return
    
    print(INDENTATION*depth, end='')
    print(url, end='\n')
    set.add(url)

    try:
        r = requests.get(url)
    except:
        print("this did not work")
        return
    
    try:
        soup = BeautifulSoup(r.content, 'html.parser')
        anchors = soup.find_all('a', href=True)

    except:
        print('this did not work')
        return
    
    for link in anchors:

        new_URL = link['href']
        defragged = urldefrag(new_URL)
        joined_URL = urljoin(url, str(defragged.url))

        crawl(joined_URL, depth+1, maxDepth, visited)

        

    

    # print("\tTODO: Check the current depth of recursion; return now if you have gone too deep", file=sys.stderr)  	  	  
    # print("\tTODO: Print this URL with indentation indicating the current depth of recursion", file=sys.stderr)  	  	  
    # print("\tTODO: Handle exceptions raised by requests and BeautifulSoup to prevent this program from crashing", file=sys.stderr)  	  	  
    # print("\tTODO: Make a GET request with the 'requests' library", file=sys.stderr)  	  	  
    # print("\tTODO: Use BeautifulSoup to find all of the <a> tags with an 'href'", file=sys.stderr)  	  	  
    # print("\tTODO: Create an absolute address from a (possibly) relative URL", file=sys.stderr)  	  	  
    # print("\tTODO: Only HTTP or HTTPS links need be followed", file=sys.stderr)  	  	  
    # print("\tTODO: Don't just print URLs found in this document, visit them!", file=sys.stderr)  	  	  
    # print("\tTODO: Trim fragments ('#' to the end) from URLs", file=sys.stderr)  	  	  
    # print("\tTODO: Use a `set` data structure to keep track of URLs you've already visited", file=sys.stderr)  	  	  
    # print("\tTODO: Call crawl() on unvisited URLs", file=sys.stderr)  	  	  
    return  	  	  


# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool  	  	  
if __name__ == "__main__":  	  	  

    ## If no arguments are given...  	  	  
    if len(sys.argv) < 2:  	  	  
        print("Please give me some arguments, good sir", file=sys.stderr)  	  	  
        exit(0)  	  	  
    else:
        url = sys.argv[1]

    # if not url.startswith('http://') or not url.startswith('https://'):
    #     print("Please provide an absolute url.\nAn absolute url begins with either 'https://' or 'http://'")


    visited = set()

    if sys.argv[2] and int(sys.argv[2]) > 0:
        maxDepth = int(sys.argv[2]) 	  	  
        plural = 's' if maxDepth != 1 else ''

    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")  	  	  

    before = time.time()

    try:
        crawl(url=url, depth=0, maxDepth=maxDepth, set=visited)
    except KeyboardInterrupt:
        print("Man why did you quit? Is it because you set the maxDepth parameter too high? Your fault, ig...")
    finally:
        after = time.time()
        totalTime = after-before
        print("Thanks to the wonderful programmer who designed me, I can give you a report of my crawl")
        print(f"it took me {totalTime} seconds to traverse {len(visited)} website(s). You're welcome.")


    # print("\tTODO: crawl() keeps track of its max depth with a parameter, not a global!", file=sys.stderr)  	  	  
    # print("\tTODO: wrap this call to crawl() in a try/except block to catch KeyboardInterrupt", file=sys.stderr)  	  	  

    # print("\tTODO: after the program finishes for any reason, report how long it ran and the number of unique URLs visited", file=sys.stderr)  	  	  
    # print("\tTODO: are all of the TODOs deleted?", file=sys.stderr)  	  	  
