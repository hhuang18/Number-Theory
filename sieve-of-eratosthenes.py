# The Sieve of Eratosthenes is a way to quickly find prime numbers up until a certain number.
# Invented by Greek mathematician Eratosthenes, you write numbers down and eliminate numbers and their multiples
# until you're left with the primes.
import math

def sieve(end_num):
    if end_num < 2:
        print("No prime numbers found")
        return []
    else:
        # Define a list of numbers from 2 to the end number.
        nums = list(range(2, end_num + 1))

        # If end_num = n, we can stop at multiples of sqrt(n) because of the following result:
        # If n is composite, then n has a prime divisor that is smaller than or equal to sqrt(n).
        # That is, once we have eliminated all the multiples of numbers smaller than or equal to sqrt(n),
        # we can stop.
        i = 0
        while nums[i] <= math.floor(math.sqrt(end_num)):
            # Find the next uneliminated number and list it as prime.
            print("Prime found: " + str(nums[i]))
            counter = 2
            # Remove all multiples of it.
            while counter * nums[i] <= end_num:
                to_find = counter * nums[i]
                index_of_num = nums.index(to_find) if to_find in nums else None
                if index_of_num != None:
                    print("Composite number removed: " + str(nums.pop(index_of_num)))
                counter = counter + 1
            # Repeat!
            i = i + 1
        return nums

def main():
    print(sieve(1000))

main()