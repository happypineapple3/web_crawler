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

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.
*   [ ] **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.


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
