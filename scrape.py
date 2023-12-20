import requests
import json

# API endpoint
url = "https://content-partners-pa.googleapis.com/v2/directory/profiles:search?key=AIzaSyBTRqr23b8ntVmGIDoing11fmn4falv-NE&alt=json"

# Iterate through all the options

flag = True


page_token = ""


def create_body(page_token: str):
    # Initialize request body
    return {
        "pageToken": page_token,
        "query": "",
        "sortOptions": {
            "sortDimension": "RELEVANCE",
            "sortOrder": "SORT_ORDER_UNSPECIFIED",
        },
    }


partners = []

while True:
    # Set page token
    body = create_body(page_token)
    # Making the POST request
    print(page_token)
    response = requests.post(url, json=body)

    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")
        print("Response:")
        print(response.text)
        break

    batch_response = response.json()

    if "nextPageToken" not in batch_response.keys():
        print("Reached the end")
        break

    partners.extend(batch_response["matchingProfiles"])

    page_token = batch_response["nextPageToken"]  # Trust


# Write to csv

# The file where you want to store the data
file_name = "partners.json"

# Writing the list to a JSON file
with open(file_name, "w") as file:
    json.dump(partners, file)

print(f"List has been written to {file_name}")
