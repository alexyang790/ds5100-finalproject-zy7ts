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

    def test_die_rolldie(self):
        """
        A test function to test the roll of a Die object.
        """
        #initializing the die
        array = np.array([1,2,3,4,5,6])
        die = mt.Die(array)
        #rolling the die
        outcome = len(die.rolldie(3))
        #expecting
        expected = 3
        #testing
        self.assertTrue(np.array_equal(outcome, expected))

    def test_printdie(self):
        """
        A test function to test the return of die's data frame
        """
        #initializing the die
        array = np.array([1,2,3,4,5,6])
        die = mt.Die(array)
        #expecting
        expected_df = pd.DataFrame({
            'faces': [1, 2, 3, 4, 5, 6],
            'weight': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        })
        # Check if the returned DataFrame from printdie() matches the expected DataFrame
        self.assertTrue(die.printdie().equals(expected_df))

    def test_game_init(self):
        """
        A test function to test the initialization of a Game object
        """
        array = np.array([1,2,3,4,5,6])
        die = mt.Die(array)
        die_list = [die, die, die]
        game = mt.Game(die_list)
        self.assertTrue(game.die_list == die_list)
    
    def test_game_play(self):
        """
        A test function to test the play of a Game object
        """
        array = np.array([1,2,3,4,5,6])
        die = mt.Die(array)
        die_list = [die, die, die]
        game = mt.Game(die_list)
        game.play(4)
        self.assertTrue(game.show_results() is not None)

    def test_game_showresults(self):
        """
        A test function to test the show_results of a Game object
        """
        array = np.array([1,2,3,4,5,6])
        die = mt.Die(array)
        die_list = [die, die, die]
        game = mt.Game(die_list)
        game.play(4)
        self.assertTrue(game.show_results(method = 'narrow') is not None)

    

if __name__ == '__main__':
    unittest.main()