import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrapes data from the given URL and extracts relevant information."""

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    # Customize this part to extract the specific information you need
    # Replace these placeholders with appropriate selectors for your target website
    titles = soup.find_all("h3", class_="title")
    descriptions = soup.find_all("p", class_="description")

    extracted_data = []
    for title, description in zip(titles, descriptions):
        data = {
            "title": title.text.strip(),
            "description": description.text.strip()
        }
        extracted_data.append(data)

    return extracted_data

# Example usage:
target_url = "https://example.com"  # Replace with the actual URL you want to scrape
data = scrape_website(target_url)

if data:
    print(data)  # Print the extracted data
else:
    print("No data could be extracted.")
