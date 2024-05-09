import urllib.request
import json
import re

def save(message):
    # Create a dictionary with the trail status
    data = {"message": message}

    # Write the data to a JSON file
    with open("index.json", "w") as file:
        json.dump(data, file)

    print("Trail status has been written to trail_status.json")

try:
    # Fetch the HTML content from the URL
    url = "https://www.sorbawoodstock.org/trail-status/"
    html_content = urllib.request.urlopen(url).read().decode('utf-8')

    # Extract the trail status message using regular expressions
    pattern = r'<h1 class="entry-title".*?><a.*?>(.*?)</a></h1>'
    match = re.search(pattern, html_content, re.DOTALL)

    if match:
        message = match.group(1).strip()
        save(message)
    else:
        print("Trail status not found in the HTML")
except Exception as err: # yes I know
    message = "SORBA status API error"
    save(message)
    raise


