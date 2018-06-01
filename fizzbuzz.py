from validation import Divisible
from get_whiz import Whiz
from is_prime_number import UserInput
from fizz_buzz_whiz import FizzBuzzWhiz

class FizzBuzz:
    def isFizzBuzz(number):               
        if Divisible.ByFive(number) and Divisible.ByThree(number):
            return "FizzBuzz"

        if Divisible.ByFive(number):
            return FizzBuzzWhiz.GetFizzBuzzWhiz("Buzz", number)

        if Divisible.ByThree(number):
            return FizzBuzzWhiz.GetFizzBuzzWhiz("Fizz", number)

        return Whiz.GetWhiz(number) if UserInput.IsPrime(number) else str(number)