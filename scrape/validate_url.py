from urllib.parse import urlparse
def validate_url(url):
    #TODO use hydra for asserts
    parsed = urlparse(url)
    
    # Assert the scheme (e.g., http, https) is valid
    assert parsed.scheme in ['http', 'https'], f"Invalid scheme: {parsed.scheme}"
    
    # Assert the network location (domain) is non-empty
    assert parsed.netloc, "URL must have a network location (domain)."
    
    # Optional: Assert the path (e.g., /some/page) is valid
    assert parsed.path.startswith('/'), f"Invalid path: {parsed.path}"
    
    # Optional: Assert the URL is not empty
    assert url.strip(), "URL cannot be empty or just whitespace."

    return True
