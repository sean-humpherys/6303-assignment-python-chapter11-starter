import requests
import config
# Get data from Yelp using API calls
# Need to watch Mosh' video 10.4 AND 10.5 to understand this code.
# Dr. Humpherys added different ways to filter and loop through the data

url = "https://api.yelp.com/v3/businesses/search"


"""
Try changing the API call to search for businesses in Canyon, TX or Amarillo TX
change the value of "location": "nyc" to 
    "location": "canyon, tx" 
or 
    "location": "amarillo, tx"

Try changing the API call to search for different types of businesses
change the "term": "barber" to 
    "term": "sushi" 
or 
    "term": "pizza"
or
    "term": "plumbing"

Try changing the data printed. View a list of all the possible variables at 
https://www.yelp.com/developers/documentation/v3/business_search
Look in the table under the section called "Response Body"
That table lists all the possible data about a business returned by Yelp
For example "businesses[x].display_phone" is the phone number 
formated nicely for display to users. 'display_phone' is the variable/property name. 
Access this variable/property in your code with 
    print(business['display_phone'])

"""
