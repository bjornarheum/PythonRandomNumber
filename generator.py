import random

# Parent class
class Randomnumbers():

    # Method
    def generate(self, amount, minRange, maxRange):

        # Pre-conditions

        # Check that all variables provided are integers
        if type(amount) != int or type(minRange) != int or type(maxRange) != int:
            raise Exception('Only integers are accepted')

        # Check that the amount of numbers requested are one or more
        if amount < 1:
            raise Exception('Amount must be higher than 0 to generate numbers')

        # Check that the lowest range is smaller than the largest
        if minRange >= maxRange:
            raise Exception('Minimum range must be lower than maximum range')


        numbers = []

        for i in range(amount):
            n = random.randint(minRange, maxRange)
            numbers.append(n)


        # Post-conditions

        # Check that there are numbers generated
        if len(numbers) == 0:
            raise Exception('No numbers were generated')

        # Return the numbers if the result is the same as requested amount
        if len(numbers) == amount:
            return numbers
        else:
            # Return empty array if amount is not the same as result
            return []


# Instatiate
test = Randomnumbers()
# Use method to generate numbers
test.generate(3, 5, 10)