import pandas as pd
import numpy as np
class Die():
    """
    The Die() class represents a 'die' that can be rolled and may have different weights on each face

    Attributes:
        faces (np.array): A NumPy array representing the faces of the die.
        __weights (np.array): An array representing the weights assigned to each face.
        __die (pd.DataFrame): A private DataFrame storing faces and their corresponding weights.

    Methods:
        __init__(self, faces: np.ndarray): initilizes the die object with provided faces array  
        changeweight(self, face, new_weight): changes the weight of a specified single face of the die to a provided new weight
        rolldie(self, times=1): rolles the die with provided times (defaults to 1) and returns a list of outcomes (faces)
        printdie(self): returns the die dataframe
    """
    def __init__(self, faces: np.ndarray):
        """
        Initializes a new Die instance with the provided faces array. 

        Inputs:
            faces (np.array): A NumPy array representing the faces of the die.

        Raises:
            TypeError: If faces is not a NumPy array or if it contains data types other than integers or strings.
            ValueError: If the faces array contains non-distinct values.
        """
        self.faces = faces
        #checking if faces is a numpy array
        if not isinstance(faces, np.ndarray):
            raise TypeError("faces must be a numpy array")

        #checking array's data type
        if not (faces.dtype == np.int64) or (faces.dtype == np.str_):
            raise TypeError("faces must be a numpy array of integers or strings")
        
        #checking if array's values are distinct
        if len(np.unique(faces)) != len(faces):
            raise ValueError("faces must be distinct values")
        
        #internally initializes the weights (private) to 1.0 for each face
        self.__weights = np.ones(len(faces))

        #saving both faces and weights in a private data frame with faces in the index
        self.__die = pd.DataFrame(
            {'faces': self.faces,
            'weight': self.__weights}
        )

    def changeweight(self, face, new_weight):
        """
        Change the weight of a single side of the die.

        Attributes:
            face (int or str): The face value of the side to be changed.
            new_weight (int or float): The new weight for the side.

        Raises:
            IndexError: If the provided face is not in the die array.
            TypeError: If the provided weight is not numeric or not castable as numeric.

        Returns:
            None
        """
        #checking if face is valid i.e. if it is in the die array
        if face not in self.__die['faces'].values:
            raise IndexError('provided face not in die')
        
        #checking if new_weight is valid
        if not isinstance(new_weight, (int, float)):
            raise TypeError('provided weight is not numeric or not castable as numeric')

        #changing the weight
        self.__die.loc[self.__die['faces'] == face, 'weight'] = new_weight

    def rolldie(self, timesrolled = 1):
        """
        A function that simulates rolling a die multiple times and returns the outcomes.

        Attributes:
            self: the object instance
            timesrolled (int): the number of times to roll the die, defaults to 1

        Returns:
            outcomes: list of outcomes from rolling the die
        """
        #checking if timesrolled is an integer
        if type(timesrolled) != int:
            raise TypeError('timesrolled must be an integer')   
        
        #rolling the dice and returning outcome possibility is the weight divided by the sum of the weights
        outcomes = np.random.choice(
            self.__die['faces'], 
            timesrolled, 
            replace = False, 
            p = self.__die['weight'] /  self.__die['weight'].sum())
        return outcomes
    
    def printdie(self):
        """
        Returns a copy of the private die data frame
        """
        return self.__die


class Game():
    """
    Represents a game where a list of similar dice can be rolled a specified number of times. Their weight can be different
    
    Attributes:
        die_list (list): A list of Die objects representing the dice used in the game.
        __results (pd.DataFrame): A placeholder for the results of the game.

    Methods:
        __init__(self, die_list): Initializes a new instance of the Game class.
        
        play(self, rolled_times): Plays the die in the list a specified number of times and stores the results in a wide data frame.
        
        show_results(self, method="wide"): Displays the results of the most recent play in the specified format ('wide' or 'narrow').
    """
    def __init__(self, die_list):
        """
        Initializes a new instance of the Game class.

        Inputs:
            die_list (list): a list of already instantiated similar dice

        Attributes:
            die_list (list): The list of Die objects representing the dice used in the game.
            play_results (None): A placeholder for the results of the game.
        """
        self.die_list = die_list
        self.__results = None #placeholder for results of the game
        
    def play(self, rolled_times):
        """
        Play the die in the list a specified number of times and store the results in a wide data frame.

        Parameters:
            rolled_times (int): The number of times to roll each die in the list.
       
        Raises:
            TypeError: If the rolled_times parameter is not an integer.
        """
        #checking if rolled_times is an integer
        if not isinstance(rolled_times, int): raise TypeError('rolled_times must be an integer')
        
        #play the die in list and store the results in a data frame
        reults = {i: die.rolldie(rolled_times) for i, die in enumerate(self.die_list)}
        self.__results = pd.DataFrame(reults)

    def show_results(self, method = "wide"):
        """
        A function to display the results of the most recent play in the specified format (wide or narrow, defaults to wide).

        Parameters:
            method (str): The format to return the results in ('wide' or 'narrow'). Defaults to 'wide'.

        Returns:
            pd.DataFrame: The DataFrame containing the results of the most recent play.

        Raises:
            ValueError: If the provided method is not 'wide' or 'narrow'.
        """
        if method == "wide":
            return self.__results
        elif method == 'narrow':
                narrow_results = self.__results.reset_index().melt(id_vars=['index'], var_name='Die', value_name='Outcome')
                narrow_results.set_index(['index', 'Die'], inplace=True)
                narrow_results.index.names = ['Roll Number', 'Die Number']
                return narrow_results
        else:
            raise ValueError("Invalid method specified. Choose 'wide' or 'narrow'.")
    
class Analyzer():
    """
    Represents an analyzer that computes various descriptive statistical properties about the results of a single game.

    Attributes:
        game (Game): An instance of the Game class representing the game being analyzed.
        __results (pd.DataFrame): A DataFrame containing the results of the game.

    Methods:
        __init__(self, game): Initializes a new instance of the Analyzer class.
        
        jackpot(self): Calculates the number of jackpots in the game.
        
        face_counts(self): Calculates the count of each face rolled in each roll of the game.
        
        combo_counts(self): Calculates the distinct combinations of faces rolled in each roll of the game.
        
        permutation_counts(self): Calculates the distinct permutations of faces rolled in each roll of the game.
    """
    def __init__(self, game):
        """
        Initializes a new instance of the Analyzer class.

        Parameters:
            game (Game): An instance of the Game class.

        Raises:
            ValueError: If the game parameter is not an instance of the Game class.

        Returns:
            None
        """
        if not isinstance(game, Game):
            raise ValueError('game must be an instance of Game')
        self.game = game
        self.__results = self.game.show_results(method = 'wide')

    def jackpot(self):
        """
        Calculates the number of jackpots in the game.

        Returns:
            count (int): The number of jackpots.
        """
        count = (self.__results.nunique(axis=1) == 1).sum()
        return count
    
    def face_counts(self):
        """
        Calculates the count of each face rolled in each roll of the game.

        Returns:
            counts_df (pandas.DataFrame): A DataFrame where the index represents the roll number and the columns represent the face values. The values in the DataFrame are the count of each face rolled in each roll.
        """
        #save the result df to a wide table
        wide_format = self.__results.melt(var_name='Die', value_name='Face', ignore_index=False)
        #make a crosstab from the wide table
        counts_df = pd.crosstab(wide_format.index, wide_format['Face'])
        return counts_df

    def combo_counts(self):
        """
        Calculates the distinct combinations of faces rolled in each roll of the game.

        Returns:
            combos_counts (pandas.DataFrame): A DataFrame representing the distinct combinations of faces rolled along with their counts.
        """
        combos = self.__results.apply(lambda x: tuple(x.sort_values().values), axis=1)
        combos_counts = combos.value_counts().reset_index().rename(columns={0: 'count'})
        combos_counts = combos_counts.set_index(list(combos_counts.columns[:-1]))
        return combos_counts

    def permutation_counts(self):
        """
        Calculates the distinct permutations of faces rolled in each roll of the game.

        Returns:
            perm_counts (pandas.DataFrame): A DataFrame representing the distinct permutations of faces rolled along with their counts.
        """
        perms = self.results.apply(tuple, axis=1)
        perm_counts = perms.value_counts().reset_index().rename(columns={0: 'count'})
        perm_counts = perm_counts.set_index(list(perm_counts.columns[:-1]))
        return perm_counts