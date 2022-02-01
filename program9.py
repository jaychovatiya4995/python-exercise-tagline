#  The program must take the directory name then walk into the full 
#  path and find all directories and all files without using an inbuilt python module(glob).+
import os     

path = input("Enter a directory path for find them full details: ")

list_of_subdirectory = [x[0] for x in os.walk(path)]

print("********** :Subdirectory: ************")
for i in list_of_subdirectory:
    print(i)  
print("********** :End of Subdirectory: ************")

list_of_file = []
for (dirpath, dirnames, filenames) in os.walk(path):   
    list_of_file.append([os.path.join(dirpath,file) for file in filenames])
print("********** :Subfiles: ************")
for j in list_of_file:   
    for k in range(len(j)): 
        print(j[k])
print("********** :End of Subfiles: ************")