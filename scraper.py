# pip install requests beautifulsoup4

# send HTTP requests and download webpage content.
import requests

# Imports BeautifulSoup from the bs4 library to parse and extract data from HTML.
# Parsing a webpage means taking its raw, unstructured code (like HTML) and breaking it down into a structured, easily readable format
from bs4 import BeautifulSoup

# User-Agent - Mimics a real web browser (Chrome on macOS) so the target website does not block the script as an automated bot.
# Accept - script expects HTML content in response.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

def fetch_website_contents(url):
    # add scheme if the user forgot it
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Could not fetch the website. Error: {e}"

    # Converts the raw HTML text from the response into a structured, searchable Python object using the built-in HTML parser.
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title found"

    # Completely removes those selected tags and their contents from the HTML structure.
    for tag in soup(["script", "style", "nav", "footer", "header", "img", "input"]):
        tag.decompose()

    # Extracts all remaining visible text from the page, separating different paragraphs with a newline character and removing extra blank spaces.
    text = soup.get_text(separator="\n", strip=True)
    return f"Title: {title}\n\nPage contents:\n{text}"