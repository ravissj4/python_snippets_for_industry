from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import  
app = FastAPI()

# # http://localhost:8000/
# @app.get('/')
# def hello_world():
#     return {'hello' : 'world'}

# # http://localhost:8000/abv
# @app.get('/abv')
# def hello_world_abc():
#     return {'data' : [1,3,4]}

# http://localhost:8000/box-office-mojo-scrapper
@app.post('/box-office-mojo-scrapper')
def scrape_runner_view():
    trigger_log_save()
    scrape_runner()
    return {'data' : [1,3,4]}