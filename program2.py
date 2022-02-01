# Python program to find the factorial of a number using recursion.

num = int(input("Enter number to find factorial : "))

def find_factorial(n):
    if n == 1 or n == 0:   
        return 1
    else:    
        return n*(find_factorial(n-1))

if num < 0:   
    print("Negative value has no factorial")
else:
    print(find_factorial(num))