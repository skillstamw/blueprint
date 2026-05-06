from os.path import join
from scrape.validate_url import validate_url
from scrape.get_scrape  import get_scrape
from scrape.get_formatted_scrape import get_formatted_scrape

def scrape_url_sequence(url_sequence,store_path,cat_sequence=None):

    formatted_scrape_sequence=[]
    index_cat=0
    index_faulty=0
    for url in url_sequence:

        try:

            validate_url(url)

            scraped_text=get_scrape(url=url)
        
            formatted_scrape=get_formatted_scrape(text=scraped_text,
                                                url=url)
            
            if isinstance(cat_sequence,list):
                formatted_scrape.update({"category":cat_sequence[index_cat]})

            scrape_id=formatted_scrape["id"]

            time_stamp=formatted_scrape["format_time"]

            sha=formatted_scrape["sha"]
            
            formatted_scrape_file_name=get_formatted_scrape_file_name(scrape_id=scrape_id,
                                                                    time_stamp=time_stamp)
            
            full_formatted_scrape_file_name=join(store_path,formatted_scrape_file_name)
            
            with open(full_formatted_scrape_file_name, 'w', encoding="utf-8") as formatted_scrape_file:

                json.dump(obj=formatted_scrape,fp=formatted_scrape_file)
            
            #print(f"formatted_scrape {formatted_scrape}")

            formatted_scrape_sequence.append(formatted_scrape)

        except Exception as e:
            index_faulty+=1
            print(f"Error {index_faulty} of {len(url_sequence)}: {e} encountered for url {url}")
        
        index_cat+=1
