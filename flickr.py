import requests
import logging
import os
import re


key = os.environ.get('flickr_key')

item = ""

def main():
    item = get_item()
    photo = getImage(item)
    
def getImage(item):
# Docs at https://www.flickr.com/services/api/explore/flickr.photos.search
# Search for pictures, modify to search for whatever tag you want
    flickerSearchURL = 'https://api.flickr.com/services/rest/'
    params = {
    'method': 'flickr.photos.search',
    'api_key': key,
    'text': item,
    'format': 'json',
    'nojsoncallback': '1',
    'sort': 'relevance',
    }
# Search flickr for pictures
    flickrResponse = requests.get(flickerSearchURL, params=params)
# get json back
    flickrResponseJson = flickrResponse.json()

# Get first json object ('photos') which contains another json object ('photo') which is an json array; each
# element represents one photo. Take element 1

    try:
        firstResponsePhoto = flickrResponseJson['photos']['photo'][0]
#confirm to get the exact json
        logging.info(firstResponsePhoto)
# deal with this in the following way.
# Extract the secret, server, id and farm; which you need to construct another URL to request a specific photo
# https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
        secret = firstResponsePhoto['secret']
        photo_id = firstResponsePhoto['id']
        server = firstResponsePhoto['server']
        farm = firstResponsePhoto['farm']
    
        fetchPhotoURL = f'https://farm{farm}.staticflickr.com/{server}/{photo_id}_{secret}_m.jpg'
        photoResponse = requests.get(fetchPhotoURL)
        return photoResponse
    except Exception as e:
        logging.error(f'Something went wrong when calling the API: {e}')

  
def get_item():
    while True:
        item = input('Enter item name: ').strip().lower()

        if not item.replace(' ', '').isalpha():
            print("No empty string and character allowed, please try again.")
            continue
        else:
            item = re.sub(' +', ' ', item)
            break
    return item
