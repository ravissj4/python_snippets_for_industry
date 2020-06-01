from fastapi import FastAPI
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # /day5
CACHE_DIR = os.path.join(BASE_DIR, 'cache')
dataset_filepath = os.path.join(CACHE_DIR, 'movies-box-office-dataset-cleaned.csv')

app = FastAPI()

@app.get('/')
def read_root():
    return {'key' : 'Hello world'}

@app.get('/box-office-sales')
def box_office_sales():
    df = pd.read_csv(dataset_filepath)
    return df.to_dict("Rank")