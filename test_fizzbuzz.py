import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_IsFizzBuzz_GivenNumberNotDivisibleBy3Or5_ShouldReturnNumber(self):
        numbersNotDivisibleBy3or5 = [1,4,8,14,16,22]
        for eachNumber in numbersNotDivisibleBy3or5:
            # Arrange
            number = eachNumber
            # Act
            result = FizzBuzz.isFizzBuzz(number)
            # Assert
            expect = str(eachNumber)
            self.assertEqual(result, expect)

    def test_IsFizzBuzz_GivenNumbersDivisibleByThree_ShouldReturnFizz(self):
        numbersDivisibleBy3 = [6,9,12,18,21,24,27,33,36,39,42,48,51]
        for eachNumber in numbersDivisibleBy3:
            # Arrange
            number = eachNumber
            # Act
            result = FizzBuzz.isFizzBuzz(number)
            # Assert
            expect = "Fizz"
            self.assertEqual(result, expect)

    def test_IsFizzBuzz_GivenNumbersDivisibleByFive_ShouldReturnBuzz(self):
        numbersDivisibleBy5 = [10,20,25,35,40]
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

    def test_IsFizzBuzz_GivenPrimeNumberGreaterThanAHundred_ShouldReturnNumber(self):
        primeNumbersGreaterThanAHundred = [101, 121]
        for eachNumber in primeNumbersGreaterThanAHundred:
            # Arrange
            number = eachNumber
            # Act
            result = FizzBuzz.isFizzBuzz(number)            
            # Assert
            expect = str(eachNumber)
            self.assertEqual(result, expect)
        
    def test_IsFizzBuzz_GivenPrimeNumberOtherThan3or5_ShouldReturnWhiz(self):
        primeNumbersOtherThan3or5 = [2, 7, 11, 13, 17]
        for eachNumber in primeNumbersOtherThan3or5:
            # Arrange
            number = eachNumber
            # Act
            result = FizzBuzz.isFizzBuzz(number)            
            # Assert
            expect = "Whiz"
            self.assertEqual(result, expect)
        
    def test_IsFizzBuzz_Given3_ShouldReturnFizzWhiz(self):
        # Arrange
        number = 3
        # Act
        result = FizzBuzz.isFizzBuzz(number)            
        # Assert
        expect = "FizzWhiz"
        self.assertEqual(result, expect)
        
    def test_IsFizzBuzz_Given5_ShouldReturnBuzzWhiz(self):
        # Arrange
        number = 5
        # Act
        result = FizzBuzz.isFizzBuzz(number)            
        # Assert
        expect = "BuzzWhiz"
        self.assertEqual(result, expect)