# python3 -m venv .venv
import requests
import pandas as pd
import certifi

# Make a GET request to fetch the raw HTML content
url = 'https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes'
headers = {'User-Agent': 'Mozilla/5.0'}  # Some websites may require a user-agent to be specified
response = requests.get(url, headers=headers, verify=certifi.where())

# Check if the request was successful
if response.status_code == 200:
    # Use pandas to read the HTML content
    simpsons_tables = pd.read_html(response.content)
    # Now you can print the tables or do further processing
    print(simpsons_tables[1])
else:
    print(f"Failed to retrieve the webpage: Status code {response.status_code}")
