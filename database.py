import sqlite3
import logging

db = 'food_db.sqlite'


def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records(restaurant TEXT, recipe TEXT, flickr TEXT)')
    conn.close()


def add_data(yelp_response, edamam_response, flickr_response):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO records (restaurant, recipe, flickr) VALUES (?, ?, ?)', (yelp_response,
                                                                                               edamam_response,
                                                                                               flickr_response))
    except Exception as e:
        logging.error(f'Error {str(e)} inserting {yelp_response}')
    conn.close()


def delete_record(restaurant, recipe, flickr):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('DELETE from records WHERE name = ? AND recipe = ? AND flickr = ?', (restaurant, recipe, flickr))
    except Exception as e:
        logging.error('Error ' + e + ' deleting ' + restaurant)
    conn.close()


def return_all():
    results_list = []
    with sqlite3.connect(db) as conn:
        results = conn.execute('SELECT * FROM records')
        for row in results:
            results_list.append(row)
    conn.close()
    return results_list
