import requests
from requests_html import HTML 
import datetime
import pandas as pd
import os
import sys

BASE_DIR = os.path.dirname(__file__)

def url_to_txt(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_text = response.text
        # if save:
        #     with open(f'world-{year}.html', 'w') as f:
        #         f.write(html_text)
        return html_text
    
    return None
    
# I have created a list of lists
# alternatively a list of dicts could have been creted 
# where key = header names and values = a row of values
def parse_and_extract(url, name='2020'):
    header_names = []
    table_data = []
    # table_data_dicts = []
    html_text = url_to_txt(url)
    if html_text == None:
        return False
    r_html = HTML(html=html_text)
    # table_class = "a-section imdb-scroll-table mojo-gutter imdb-scroll-table-styles"
    table_class = '.imdb-scroll-table'
    # table_class = "#table"
    # now play with the html text
    r_table = r_html.find(table_class)
    if len(r_table) == 0:
        return False
    # print(type(r_table))
    parsed_table = r_table[0]
    rows = parsed_table.find('tr')

    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [col.text for col in header_cols]


    data_rows = rows[1:]
    for row in data_rows:
        cols = row.find('td')
        # print(cols)
        row_data = []
        # row_dict_data = {}
        for col in cols:
            # print(col.text)
            # header_name = header_names[i]
            row_data.append(col.text)
            # row_dict_data[header_name] = col.text
        # table_data_dicts.append(row_dict_data)
        table_data.append(row_data)

    # print(header_names)
    # print(rows_list)

    df = pd.DataFrame(data=table_data, columns=header_names)

    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join('data', f'{name}.csv')
    df.to_csv(filepath, index=False)
    return True

def run(start_year=None, years_ago=0):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year

    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f'{start_year}') == 4

    for i in range(0, years_ago+1):
        url = f'https://www.boxofficemojo.com/year/world/{start_year}'
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"{start_year} finished")
        else:
            print(f"{start_year} not finished")
        start_year -= 1

if __name__ == "__main__":
    
    try:
        startyear = int(sys.argv[1])
    except:
        startyear = None
    try:
        yearsago = int(sys.argv[2])
    except:
        yearsago = None
    run(startyear, yearsago)

