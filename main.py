import keys1


from mastodon import Mastodon

import requests
import json

def mes():

    #API_KEY 

    # Define the start and end points
    origin = 'Kasarani Stadium, Kenya'
    destination = 'GPO, Nairobi, Kenya'  # Adjust this as needed

    # Make a request to the Directions API without considering traffic
    directions_url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}'
    directions_response = requests.get(directions_url)

    # Get the JSON response
    directions_data = directions_response.json()

    # Check if any routes were returned
    if directions_data['routes']:
        # Get the duration of the route without considering traffic
        duration_without_traffic = directions_data['routes'][0]['legs'][0]['duration']['value']  # in seconds

        # Make a request to the Directions API considering traffic
        directions_url += '&departure_time=now'
        directions_response = requests.get(directions_url)

        # Get the JSON response
        directions_data = directions_response.json()

        # Get the duration of the route considering traffic
        duration_with_traffic = directions_data['routes'][0]['legs'][0]['duration_in_traffic']['value']  # in seconds

        # Calculate the difference in duration
        difference = duration_with_traffic - duration_without_traffic

        # Infer the traffic condition
        if difference < 300:  # less than 5 minutes difference
            traffic_condition = 'light'
        elif difference < 900:  # less than 15 minutes difference
            traffic_condition = 'moderate'
        else:  # 15 minutes or more difference
            traffic_condition = 'heavy'

        print(f'The traffic condition on Thika Road from {origin} to Nairobi\'s {destination} is approximately {traffic_condition}.')

        Message1 = (f'The traffic condition on Thika Road from {origin} to Nairobi\'s {destination} is approximately {traffic_condition}.')
    else:
        print('No routes found between the origin and destination.')

        Message2 = ('No routes found between the origin and destination.')

mes()

post_message = mes()



# Create an instance of the Mastodon API client
mastodon = Mastodon(
    from keys1 import access_token	  # Your access token
    api_base_url = "https://mastodon.social"
  # URL of your Mastodon instance
)


# Compose your post message
post_message = "Testing"

# Post your message
mastodon.status_post(post_message)

print("Post created successfully.")
