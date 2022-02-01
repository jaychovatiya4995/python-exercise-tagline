# Flatten a list using list comprehension and for loop.
# For example:
#    Input:
#    [[1,2,3], [4,5,6], [7,8,9]]

#    Output: 
#     [1, 2, 3, 4, 5, 6, 7, 8, 9] 

number_list = int(input("Enter value for how much list you can insert: "))
main_list = []

for i in range(1, number_list+1):    
    number_element = int(input(f"How much elements you can add for {i} list: "))
    inner_list = []
    inner_list[:] = []
    for j in range(1, number_element+1):
        element = int(input(f"Enter value for {j} element of list {i}: "))
        inner_list.append(element)
    main_list.append(inner_list)

print("Main list: ",main_list)
print("Flatten list: ",[j for i in main_list for j in i])

