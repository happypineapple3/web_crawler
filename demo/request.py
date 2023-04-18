#!/bin/env python3  	  	  

# if this doesn't work because of a missing package, `pip3 install --user requests`  	  	  
import requests  	  	  


# This demo program illustrates the requests library  	  	  
#  	  	  
# Requests is a simple interface to making HTTP requests from a Python program.  	  	  

def demo(url):  	  	  
    try:  	  	  
        # if an error happens anywhere in this `try` block...  	  	  
        print(f"Getting {url}...")
        # requests.get() returns a Response object
        response = requests.get(url)  	  	  
        if response.ok:
            print("The response is OK ", end='')
        else:
            print("The response is NOT OK ", end='')
        print(f"[{response.status_code} '{response.reason}']")  	  	  
        i = 5  	  	  
        for line in response.text.split('\n'):  	  	  
            if i == 0:  	  	  
                print('  ...')  	  	  
                break  	  	  
            print(f"  {line}")  	  	  
            i -= 1  	  	  

    except Exception as e:  	  	  
        # ... this block of code will be run in response  	  	  
        print(f"Failed to get {url} because {e}")  	  	  

    finally:  	  	  
        # This will *always* happen, exception or no  	  	  
        print(f"All done with {url}\n\n")  	  	  


# These two requests succeed and are OK
demo('http://example.com')  	  	  
demo('https://cs.usu.edu/about/contact')  	  	  

# This request succeeds but is NOT OK
demo('http://unnovative.net/does-not-exist.html')  	  	  

# This request fails because the Requests library does not speak FTP
demo('ftp://unnovative.net/does-not-exist.html')  	  	  
