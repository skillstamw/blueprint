import re

def find_matches(text, base_word, keywords,pattern):
    # Optimized regex pattern

    # Find all matches
    matches = re.findall(pattern, text,flags=re.IGNORECASE)
    return matches