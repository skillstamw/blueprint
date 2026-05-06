from uuid import UUID

def get_formatted_scrape_file_name(scrape_id:UUID,time_stamp):

    return f"scrape_{str(scrape_id).replace("-","_")}_{time_stamp}.json"

def hello():
    print("is it me you're waiting for?")