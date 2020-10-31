import sqlite3
import logging

db = 'food_db.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records(restaurant TEXT, recipe TEXT, flickr TEXT, bookmarked INTEGER)')
    conn.close()

def add_data(yelp_response, edamam_response, flickr_response):
    bookmarked = 0
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO records (restaurant, recipe, flickr, bookmarked) VALUES (?, ?, ?, ?)', (yelp_response, edamam_response, flickr_response, bookmarked))
    except Exception as e:
        logging.error('Error ' + e + ' insrting ' + yelp_response)
    conn.close()


def toggle_bookmark(restaurant, recipe, flickr, bookmarked):
    with sqlite3.connect(db) as conn:
        if bookmarked == 0:
            new_boomark = 1
            conn.execute('UPDATE records SET bookmarked = ? WHERE (restaurant = ? AND recipe = ?)', (new_boomark, restaurant, recipe))
        elif bookmarked == 1:
            new_boomark = 0
            conn.execute('UPDATE records SET bookmarked = ? WHERE (restaurant = ? AND recipe = ?)', (new_boomark, restaurant, recipe))
    conn.close()


def delete_record(restaurant, recipe, flickr):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('DELETE from records WHERE name = ? AND recipe = ? AND flickr = ?', (restaurant, recipe, flickr))
    except Exception as e:
        logging.error('Error ' + e + ' deleting ' + restaurant)
    conn.close()

def return_all():
    with sqlite3.connect(db) as conn:
        results = conn.execute('SELECT * FROM records')
    conn.close()
    return results

def clear_unbookmarked():
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE * FROM records WHERE bookmarked = ?', (0, ))
    conn.close()




