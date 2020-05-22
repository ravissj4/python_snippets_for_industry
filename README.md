# python_snippets_for_industry

Day 1 : Web-scrapping
* some websites do provide APIs to access and grab data. 
* some websites allow third party apps to do that. 
* some websites don't allow any of the above two -> manually scrape data.

* Can be done by many libraries in python like beautiful soup, requests-html, etc.
* requests-html is the more preferred one and hence I explore it here. 
* concepts such as grabbing data by class or id selectors, saving data to csv via pandas, extending the code to fetch data from multiple pages via dynamic change in urls, etc.


Day 2 : Learning how to use REST APIs 
* websites that do provide APIs for grabbing their data generally also give proper documentation to do so, if not, then our work becomes harder. 
* sometimes we might need to do both, themoviedb.org does not have box office sales data, for that we again need to scrape from boxofficemojo.com, and then combine these two datasets into one csv file for analysis.
* the stripes api takes us one step even further but it adds a whole new level of complexity(how to collect the credit card information securely).
* Another cool thing to do is to make a website which allows a user to grab data in directly through a very easy interface with these REST API calls at the backend. 


Day 3 : Web Appication with Flask and Fast API using ngrok and invictify

Some commands to learn : 
install pipenv - 
python3 -m pip install pipenv

create virtual environment inside the relevant folder only and activate a subshell inside that - 
pipenv shell --python 3.8

reactivate subshell in the virtual env - 
pipenv shell

install required packages - 
pipenv install flask gunicorn uvicorn fastapi

after writing code for the server, run the server(flask) - 
gunicorn module_name:app_name 
eg : gunicorn server1:app

after writing code for the server, run the server(fastapi) - 
gunicorn module_name:app_name 
eg : uvicorn server1:app

# ngrok : 
* can use a live production server in place of ngrok 

# invictify.com 
* webhook - one webapplication talking to another webapplication and sending some data there
* can use celery and reddis in place of invictify. 

Things we need to be sure of :
1. That the server is running on local machine
2. That ngrok is also running on the local machine and that urls are mapped