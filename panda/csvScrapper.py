import pandas as pd
import requests
from io import StringIO
import certifi

# URL of the CSV file
url = 'https://www.football-data.co.uk/mmz4281/2324/E0.csv'

# The local path where you want to save the CSV file
local_file_path = 'scrapedData/england.csv'

# Make a GET request to fetch the raw CSV content
response = requests.get(url, verify=certifi.where())

# Check if the request was successful
if response.status_code == 200:
    # Read the CSV content from the response using StringIO
    df = pd.read_csv(StringIO(response.text))

    # Rename the columns as desired
    df.rename(columns={'FTHG': 'NewName1', 'FTAG': 'NewName2'}, inplace=True)

    # Save the DataFrame to a CSV file locally
    df.to_csv(local_file_path, index=False)
    print(f"The file has been saved to: {local_file_path}")
else:
    print(f"Failed to retrieve the CSV file: Status code {response.status_code}")
