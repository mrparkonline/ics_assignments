import math
numbers_factors = []
#function to calculate all the prime factors of all the numbers in a sequence
def primeFactors(n):

    #number must be greater than 2
    if n < 2:
        print("no")
        return None

    #counter variable to track the number of distinct factors of a number
    distinct_factors = 0

    #iterate over all integers from 2 to n
    for number in range(2, n + 1):
#        print("number: " + str(number) + "--", end = '') #FOR TESTING
        #only count once even if the number can be divided by 2 more than once
        if number % 2 == 0:
#            print("2" + " ", end = '') #FOR TESTING
            distinct_factors += 1

        #divide the number by 2 until it cannot be divided further
        while (number % 2 == 0):
            number = int(number / 2)

        #the number must be odd now --> all 2s have been divided out
        #start testing all odd factors starting at 3 until n
        for factor in range(3, n + 1, 2):

            #only count the factor once
            if number % factor == 0:
#                print(str(factor) + " ", end = '') #FOR TESTING
                distinct_factors += 1

            #keep dividing the number by that factor until it cannot be further divided
            while number % factor == 0:
                number = int(number / factor)

        #add the number of distinct factors to list
        numbers_factors.append(distinct_factors)

        #reset the number of distinct factors for the next number
        distinct_factors = 0

#    print(numbers_factors) #FOR TESTING
    #print the first occuring number with the largest amount of distinct prime factors
    print(str(((numbers_factors.index(max(numbers_factors)) + 2))) + ": " + str(max(numbers_factors)) + " distinct prime factors")


primeFactors(1000)
