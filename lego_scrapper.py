import os
import json
import requests as req
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

# get the brickset api key
BRICKSET_API_KEY = os.getenv("BRICKSET_API_KEY")

# brickset api endpoint
BRICKSET_API_ENDPOINT = os.getenv("BRICKET_API_ENDPOINT")

# brickset username
BRICKSET_USERNAME = os.getenv("BRICKSET_USERNAME")

# brickset password
BRICKSET_PASSWORD = os.getenv("BRICKSET_PASSWORD")

# brickset user Hash
BRICKSET_HASH = os.getenv("BRICKSET_HASH")

URLS_DF = pd.read_csv("lego_urls_setIDs.csv")
set_IDs = URLS_DF["set_id"]

print(set_IDs)
# build a POST request to confirm user hash
print("Verifying API and retrieve userHase")
print("\n==================================\n")

r = req.post(f"{BRICKSET_API_ENDPOINT}/login",
             headers={"Content-Type": "application/x-www-form-urlencoded"},
             data={"apiKey": BRICKSET_API_KEY,
                   "username": BRICKSET_USERNAME,
                   "password": BRICKSET_PASSWORD},
             )

print("Request Status Code: ", r.status_code)
print(f"User Hash: {r.json()['hash']}")
print("\n==================================\n")

# getSet get Request
print("Send POST request for data on setNumber")
print("\n==================================\n")
# set up payload
for set_ID in set_IDs:

    payload = {
        "apiKey": BRICKSET_API_KEY,
        "userHash": BRICKSET_HASH,
        "params": json.dumps({"setNumber": set_ID}),
    }
    response = req.post(f"{BRICKSET_API_ENDPOINT}/getSets",
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        data=payload,
                        timeout=30)
    # check if any are not getting a 200 status code
    if response.status_code != 200:
        print(f"Respose data for set: {set_ID}")
        print(f"Request Status Code: {response.status_code}")
        print(f"Request Status Body: {response.text}")

    print(f"Set ID {set_ID} status: {response.status_code} ")





print("\n==================================\n")


