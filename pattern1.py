row = int(input("Enter value (minimum 3): "))
spec = row-1 

for i in range(1,row):
    for j in range(1,spec):
        print(' ',end="")
    spec -= 1    
    for k in range(1,i+1):   
        print('* ',end="")
    print()  
for i in range(row-2,0,-1): 
    for j in range(0,row-1-i):    
        print(' ',end="")  
    for k in range(i+1,1,-1):   
        print('* ',end="")
    print()