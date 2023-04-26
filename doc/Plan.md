# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
## Rewrite instructions
* For this project, I have been tasked by the same mathematician to create a web crawler program that starts from a single website, checks for other links on that site, visits those links, and checks for more links on those links, and follows this pattern until every site has been visited within a specified depth from the original site. This will be a recursive program. As it runs, it does several things:
    * print out the current URL, using indentation to show the current depth of the crawler
    * mark the URL that is about to be visited
    * use the requests library to fetch a page by URL
    * print any exceptions that are raised and return from this call of crawl
    * scan resulting html for any anchor tags
    * for each anchor tag, check elegibility and call crawl again
* This program is supposed to handle any exceptions without crashing and provide detailed information on any exception that it encounters.
* This program is also supposed to be written with pre-existing code imported from libraries. Rather than writing everything myself, I am to utilize each of these libraries to help request and parse URL's for the web crawler to use. This will help save time and effort writing code that has already been written.

*   [X] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
## What this program aims to solve
* This program's goal is to recursively search a single url for other url's and then search those url's for even more. It keeps track of its current depth from the main url and logs every new url that it visits. It simply visits as many url's as it can within the allowed maximum depth provided by the user. It doesn't do anything else with the sites except log them in a set to make sure that it doesn't count repeated sites and print them out on the console to the user. 
## A good solution
* A good solution for this program uses a few lines as necessary to achieve the recursion expected of it. It handles errors whenever they're encountered, and it only goes as deep as the maximum depth allows. It also uses FOUR SPACES instead of a TAB to show the levels of depth that the web crawler experiences. A good solution fully utilizes all of the imported libraries to their extent so that I'm borrowing as much code as I can. It also uses a set to keep track of websites that I've already been to. The web crawler function returns when it should and calls itself accordingly.
## What I know how to do
* I feel like I have a decent enough understanding of recursion to write the recursive portion of the function, so I'm honestly not super worried about that part.
* I know how to use exception handling, so that should be easy enough to implement in my program.
* I'm very familiar using sys.argv to read arguments from the command line.
* I know how to import time to record the total time that the program runs for.
## Potential challenges 
* I've never onced used any of the libraries that we'll be using to request and parse url's, so I'm a little nervous about that. I'll need to take my time to learn exactly how they work and how I'll need to implement them in my program. 
* I'm not familiar with sets, so though they don't seem too difficult at first glance, it would be wise to take some more time studying them to know how they work and how I can use them.
* Within the recursive function, I can see myself messing up the little details of not counting a page when I should have or vice versa. Not a huge deal, but I imagine it taking a bit of time to fine tune that function to be perfect. 

*   [X] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
## Data used by the program
* With this program, there isn't a lot of data that gets used. Everything is based off the initial url that the user provides. From there, the web crawler makes its way to other pages, but they all stem off of that first url given as an argument. Other libraries are imported for use in the program, but that's all that this program will be using.
## Form of the output
* The output for this program is simply a series of print statements outputted to the terminal. Starting with the initial url, it prints out every url that the web crawler visits, also including any errors that occur while the web crawler runs. Each depth level away from the starting position is indented with four spaces. Once the web crawler finishes searching every url it's supposed to, a line prints to the terminal giving the total number of unique websites as well as how long it took the web crawler to run. 

*   [X] List the algorithms that will be used (but don't write them yet).
## List of algorithms to be used
* For this program, I'll be needing algorithms to:
    * Run the actual web crawler
    * Run a for loop within the web crawler that:
        * Checks all the anchor tags in an HTML document and determines if they can be crawled
        * Joins absolute and relative url's for the web crawler to crawl
        * Calls the web crawler on a new url
    * Handle any exceptions appropriately
    * Parse the url argument provided by the user to make sure that it's a valid site
    * Read command line arguments to know if the web crawler should be run or not
    * Keep track of the sites already visited using a set
    * Keep track of the amount of time that the program is running for 


*   [X] **Tag** the last commit in this phase `analyzed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
## Function signatures
* def crawl(url, depth=0, maxDepth, visited)
    * 'url' is the current url address that the function is crawling
    * 'depth' is the current depth level of the crawler from the original url (provided by the user)
    * 'maxDepth' is the maximum depth that the crawler will go (specified by the user)
    * 'visited' is a set that contains url's that have already been visited
* This is the main function of the program. It's purpose is to start with a url (provided by the user), and from there search the page for more links. After finding a link, it moves to that website, scanning for more links all while keeping track of how far away it is from the initial url and adding any visited url's into the 'visited' set. Once the crawler visits every page within the specified 'maxDepth', it stops.
* When it visits a new page, it prints out the url to the console with an indentation equal to the depth level. It also will report how many unique pages it visits as well as the time it took to complete the crawl.

*   [X] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.
## Pseudocode
```
begin timing
def crawl(url, depth, maxDepth, visited):
    if (the provided url is a valid url and not in visited) and depth<=maxDepth:
        print out the current url with an indentation equal to depth
        mark the url about to be visited as visited
        try:
            use the requests library to fetch the webpage by url
        else:
            print the failed request
            return
        scan resulting HTML for anchor tags
        for each anchor tag:
            if the tag has no 'href' attribute: continue
            discard the 'fragment' portion of url
            check if the 'href' attribute is an absolute or relative path. If relative, make it an absolute using urljoin()
            call crawl on the new url
            increment depth by 1
end timing
```
## Good and bad input
* In the face of good input, this function will work exactly as it should. It will print out each url that it visits with an indentation equal to its current depth. It will visit every website possible, skipping over previously visited sites and making use of the set. It will dynamically create absolute url's whenever it needs to, and it will not visit any invalid url's nor will it exceed its max depth. The program will also terminate upon the user entering Ctrl C and will print out its final report regardless of when Ctrl C was pressed. It might take some timing right to figure out exactly how to word and position the try/except block so that this will always happen. I'll have to give it a large maxDepth so that I'll have time to force the shutdown and make sure that the report message is always printed.

* In the face of bad input, the program should still nearly perfectly run. The only place where the bad input can cause the program to not run is if the user provides an invalid url as an argument for the program to start. Otherwise, the program will be able to handle any errors that occur while it is running. Messages will print out describing the error, but the program will continue to run. If the user does provide an invalid url, then the program will print a message explaining the error and asking the user for a valid url. The program will then quit, and the user must try again. I'll need to test multiple variations of an invalid url to make sure that the program doesn't try running with any of them (i.e. anything that doesn't start with http:// or https://).

*   [X] **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [X] More or less working code.
*   [X] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.
## Things that happened
* I would sat that the thing that surprised me the most was how quickly it all came together. Maybe I'm just used to working on larger projects now, but by the time I had finished by implementation, I was surpised that it was already done. Sure, it certainly wasn't bug-free, but it worked well enough.
* There were a few incorrect logic statements in my pseudocde that required a change during the implementation, but for the most part, I was surpised by how closely my code resembled the pseudocode. I guess that's a good thing, but with previous projects, I've had to change a lot. It was nice with this assignment.
* It was also just interesting to use requests and BeautifulSoup. These are entirely new libraries to me, and though I was a little nervous at first, I found that they were a lot easier to use than I had previously thought. 

*   [X] **Tag** the last commit in this phase `implemented` and push it to GitLab.


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [X] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
## Test cases
* The first bug that I ran into was a problem with BeautifulSoup. Because it was already part of an except block, the specifics of the error didn't print at first, but I discovered that it was because I was passing the entirety of the return value of 'r=requests.get(url)' into the BeautifulSoup parameter rather than the content of requests.get. To fix this, I changed 'BeautifulSoup(r)' to 'BeautifulSoup(r.content)' and the problem was resovled. 
* I ran into a problem where the program was printing out far more indentations than what was expected. It was continuously printing out an additional level of indentation with every url, regardless of how 'far' the current url was from the inital url. After examining my logic, I found that in my crawl function, I had told it to return whenever the depth was equal to the maxDepth. This returned only once, for every time after that, the depth would be greater than maxDepth. To fix this, I changed 'if depth == maxDepth' to 'if depth > maxDepth'. This fixed the problem.
* Another bug that I ran into was when I ran the program with fewer arguments that it takes. I realized that I was off by one with my logic in 'sys.argv'. To fix this, I added 1 to each index of sys.argv and the problem was solved.
* Once I felt that the program was bug-free, I ran it on the 'https://cs.usu.edu' url as well as the testing server. I ran it without the option 'maxDepth' argument, and each time, it ran with the default value of 3 for 'maxDepth'.
* I tried running the program with invalid url's, and each time it printed out the USAGE error asking for an absolute url.
* I ran the program several times with no arguments, and each time it printed out messages explaining how to run the program.
* Each time I ran the program with an invalid 'maxDepth' argument, it reverted back to the default value of 3.
* The last test case that I repeatedly tested was using 'Ctrl^C' to exit the program while it was running. I got this to work every time while still printing the results regardless of how the program was terminated.

*   [X] **Tag** the last commit in this phase `tested` and push it to GitLab.


## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] **Tag** the last commit in this phase `deployed` and push it to GitLab.
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Look for all of the tags in the **Tags** tab.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
