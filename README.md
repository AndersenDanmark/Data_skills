# Data_Skills
Web scraper for indeed job search to reveal the data scientist required skills keywords

When I’m preparing my resume to look for a data scientist job, what skills do you need to be a data scientist? Or, what skills are the companies looking for? I tried to answer these questions by looking up the job posts on indeed.com with web scraping. I collected all data scientist job posts’ requirements on data science skills from six cities, San Francisco, New York, Seattle, Austin, Chicago and Detroit.

I build a web scraper with Beautifulsoup and selenium’s python package. After collecting all job posts’ urls with requests, I use selenium to automate Firefox (PhantomJS also works but I like to view the browser directly) to load the urls due to the indeed’s Ajax; then parse the webdriver’s page source with beautifulsoup. And the beautifulsoup object will be cleaned and after text processing only data science skill keywords will be extracted. Then I count the frequency of each skill keyword and divide them by the total jobs found.
In version 1, job posts’ urls were collected with Requests package.
In version 2, job posts’ urls were collected by directly clicking the links in Firefox controlled by selenium.
For San Francisco, 2946 jobs are found and 40 keywords found, the top five required skills are Python, R, Hadoop, SQL, Java
For New York, 3263 jobs are found and 37 keywords found, the top five required skills are R, Python, Excel, SQL, C++
For Seattle, 1654 jobs are found and 35 keywords found, the top five required skills are R, Java, Python, SQL, Spark
For Austin, 285 jobs are found and 30 keywords found, the top five required skills are Python, Java, R, SQL, SAS
For Chicago, 798 jobs are found and 40 keywords found, the top five required skills are Python, Java, R, SAS, Hadoop
For Detroit, 358 jobs are found and 23 keywords found, the top five required skills are SQL, R, SAS, Matlab, Excel

Below is a pic of the percentage of the skills being looked for at San Francisco, New York and Seattle. Blue for New York, orange for San Francisco and green for Seattle.
I gathered the data and stored them as a csv file. 

Different cities prefer different data science skills and the requirements varies over time, the results I present here are for April 2016. Besides, the data scientist title includes positions for data analyst and data engineer, and different kinds of companies put different emphasis on the skills.
