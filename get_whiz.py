from is_prime_number import UserInput

class Whiz:
    def GetWhiz(number):
        if  UserInput.IsPrime(number):
            return "Whiz"
        else:
            return ""