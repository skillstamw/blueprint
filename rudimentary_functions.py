#assert False, "make sure that scrape files are store in the correct folder, then continue. "
def print_hello_blue_print():
    print("hello blueprint")
import re
import requests
from bs4 import BeautifulSoup

# # List of target words
# words = [
#     "algorithm", "artificial", "intelligence", "uncertain", "prediction", 
#     "loss", "model", "definition", "parameter", "solution", "derived", "application",
#     "declare", "code", "data", "result", "variability", "variance", 
#     "variation", "power", "significance", "hypothesis", "theory", "available"
# ]



# import requests
# import io
# import PyPDF2
# def get_scrape_pdf(url):

#     #url = "https://arxiv.org/pdf/astro-ph/0204451"

#     print("d015289f-0d1a-40f6-abd7-4eb9e9fc4300")

#     # Fetch the PDF from the internet
#     response = requests.get(url)
#     #response.raise_for_status()  # ensures request succeeded

#     if response.status_code != 200:
#         raise Exception(f"Failed {response.status_code} to fetch the URL: {url}")

#     # Load PDF from memory (not from disk)
#     pdf_file = io.BytesIO(response.content)

#     # Parse the PDF
#     reader = PyPDF2.PdfReader(pdf_file)

#     all_text = ""
#     for page in reader.pages:
#         text = page.extract_text()
#         if text:
#             all_text += text


#     return all_text


# def pre_process_scrape(text):

#     text=text.lower().replace('"',"'")

# from datetime import datetime, timezone

# def get_time_stamp():
#     timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
#     return timestamp





# def write_formatted_scrape_sequence(file_name:str, 
#                                     formatted_scrape_sequence):
#     assert exists(file_name), f"missing file {file_name}"

#     with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
#         json.dump(formatted_scrape_sequence, file)






# def scrape_url_sequence_pdf(url_sequence,store_path,cat_sequence=None):

#     formatted_scrape_sequence=[]
#     index_cat=0
#     index_faulty=0
#     for url in url_sequence:

#         try:

#             validate_url(url)

#             scraped_text=get_scrape_pdf(url=url)
        
#             formatted_scrape=get_formatted_scrape(text=scraped_text,
#                                                 url=url)
           
#             if isinstance(cat_sequence,list):
#                 formatted_scrape.update({"category":cat_sequence[index_cat]})

#             scrape_id=formatted_scrape["id"]

#             time_stamp=formatted_scrape["format_time"]

#             sha=formatted_scrape["sha"]
            
#             formatted_scrape_file_name=get_formatted_scrape_file_name(scrape_id=scrape_id,
#                                                                     time_stamp=time_stamp)
            
#             full_formatted_scrape_file_name=join(store_path,formatted_scrape_file_name)
            
#             with open(full_formatted_scrape_file_name, 'w', encoding="utf-8") as formatted_scrape_file:

#                 json.dump(obj=formatted_scrape,fp=formatted_scrape_file)
            
#             #print(f"formatted_scrape {formatted_scrape}")

#             formatted_scrape_sequence.append(formatted_scrape)

#         except Exception as e:
#             index_faulty+=1
#             print(f"Error {index_faulty} of {len(url_sequence)}: {e} encountered for url {url}")
        
#         index_cat+=1
