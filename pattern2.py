# write program to create blow pattern : 
# 5432112345
# 5432  2345
# 543    345
# 54      45
# 5        5
row = int(input("Enter value to draw pattern : "))

for i in range(1,row+1):   
    for j in range(row,i-1,-1):   
        print(j,end="")
    for k in range(1,i): 
        print("  ",end="") 
    for n in range(i,row+1):   
        print(n,end="")
    print()

