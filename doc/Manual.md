# Recursive Web Crawler User Manual

*   This is the **user manual**, not the **programmer's manual**
    *   Keep your instructions at a user-friendly level.
*   Explain how to run the program
    *   What is the name of the main program file?
    *   What command-line arguments are needed?
*   What output does the program produce?
    *   What is shown when the program works correctly?
    *   What is shown when an error is encountered
    *   Provide examples of both!
*   This block of instructions does not belong in the finished product
    *   Delete this before turning it in


## How to setup
Before this program can be run, it is necessary for the user to run the following command from anywhere in the terminal:
' python -m pip install --user -r requirements.txt '
If an error occurs with this command, try replacing 'python' with 'python3'. This will download necessary files that the program uses. If this step is skipped, then the program will not run properly until the user runs the above command.

## How to run
Before reading this section, make sure that all of the steps listed in 'How to setup' have been followed exactly as written.

Now that everything has been installed, the program is ready to run! First, the user must navigate to the main repository where the program is stored. Once there, the user must type
'python src/crawler.py [URL] [MAX_DEPTH]'
where the 'URL' is an absolute URL (see definition of an absolute URL below) that the web crawler starts with and 'MAX_DEPTH' is any integer (whole number) that isn't negative that tells the program the maximum number of pages away from the initial page the crawler can search. For example, if a search were being performed starting with the absolute URL 'https://cs.usu.edu' with a maximum depth of 3, then the command to run the program woud be:
'python src/crawler.py https://cs.usu.edu 3'
This will start the web crawler on the page 'https://cs.usu.edu' and tell it to search every site up to three sites away from the original.

Increasing the 'MAX_DEPTH' paramter will drastically affect how long the program takes to run. If its value is set to 0, then only one page is actually crawled -- the initial page provided by the user. If it is 1, then it will crawl every URL that it has access to from the initial 'URL'. For explanation purposes, let's say that each page that this program will ever crawl has exactly three URL's. We can form the mathematical expression: # of pages = 3^'MAX_DEPTH'. This is an exponential function. The total number of pages crawled from numbers 0-6 would be:
0:1
1:3
2:9
3:27
4:81
5:243
6:729
Actual sites will have varying amounts of URL's on them, but the point remains the same. With each increased 'MAX_DEPTH', the total number of pages crawled increases expontentially, increasing the time needed to crawl over each page. 

If the command 'python src/crawler.py' is run without any commands, then a message will print to the screen explaining how the program is meant to be run. If the program is run with only the URL being provided, then a default 'MAX_DEPTH' of 3 will be provided for the program. If the URL provided is not an absolute URL (see definition of an absolute URL below), then an error message will appear, and the program will quit.

An absolute URL is one that begins with either 'http://' or 'https://'. *Only* these types of URL's are accepted by the program as its initial 'URL'. For example, in the above demonstration of starting with the website 'https://cs.usu.edu', it is an accepted URL because it begins with 'https://'. It is an absoulte URL. A non-absolute URL would be a relative URL. A relative URL does *not* begin with 'http://' or 'https://'. A relative URL could look like: 'cs.usu.edu' while its counterpart absolute URL would look like: 'https://cs.usu.edu'. The difference is very technical, but the program will *not* work if the given initial 'URL' is not an absolute URL.

## What the user will see
Once the user has run the program with valid argument(s), then the program will begin to run. It starts by printing out the initial 'URL' to the terminal, and from there, it prints out every URL that it visits. With each increasing depth level, an indentation is added to the line, showing how far away from the current URL is from the initial 'URL'. Take a look at the following example:

```
python src/crawler.py http://127.0.0.1:8000/breadth=1/depth=10 5
Crawling from http://127.0.0.1:8000/breadth=1/depth=10 to a maximum distance of 5 links
http://127.0.0.1:8000/breadth=1/depth=10
    http://127.0.0.1:8000/
        http://127.0.0.1:8000/deadend
        http://127.0.0.1:8000/a
            http://127.0.0.1:8000/aa
                http://127.0.0.1:8000/aaa
                    http://127.0.0.1:8000/aaaa
Visited 7 unique pages in 0.1069 seconds
```
On the first line, the program is given its initial 'URL' and 'MAX_DEPTH'. The program prints a message explaining where it's starting and how deep it will go, and then it proceeds to visit all the pages it can. Notice that the indentation is increasing with each level the crawler goes. If you count the number of times the indentation changes, you'll see that it changes 5 times, the number specified as the 'MAX_DEPTH'. Once finished, the program prints out how many different URL's it visited and the time it took for the program to run. 

There is a chance that one of the URL's being visited will be invalid. In this case, an error will print to the screen explaining that the desired URL is unreachable. The program will then continue to run as if nothing happened. 

## Errors that may occur
In this program, there are very few errors that can occur. The first is if the user provides an initial 'URL' that is invalid (i.e. not an absolute URL) (see what constitutes a valid URL in the section 'How to run'). An error message will be printed to the terminal explaining the error and what the user can do to fix it. The program will then quit. 

Another error that can occur is when the web crawler finds a page that it cannot visit. It will print out an error message detailing what went wrong and for which page, but it will continue to run afterwards. An error message like this might look something like:
```
            http://catalog.usu.edu/content.php?catoid=4&navoid=546
Requests or BeautifulSoup ctor() HTTPSConnectionPool(host='catalog.usu.edu', port=443): Max retries exceeded with url: /content.php?catoid=4&navoid=546 (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines','tls_process_server_certificate', 'certificate verify       failed')])")))
            http://www.usu.edu/arc/tutoring/
            http://www.usu.edu/arc/
```
Notice how the error message doesn not follow the same level of indentation as the other pages that the crawler visited. It explains what went wrong and then continues to run.

