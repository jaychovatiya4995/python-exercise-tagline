# Find the even elements from an array. Respectively multiply this element in the array.
#             For example:
# Input:
#  [1, 2, 3, 4, 5]

# Output 
#  [4,8]

# 	(Note: Need one line code, don't use for loop and if statement).

value = input("Enter value for list using comma(,) separate : ").split(",")
list1 = list(map(int, value))

print("Input list: ", list1)
print("Output list: ",list(map(lambda n : n*2, (list1[1::2]))))
