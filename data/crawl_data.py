import googlemaps
import time
import json

# Set up the Google Maps API client with your API key
gmaps = googlemaps.Client(key='AIzaSyD33vGmY4G4vlB1m4HNCcWPQ1uMGSZd3QI')
# Replace 'YOUR_API_KEY' with your actual Google Maps API key

# Define the location and radius for the search
location = (21.0055108,105.8510694)
radius = 300 # Specify the radius in meters to include nearby locations

# Perform a Places API nearby search to retrieve the locations within the specified radius
places_result = gmaps.places_nearby(location=location, radius=radius)

# Extract the relevant information from the API response
locations = []
for place in places_result['results']:
    name = place['name']
    latitude = place['geometry']['location']['lat']
    longitude = place['geometry']['location']['lng']
    locations.append({
        'name': name,
        'latitude': latitude,
        'longitude': longitude
    })
    time.sleep(1)  # Pause to avoid hitting API rate limits

# Save the locations to a JSON file
with open('locations.json', 'a+', encoding='utf-8') as outfile:
    json.dump(locations, outfile, ensure_ascii=False, indent=4)

print("Locations have been saved to 'locations.json'.")
