import requests
from bs4 import BeautifulSoup
import sys

# Define the URL of the news website to scrape
URL = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"

# Define a User-Agent header to mimic a browser
# (This relates to interview question 3) 
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Use a try-except block for error handling
# (This relates to interview question 9) 
try:
    # 1. Use requests to fetch HTML [cite: 8]
    response = requests.get(URL, headers=HEADERS)
    
    # Raise an exception for bad status codes (like 404, 500)
    response.raise_for_status()

    # 2. Use BeautifulSoup to parse the HTML [cite: 9]
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find headline tags. The hint suggests <h2> or title tags[cite: 9].
    # On many news sites, <h3> tags are also common for headlines.
    # We will find all <h3> tags as an example.
    # (This relates to interview question 4) 
    headlines = soup.find_all('h3')
    
    if not headlines:
        print("No headlines found using <h3> tags. You might need to inspect the website and change the tag (e.g., to 'h2').")
        sys.exit()

    # 3. Save the titles in a .txt file [cite: 9]
    with open('headlines.txt', 'w', encoding='utf-8') as f:
        for headline in headlines:
            # Get the human-readable text from the tag
            # (This relates to interview question 8) 
            title = headline.text.strip()
            
            # Write to file only if the title is not empty
            if title:
                f.write(title + '\n')

    print(f"Successfully scraped {len(headlines)} headlines and saved to headlines.txt")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
except Exception as e:
    print(f"An error occurred: {e}")