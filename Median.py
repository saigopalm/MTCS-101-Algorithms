'''
Program to find median of a given list of integers.
Author: Mantha Sai Gopal
Reg.no: 23358
'''

import math
import random

# function to partition about the first element in the list and returns it's index after partition
def Partition(array):
    n = len(array)
    x = array[0]
    i,j = 1, n-1

    while i <= j:
        if array[i] <= x:
            i = i+1
        elif array[j] > x:
            j = j - 1
        else:
            array[i], array[j] = array[j], array[i]
            i = i+1
            j = j-1
    array[j], array[0] = array[0], array[j]
    return j

# function to partition the array about any given element in the array
def partition(array,x):
    index = array.index(x)
    array[0], array[index] = array[index], array[0]
    return Partition(array)

# function to find the ith smallest element in a list of integers
def select(arr, i):
    n = len(arr)

    # base case
    if n == 1:
        return arr[0]
    
    # creating sublists each of size atmost 5
    sublists = []
    for j in range(0,len(arr), 5):
        temp_list = arr[j:j+5]
        sublists.append(temp_list)

    # sorting the sublists
    sublists_sorted = [sorted(list) for list in sublists]

    # finding medians for each of the sublists
    medians = []
    for list in sublists_sorted:
        if len(list) == 5:
            medians.append(list[2])
        else:
            x = len(list)
            if x % 2 == 0:
                j = x // 2 - 1
            else:
                j = x // 2
            medians.append(list[j])
    
    # median of medians
    median_of_medians = select(medians, math.ceil(len(medians) / 2))

    # partitioning around median of medians
    k = partition(arr, median_of_medians) + 1

    if i == k:
        return median_of_medians
    elif i < k:
        return select(arr[:k], i)
    else:
        return select(arr[k:], i - k)

# function to find the median
def find_median(arr):
    if len(arr) <= 140:
        array_sorted = sorted(arr)
        middle_index = len(arr) // 2
        if len(arr) % 2  == 0:
            median = array_sorted[middle_index - 1]
            print(f"Actual Median: {median}")
        else:
            median = array_sorted[middle_index]
            print(f"Actual Median: {median}")
    
    else:
        n = math.ceil(len(arr)/2)
        print(f"Actual Median: {select(arr,n)}")

        
# test function
def main():
    # generating random integers between 1 and 100 
    arr = random.sample(range(1, 50000), 10000)
    # print(arr)
    
    array_sorted = sorted(arr)
    middle_index = len(arr) // 2
    if len(arr) % 2  == 0:
        median = array_sorted[middle_index - 1]
        print(f"Expected Medain: {median}")
    else:
        median = array_sorted[middle_index]
        print(f"Expected Median: {median}")
    
    find_median(arr)
    
# calling the main function
main()
