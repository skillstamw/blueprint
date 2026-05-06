def hello():
    print("hello")
def pre_process_scrape(text):

    text=text.lower().replace('"',"'")

    return text