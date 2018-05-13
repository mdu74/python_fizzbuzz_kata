from validation import Divisible
from get_whiz import Whiz
from is_prime_number import UserInput

class FizzBuzz():
    def isFizzBuzz(number):               
        if Divisible.ByFive(number) and Divisible.ByThree(number):
            return "FizzBuzz"

        if Divisible.ByFive(number):
            return "Buzz" + Whiz.GetWhiz(number)

        if Divisible.ByThree(number):
            return "Fizz" + Whiz.GetWhiz(number)

        return Whiz.GetWhiz(number) if UserInput.IsPrime(number) else str(number)