# To read the last element from each row and sum of the all last elements.
# For example:
# 	Input
# [[8, 14, -6], [12,7,4], [-11,3,21]]

# Output 
# 19

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

last_element = []
for i in main_list:    
    last_element.append(i[-1])
    
print(sum(last_element))
