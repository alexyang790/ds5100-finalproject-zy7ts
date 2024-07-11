import unittest
import numpy as np
import pandas as pd
import montecarlo as mt

class MonteCarloTest(unittest.TestCase):
    def test_die_init(self):
        """
        A unit test function to test the initialization of a Die object
        """
        array = np.array([1,2,3,4,5,6])
        die = mt.Die(array)
        expected_die = pd.DataFrame({
            'faces': [1,2,3,4,5,6],
            'weight': [1.0,1.0,1.0,1.0,1.0,1.0]
        })
        self.assertTrue(die.printdie().equals(expected_die))

    def test_die_changeweight(self):
        """
        A test function to test the change in weight of a Die object.
        """
        #initializing the die
        array = np.array([1,2,3,4,5,6])
        die = mt.Die(array)
        #changing the weight
        die.changeweight(2,4)
        #expecting 
        expected_die = pd.DataFrame({
            'faces': [1,2,3,4,5,6],
            'weight': [1.0,4.0,1.0,1.0,1.0,1.0]
        })
        #testing
        self.assertTrue(die.printdie().equals(expected_die))


if __name__ == '__main__':
    unittest.main()