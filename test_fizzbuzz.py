import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_IsFizzBuzz_GivenNumberNotDivisibleBy3Or5_ShouldReturnNumber(self):
        numbersNotDivisibleBy3or5 = [1,2,4,7,8,11,13,14,16,17,19,22]
        for eachNumber in numbersNotDivisibleBy3or5:
            # Arrange
            number = eachNumber
            # Act
            result = FizzBuzz.isFizzBuzz(number)
            # Assert
            expect = eachNumber
            self.assertEqual(result, expect)

    def test_IsFizzBuzz_GivenThree_ShouldReturnFizz(self):
        numbersDivisibleBy3 = [3,6,9,12,18,21,24,27,33,36,39,42,48,51]
        for eachNumber in numbersDivisibleBy3:
            # Arrange
            number = eachNumber
            # Act
            result = FizzBuzz.isFizzBuzz(number)
            # Assert
            expect = "Fizz"
            self.assertEqual(result, expect)

    def test_IsFizzBuzz_GivenFive_ShouldReturnBuzz(self):
        numbersDivisibleBy5 = [5,10,20,25,35,40]
        for eachNumber in numbersDivisibleBy5:
            # Arrange
            number = eachNumber
            # Act
            result = FizzBuzz.isFizzBuzz(number)
            # Assert
            expect = "Buzz"
            self.assertEqual(result, expect)
    
    def test_IsFizzBuzz_GivenNumbersDivisibleByBoth3And5_ShouldReturnFizzBuzz(self):
        numbersDivisibleBy3and5 = [15, 30, 45, 75]
        for eachNumber in numbersDivisibleBy3and5:
            # Arrange
            number = eachNumber
            # Act
            result = FizzBuzz.isFizzBuzz(number)            
            # Assert
            expect = "FizzBuzz"
            self.assertEqual(result, expect)