import requests
from bs4 import BeautifulSoup
def get_scrape(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the URL: {url}")
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract text from the HTML
    text = soup.get_text(separator=" ")
    return text