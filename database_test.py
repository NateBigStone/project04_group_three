import unittest
from unittest import TestCase
from database import db, logging
import sqlite3



# class for testing the database
class TestRecordsDB(TestCase):
    test_db_url = 'test_food.db'

    

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        database.db = self.test_db_url


        # drop everything from the DB to always start with an empty database
        with sqlite3.connect(self.test_db_url) as con:
            con.execute('DROP TABLE IF EXISTS records')
            
        con.close()

        with sqlite3.connect(self.test_db_url) as con:
            con.execute('CREATE TABLE IF NOT EXISTS records(restaurant TEXT, recipe TEXT, flickr TEXT, bookmarked INTEGER)')
            
        con.close()

        self.db = database.db
    #testing new added food
    def test_add_new_food(self):
        restaurant_Name = 'Tawakal'
        recipe_Name = 'Tacos'
        flickr_Name = 'Tacos Photo'
       
        database.add_data(restaurant_Name, recipe_Name, flickr_Name,)
        expected = {'Tawakal', 'Tacos', 'Tacos Photo', }
        self.compare_db_to_expected(expected)    
    
    # testing for food already in database
    def test_food_already_in_data(self):
        restaurant_Name = 'Tawakal'
        recipe_Name = 'Tacos'
        flickr_Name = 'Tacos Photo'
       
        database.add_data(restaurant_Name, recipe_Name, flickr_Name,)
        expected = {'Tawakal', 'Tacos', 'Tacos Photo', }
        with self.assertRaises(error):
            #database.add_data(restaurant_Name, recipe_Name, flickr_Name,)
            self.compare_db_to_expected(expected)    


    def compare_db_to_expected(self, expected):
        conn = sqlite3.connect(self.test_db_url)
        all_data = conn.execute('SELECT * FROM records').fetchall()

      
       

        for row in all_data:
            
            print(row)
           

        conn.close()


if __name__ == '__main__':
    unittest.main()