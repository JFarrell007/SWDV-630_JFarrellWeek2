"""
Name: Jim Farrell
Class: SWDV-630
Description: For this assignment write a Python class named Rectangle constructed by a length
and width and apply a method which will compute the area of a rectangle.
"""
from Input import Input #Input class to get input from user

class Retangle:

    def __init__(self, length, width):
        """Create Rectangle with length and width"""
        self.length = length
        self.width = width
        
    def computeArea(self):
        """Calculate the area of the rectangle"""
        area = self.length * self.width
        return area
    
def runTest():
    """runTest creates an Input object and Retangle object and runs the test"""
    data = Input()#create Input obj
    length = data.getNumber('Enter length of rectangle: ')#Use Input obj to get data with prompt
    width = data.getNumber('Enter width of rectangle: ')#Use Input obj to get data with prompt
    rec = Retangle(length,width) #Create a Rectangle obj with length and width
    print('The area of the retangle is {}'.format(rec.computeArea()))
    
runTest()
