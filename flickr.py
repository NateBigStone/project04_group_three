import requests
import logging
import os
import re


def main():
    item = get_item()
    photo = get_image(item)
    print(photo)


def get_image(item):
    # Docs at https://www.flickr.com/services/api/explore/flickr.photos.search
    # Get flickr key
    key = os.environ.get('flickr_key')
    # Search for pictures, modify to search for whatever tag you want
    flicker_search_url = 'https://api.flickr.com/services/rest/'
    params = {
        'method': 'flickr.photos.search',
        'api_key': key,
        'text': item,
        'format': 'json',
        'nojsoncallback': '1',
        'sort': 'relevance',
    }
    # Search flickr for pictures
    try:
        flickr_response = requests.get(flicker_search_url, params=params)
        # get json back
        flickr_response_json = flickr_response.json()
    except Exception as e:
        logging.error(f'Something went wrong when calling the API: {e}')
        return None
    # Get first json object ('photos') which contains another json object ('photo') which is an json array; each
    # element represents one photo. Take element 1

    try:
        first_response_photo = flickr_response_json['photos']['photo'][0]
        # confirm to get the exact json
        logging.info( first_response_photo)
        # deal with this in the following way.
        # Extract the secret, server, id and farm; which you need to construct another URL to request a specific photo
        # https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
        secret = first_response_photo['secret']
        photo_id = first_response_photo['id']
        server = first_response_photo['server']
        farm = first_response_photo['farm']
    
        fetch_photo_url = f'https://farm{farm}.staticflickr.com/{server}/{photo_id}_{secret}_m.jpg'
        
        return fetch_photo_url
    except Exception as e:
        logging.error(f'Something went wrong when calling the API: {e}')

    return None

  
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


if __name__ == "__main__":
    main()
