import unittest
from unittest import TestCase
from database import db, logging









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

    def test_add_new_food(self):
        restaurant_Name = 'Tawakal'
        recipe_Name = 'Tacos'
        flickr_Name = 'Tacos'
       
        database.add_data(restaurant_Name, recipe_Name, flickr_Name,)
        expected = {'Tawakal', 'Tacos', 'Tacos', }
        self.compare_db_to_expected(expected)    
    

    def test_food_already_in_data(self):
        restaurant_Name = 'Tawakal'
        recipe_Name = 'Tacos'
        flickr_Name = 'Tacos'
       
        database.add_data(restaurant_Name, recipe_Name, flickr_Name,)
        expected = {'Tawakal', 'Tacos', 'Tacos', }
        with self.assertRaises(er):
            #database.add_data(restaurant_Name, recipe_Name, flickr_Name,)
            self.compare_db_to_expected(expected)    


    def compare_db_to_expected(self, expected):
        conn = sqlite3.connect(self.test_db_url)
        all_data = conn.execute('SELECT * FROM records').fetchall()

      
        #self.assertEqual(len(expected.update()), len(all_data))

        for row in all_data:
            
            print(row)
            #self.assertIn(row[0], expected.update())
            #self.assertEqual(expected[row[0]], row[1])

        conn.close()


if __name__ == '__main__':
    unittest.main()