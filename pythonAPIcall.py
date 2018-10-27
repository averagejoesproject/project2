import requests
import pandas as pd
import csv
import json
from pprint import pprint


city_ids = [362, 385, 382, 324, 381]


response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&dmaId=382&apikey=z3MYY7aQJFKC0wRH60emlfCUBUCjfeUF").json()


event_name = []
event_id = []
event_url = []
event_genre = []
event_genreID = []
event_subGenre = []
event_img = []
event_venue = []
event_id = []
event_venueURL = []
event_postCode = []
event_state = []
event_city = []
event_lat = []
event_lng = []
min_price = []
max_price = []
event_date = []
event_time = []

# All Events URL
for item in response["_embedded"]["events"]:
    event_name.append(item.get("name", "No Name"))
    event_id.append(item["id"])
    event_url.append(item["url"])
    event_date.append(item["dates"]["start"]["localDate"])
    event_time.append(item["dates"]["start"]["localTime"])
    for genre in item["classifications"]:
        event_genre.append(genre["genre"]["name"])
        event_genreID.append(genre["genre"]["id"])
        # event_subGenre.append(genre["subGenre"]["name"])
    for stoof in item["images"]:
        event_img.append(stoof.get("url", "NULL"))
    if "priceRanges" in item:
        for prices in item["priceRanges"]:
            min_price.append(prices["min"])
            max_price.append(prices["max"])


for venue in response["_embedded"]["events"]:
    for moreV in venue["_embedded"]["venues"]:
        event_venue.append(venue["name"])
        event_id.append(venue["id"])
        event_venueURL.append(venue.get("url", "NULL"))
        event_lat.append(moreV["location"]["latitude"])
        event_lng.append(moreV["location"]["longitude"])
        for blob in venue["_embedded"]["venues"]:
            for crap in blob:
                event_state.append(blob["state"])
                event_city.append(blob["city"])
                event_postCode.append(blob["postalCode"])


response_dictionary = {"Name": event_name, "Event ID": event_id, "Event URL": event_url,
                        "Genre": event_genre,"Genre ID": event_genreID, "Sub Genre": event_subGenre,
                        "Image": event_img,"Venue": event_venue,"Venue URL": event_venueURL,
                        "Zip Code": event_postCode, "State": event_state,"City": event_city,
                        "Latitude": event_lat,"Longitude": event_lng,"Max Price":max_price,"Min Price": min_price,
                        "Event Date": event_date, "Event Time": event_time}

response_df = pd.DataFrame({ key:pd.Series(value) for key, value in response_dictionary.items() })
response_df = response_df.dropna(axis=0, how='all', subset=["Name"])

response_df.to_csv('382.csv')