'''
Run tests with: python -m unittest flights_tests
Run 2nd class: python -m unittest flights_tests.FlightsTestCase2
https://docs.python.org/3/library/unittest.html 
'''

import unittest
import flights
# import os

class FlightsTestCase(unittest.TestCase):

    def setUp(self):
        print('executing setUp')
        self.itemUnderTest = flights.FlightTable(flights.available_flights)

    def tearDown(self):
        print('executing tearDown')
        del self.itemUnderTest 
        self.itemUnderTest = None

    def test_init(self):
        print('executing test_init')
        self.assertEqual(len(self.itemUnderTest._flights), 11)
   

    def test_get_ids_to_city(self):
        print('executing test_p')
        expected_result = ['000', '004']
        results = self.itemUnderTest.get_ids_to_city('City X')
        # print('debug:', results)
        self.assertEqual(results, expected_result)


    def test_get_availables_to_cities(self):
        expected_result = ['City Y', 'City E']

        results = self.itemUnderTest.get_availables_to_cities('City X')
        self.assertEqual(results, expected_result)
        

class FlightsTestCase2(unittest.TestCase):

    def setUp(self):
        print('executing setUp')
        self.itemUnderTest = flights.FlightTable(flights.available_flights)

    def tearDown(self):
        print('executing tearDown')
        del self.itemUnderTest 
        self.itemUnderTest = None

    def test_init(self):
        print('executing test_init')
        self.assertEqual(len(self.itemUnderTest._flights), 11)
   

if __name__ == '__main__':
    # os.system('cls')
    unittest.main()