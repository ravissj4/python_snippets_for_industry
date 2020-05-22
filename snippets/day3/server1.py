import os
import datetime
from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_save

app = Flask(__name__)

# # http://localhost:8000/
# @app.route("/", methods=['GET'])
# def hello_world():
#     # other code goes here
#     return "hello, world, I am flask"

# # http://localhost:8000/abc
# @app.route("/abc", methods=['GET'])
# def hello_world_abc():
#     # other code goes here
#     return "hello, world, again, I am flask"

# # using the get method just to check if things are running okay at local
# # http://localhost:8000/box-office-mojo-scrapper
# @app.route("/box-office-mojo-scrapper", methods=['GET'])
# def box_office_mojo_scrapper_view():
#     # other code goes here
#     scrape_runner()

#     return "Done"

# http://localhost:8000/box-office-mojo-scrapper
@app.route("/box-office-mojo-scrapper", methods=['POST'])
def box_office_mojo_scrapper_view():
    # other code goes here
    trigger_log_save()
    scrape_runner()
    return {'data' : [1,2,3]}