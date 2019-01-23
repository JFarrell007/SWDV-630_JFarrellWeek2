"""
Name: Jim Farrell
Class: SWDV-630
Description: Input class to prompt user for input and make sure data is a a non-negative real number.
"""
class Input:
        
    def getNumber(self,prompt):
        """get get input from the user"""
        while True:
            val = input(prompt)
            try:
                val = float(val)#convert to float.  It will raise ValueError if it cannot convert.
                if val < 0:#if less than 0 raise an error
                    raise ValueError()
                return val#otherwise return number
            except ValueError:#Handle the error
                print("Please enter a non-negative real number.")