from scrape.get_scrape import get_scrape
import re
# Function to scrape a URL and count word occurrences
def scrape_and_count(url:str,words:list):
    # Fetch the webpage
    text=get_scrape(url=url)

    # Calculate the total length of the text
    text_length = len(text)
    
    # Prepare regex pattern for word matching (handles singular/plural forms)
    # Adding word boundaries to match whole words and common endings
    patterns = [r"\b{word}(s|ed|ing|es|ial|ive|y|ies)?\b" for word in words]
    full_pattern = re.compile("|".join(patterns), re.IGNORECASE)
    
    # Count occurrences of words
    matches = full_pattern.findall(text)
    word_count = len(matches)
    
    return word_count, text_length