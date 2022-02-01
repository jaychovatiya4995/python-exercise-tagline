# Write a program.
# For example:
#     Input
#     [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

#     Output 
#     [56.2, 51.7, 55.3, 52.5, 47.8]
import math, itertools
list1 = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

print(list(itertools.filterfalse(math.isnan, list1)))