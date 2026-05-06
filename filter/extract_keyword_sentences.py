

import re
# Function to extract sentences containing both the base word and a keyword
def extract_keyword_sentences(text,pattern):
    sentences = re.findall(pattern, text, re.IGNORECASE)
    # Clean up sentences: remove newlines, extra spaces, and commas in the sentence itself
    return [sentence[0].replace('\n', ' ').replace(',', '').strip() for sentence in sentences if sentence[0]]
