from validation import Divisible

class FizzBuzz():
    def isFizzBuzz(number):
        if Divisible.ByFive(number) and Divisible.ByThree(number):
            return "FizzBuzz"

        if Divisible.ByFive(number):
            return "Buzz"

        if Divisible.ByThree(number):
            return "Fizz"

        return number