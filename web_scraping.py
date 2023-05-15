import requests
from bs4 import BeautifulSoup

def get_main_headings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all main headings
    main_headings = soup.find_all(['h1', 'h2', 'h3'])

    # Extract text from each heading
    main_headings = [heading.text.strip() for heading in main_headings]

    return main_headings

# Replace the URL with the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
headings = get_main_headings(url)

for heading in headings:
    print(heading)
