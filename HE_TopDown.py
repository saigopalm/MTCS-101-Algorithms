'''
Author: Mantha Sai Gopal
Reg.no: 23358
Program for building min-heap using top down approach
'''

import random
from numpy import loadtxt

# Top down approach
def heapify_top_down(arr):
    n = len(arr)
    counter = 0
    
    i = 1
    while i < n:
        child = i
        parent = (i - 1) // 2

        # verifying if heap property is maintained up to the index i
        while child > 0 and arr[child] < arr[parent]:
            arr[child], arr[parent] = arr[parent], arr[child]
            counter = counter + 1
            child = parent
            parent = (child - 1) // 2
        i = i + 1

    return counter

# Create a list of 'n' elements 
arr = loadtxt('random_values.txt', dtype='int')
print(heapify_top_down(arr))
