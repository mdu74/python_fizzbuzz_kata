class FizzBuzz(object):
    def isFizzBuzz(number):
        if number % 5 == 0 and number % 3 == 0:
            return "FizzBuzz"

        if number % 5 == 0:
            return "Buzz"

        if number % 3 == 0:
            return "Fizz"

        return number
    