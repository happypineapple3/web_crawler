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
import traceback
INDENTATION = '    '
  	  
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
        r = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        print(requests.exceptions.RequestException)
        return
    
    try:
        soup = BeautifulSoup(r.content, 'html.parser')
        anchors = soup.find_all('a', href=True)
    except not KeyboardInterrupt:
        traceback.print_tb()
        return
    
    for link in anchors:
        new_URL = link['href']
        defragged = urldefrag(new_URL)
        joined_URL = urljoin(url, str(defragged.url))
        crawl(joined_URL, depth+1, maxDepth, visited)

    return  	  	  


# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool  	  	  
if __name__ == "__main__":  	  	  

    ## If no arguments are given...  	  	  
    if len(sys.argv) < 2:  	  	  
        print("USAGE: Please provide at least the absolute url of the site you want me to crawl from.", file=sys.stderr)
        print("An absolute url begins with either 'https://' or 'http://'")
        print("You may also provide an optional 'maxDepth' value that is greater than 0.")	  	  
        exit(0)  	  	  
    else:
        parse = urlparse(sys.argv[1])
        if parse.scheme != 'https' and parse.scheme != 'http':
            print("USAGE. Please provide an absolute url.\nAn absolute url begins with either 'https://' or 'http://'")
            sys.exit(1)
        url = sys.argv[1]

    maxDepth = 3
    visited = set('https://www.tripadvisor.com/')


    if len(sys.argv) >= 3 and int(sys.argv[2]) >= 0:
        maxDepth = int(sys.argv[2]) 	  	  
    
    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")  	  	  

    before = time.time()

    try:
        crawl(url=url, depth=0, maxDepth=maxDepth, set=visited)
    except KeyboardInterrupt:
        print("Exiting...")
        time.sleep(1)
    finally:
        after = time.time()
        totalTime = after-before
        print("Thanks to the wonderful programmer who designed me, I can give you a report of my crawl.")
        print(f"it took me {totalTime.__round__(2)} seconds to traverse {len(visited)} website(s). You're welcome.")
        sys.exit(1)
	  	  
