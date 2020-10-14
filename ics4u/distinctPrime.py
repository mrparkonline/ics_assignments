# Solution File for Distinct Primes
''' Assignment Goal.

We are to determine which number from 2 to N (Natural Number greater than 2) has
the most distinct prime factors.

Prime Factors : The set of prime numbers that multiply to a number.
- All Integers can be expressed as prime factorization

Repetition of prime factors do not count as unique/distinct prime factor.
- 4 vs 8
    4 has 1 prime factor of 2
    8 has 1 prime factor of 2
'''

# functions
def primeFactorizer(num):
    ''' primeFactorizer() returns a list of num's prime factorization w/
    duplicate prime factors if needed

    argument
    -- num : integer

    return
    -- list
    '''

    if num < 2:
        return []
    else:
        factors = []
        while num % 2 == 0:
            factors.append(2)
            num //= 2

        if num == 1:
            return factors
        else:
            divisor = 3
            while num != 1:
                if num % divisor == 0:
                    num //= divisor
                    factors.append(divisor)
                else:
                    divisor += 2

            return factors
# end of primeFactorizer()

def removeDuplicates(array):
    ''' removeDuplicates() saves only single instance of each item '''
    # Easiest way: list(set(array))
    result = []

    for item in array:
        if item not in result:
            result.append(item)

    return result
# end of removeDuplicates

# input
upper_limit = int(input('Enter your N value: ')) # let upper_limit represent N

# processing
answer = [] # This variable hold number with most unique factors
largest_count = 0 # This variable tracks answer's number of unique factors

for num in range(2, upper_limit):
    num_prime_factors = primeFactorizer(num)
    distinct_primes = removeDuplicates(num_prime_factors)
    current_count = len(distinct_primes)

    if current_count > largest_count:
        answer = [num]
        largest_count = current_count
    elif current_count == largest_count:
        answer += [num]
# end of for loop

if len(answer) == 1:
    print(answer[0], 'has the most unique prime factors.')
else:
    print('These numbers:', answer, 'have the most unique prime factors.')
