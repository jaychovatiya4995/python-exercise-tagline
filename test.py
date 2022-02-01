#  pattern 1
#  spec = 6
# for i in range(1,7):
#     for j in range(1,spec):
#         print(' ',end="")
#     spec -= 1    
#     for k in range(1,i+1):   
#         print('* ',end="")
#     print()  
# for i in range(5,0,-1): 
#     for j in range(0,6-i):    
#         print(' ',end="")  
#     for k in range(i+1,1,-1):   
#         print('* ',end="")
#     print()

#  pattern 2
# for i in range(1,6):   
#     for j in range(5,i-1,-1):   
#         print(j,end="")
#     for k in range(1,i): 
#         print(" ",end="") 
#     for m in range(1,i):   
#         print(" ",end="")
#     for n in range(i,6):   
#         print(n,end="")
#     print()

# pattern4
# spec=6
# for i in range(1,7):
#     for j in range(1,spec):    print(' ',end="")
#     spec -= 1    
#     for k in range(1,i+1):   print("  ",end="") if(k!=1 and k!=i)  else print('* ',end="")
#     print() 
     
# for i in range(5,0,-1): 
#     for j in range(0,6-i):    print(' ',end="")  
#     for k in range(i+1,1,-1):    print("  ",end="") if(k!=2 and k!=i+1) else print('* ',end="")     
#     print()

#  pattern 5
# spec = 4
# for i in range(1,5):
#     for j in range(1,spec):
#         print('  ',end="")
#     spec -= 1   
#     for k in range(1,i+1):   
#         print('*   ',end="")
#     print()  
# for i in range(4,0,-1): 
#     for j in range(0,5-i):    
#         print('  ',end="")  
#     for k in range(i    ,1,-1):   
#         print('*   ',end="")
#     print()

def addition(n):
    return chr(n)
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
# result = 
# print(" ".join(map(str, map(addition, range(1,8)))))
value = 63
print(" ".join(map(str, map(addition, range(65,93)))))
