from math import sqrt 
from itertools import count, islice

class UserInput():
    def IsPrime(number):
        if number > 97:
            return False
        else:
            return number > 1 and all(number % i for i in islice(count(2), int(sqrt(number)-1)))