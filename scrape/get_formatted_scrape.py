from uuid import uuid4, UUID
from os.path import exists
from filter.get_sha import get_sha
from get_time_stamp import get_time_stamp
import json

def get_formatted_scrape(text:str,
                 url:str,
                 scrape_id=uuid4()):

    formatted_scrape={"id":str(scrape_id),
                        "url":url,
                        "body":text,
                        "sha":get_sha(text),
                        "format_time":get_time_stamp()}

    return formatted_scrape

def get_formatted_scrape_file_name(scrape_id:UUID,time_stamp):

    return f"scrape_{str(scrape_id).replace("-","_")}_{time_stamp}.json"