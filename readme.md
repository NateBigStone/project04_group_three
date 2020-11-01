## Group Three Foods

    pip install -r requirements.txt
    python app.py

App will be running on http://127.0.0.1:5000

This is a basic python app which requires Python 3.8 , SQLite3 and uses Flask as user 
interface. This application is developed to extract information from three API'S and store the output in a database.

Requirements: Flickr API and flickr key, Yelp API and  yelp key, and lastly Edamam API and recipe key.

The Edamam APi is a recipe API which will extract recipe information of the food entered. While the Flickr API will extract and display the photo of the recipe the user chooses to enter and lastly the Yelp API will display the restaurant of the recipe entered.

In order to run this app you need to have SQLITE3 installed since it is being used to store data in the database.