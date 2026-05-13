import json
from os.path import exists
def write_formatted_scrape(file_name:str, 
                                    formatted_scrape:dict):
    
    assert exists(file_name), f"missing file {file_name}"

    with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
        json.dump(formatted_scrape, file)
