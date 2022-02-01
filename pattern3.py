# pattern using asccii 
#  65 - 94

spec=7
value = 65 
for i in range(1,8):
    for j in range(1,spec):
        print(' ',end="")
    spec -= 1 
      
    for k in range(1,i+1):   
        print(chr(value),end=" ")
        value += 1
    print()  
    
# def spec
    