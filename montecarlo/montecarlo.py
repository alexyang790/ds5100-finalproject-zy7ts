import pandas as pd
import numpy as np
class Die():
    def __init__(self, faces: np.ndarray):
        """
        Initializes a Die object with the provided faces array. 

        Parameters:
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
        #checking if face is valid i.e. if it is in the die array
        if face not in self.__die['faces'].values:
            raise IndexError('provided face not in die')
        
        #checking if new_weight is valid
        if not isinstance(new_weight, (int, float)):
            raise TypeError('provided weight is not numeric or not castable as numeric')

        #changing the weight
        self.__die.loc[self.__die['faces'] == face, 'weight'] = new_weight

    def printdie(self):
        return self.__die


class Game():
    def __init__(self):
        pass   

class Analyzer():
    def __init__(self):
        pass