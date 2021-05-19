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
        
if __name__ == '__main__':
    # os.system('cls')
    unittest.main()