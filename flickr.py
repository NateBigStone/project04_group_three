import requests
from logging import logging
import os

key = os.environ.get('flickr_key')

def getImage(yelp_dish):
    # Docs at https://www.flickr.com/services/api/explore/flickr.photos.search
# Search for pictures, modify to search for whatever tag you want
flickerSearchURL = 'https://api.flickr.com/services/rest/'
params = {
'method': 'flickr.photos.search',
'api_key': key,
'text': yelp_dish,
'format': 'json',
'nojsoncallback': '5',
'sort': 'relevance',
}
# Search flickr for pictures
flickrResponse = requests.get(flickerSearchURL, params=params)
# get json back
flickrResponseJson = flickrResponse.json()

# Get first json object ('photos') which contains another json object ('photo') which is an json array; each
# element represents one photo. Take element 1
firstResponsePhoto = flickrResponseJson['photos']['photo'][2]
#confirm to get the exact json
print(firstResponsePhoto)
# deal with this in the following way.
# Extract the secret, server, id and farm; which you need to construct another URL to request a specific photo
# https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
secret = firstResponsePhoto['secret']
photo_id = firstResponsePhoto['id']
server = firstResponsePhoto['server']
farm = firstResponsePhoto['farm']
try:
    fetchPhotoURL = f'https://farm{farm}.staticflickr.com/{server}/{photo_id}_{secret}_m.jpg'
    photoResponse = requests.get(fetchPhotoURL)
    return photoResponse
except Exception as e:
    logging.error(f'Something went wrong when calling the API: {e}')
    error = ('Error', data)
    return error 

with open(filename, 'wb') as f:
    for chunk in photo_Response.iter_content():
        f.write(chunk)

print('Photo saved to ' + filename)    

    

    


