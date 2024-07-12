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

    def test_analyzer_init(self):
        """
        A test function to test the initialization of an Analyzer object
        """
        array = np.array([1,2,3,4,5,6])
        die = mt.Die(array)
        die_list = [die, die, die]
        game = mt.Game(die_list)
        game.play(4)
        analyzer = mt.Analyzer(game)
        self.assertIsInstance(analyzer.game, mt.Game)

    def test_analyzer_jackpot(self):
        """
        A test function to test the jackpot of an Analyzer object
        """
        #setting up the analyzer instance
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = mt.Die(faces)
        die2 = mt.Die(faces)
        game = mt.Game([die1, die2])
        game.play(rolled_times=10)
        analyzer = mt.Analyzer(game)

        #testing jackpot
        result = analyzer.jackpot()
        self.assertTrue(result >= 0)
       
    def test_analyzer_face_counts(self):
        """
        A test function to test the face_counts of an Analyzer object
        """
        #setting up the analyzer instance
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = mt.Die(faces)
        die2 = mt.Die(faces)
        game = mt.Game([die1, die2])
        game.play(rolled_times=10)
        analyzer = mt.Analyzer(game)

        #testing face_counts
        result = analyzer.face_counts()
        self.assertIsInstance(result, pd.DataFrame, "Face counts should return a DataFrame.")

    def test_analyzer_combo_counts(self):
        """
        A test function to test the combo_counts of an Analyzer object
        """
        #setting up the analyzer instance
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = mt.Die(faces)
        die2 = mt.Die(faces)
        game = mt.Game([die1, die2])
        game.play(rolled_times=10)
        analyzer = mt.Analyzer(game)

        #testing combo_counts
        result = analyzer.combo_counts()
        self.assertIsInstance(result, pd.DataFrame, "Combo counts should return a DataFrame.")
        self.assertIn('count', result.columns, "Combo counts DataFrame should have a 'count' column.")

    def test_analyzer_permutation_counts(self):
        """
        A test function to test the permutation_counts of an Analyzer object
        """
        #setting up the analyzer instance
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = mt.Die(faces)
        die2 = mt.Die(faces)
        game = mt.Game([die1, die2])
        game.play(rolled_times=10)
        analyzer = mt.Analyzer(game)

        #testing permutation_counts
        result = analyzer.permutation_counts()
        self.assertIsInstance(result, pd.DataFrame, "Permutation counts should return a DataFrame.")

if __name__ == '__main__':
    unittest.main()