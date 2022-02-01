# Python program to check whether the given integer is a multiple of 5 and 7, and 10, 56.

num = int(input('Enter any number : '))

if((num%5) == 0 or (num % 7) == 0 or (num%10) == 0 or (num%56) == 0):
    print("Given numer is multiple of 5 or 7 or 10 or 56.")
else:
    print("Given numer is not multiple of 5 or 7 or 10 or 56.")