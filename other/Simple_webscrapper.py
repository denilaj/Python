import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://example.com"  # Replace with the URL of the website you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract data (e.g., article titles and links)
    articles = soup.find_all('article')  # Adjust the HTML tag as per the target website's structure

    for article in articles:
        title = article.find('h2').text  # Adjust the tag for the title
        link = article.find('a')['href']  # Adjust the tag for the link

        print(f"Title: {title}")
        print(f"Link: {link}")
        print("\n")

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
