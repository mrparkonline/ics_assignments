# CCC '18 J1 - Telemarketer or not?
# Solution

# input
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# processing & output
if num1 == 9 or num1 == 8:
    if num2 == num3:
        if num4 == 9 or num4 == 8:
            print('Hang Up')
        else:
            print('Answer')
    else:
        print('Answer')
else:
    print('Answer')
