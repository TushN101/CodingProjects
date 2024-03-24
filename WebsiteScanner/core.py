import requests
from urllib.parse import urlparse

def normalize_url(url):
    parsed_url = urlparse(url)
    if parsed_url.path.endswith('/'):
        # Remove trailing slash if present
        return parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path[:-1]
    else:
        return url

def scanning(url, wordlist):
    normalized_url = normalize_url(url)
    with open(wordlist, 'r') as f:
        for line in f:
            word = line.strip()
            full_url = f"{normalized_url}/{word}"
            response = requests.get(full_url)
            print(f"Requested: {full_url}")
            if response.status_code == 200:
                print(f"Found: {full_url}")

def main():
    website_url = input("Enter the website URL: ")
    wordlist = input("Enter the wordlist file path: ")

    scanning(website_url, wordlist)

if __name__ == "__main__":
    main()
