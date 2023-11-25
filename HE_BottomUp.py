'''
Author: Mantha Sai Gopal
Reg.no: 23358
Program for building min-heap using bottom up approach
'''

import random

n = 1000000

arr = [random.randint(1,10000) for _ in range(n)]

file_name = "random_values.txt"

with open(file_name, 'w') as file:
    for value in arr:
        file.write(str(value) + '\n')

# print(f"Writing values to the file...'{file_name}'.")

# Bottom up approach
def heapify_bottom_up(arr):
    n = len(arr)
    counter = 0

    for i in range(n//2-1, -1, -1):
        minimum = i
        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] < arr[minimum]:
                minimum = left
            if right < n and arr[right] < arr[minimum]:
                minimum = right
            if i != minimum:
                arr[i], arr[minimum] = arr[minimum], arr[i]
                counter = counter + 1 
                i = minimum
            else:
                break
    return counter


print(heapify_bottom_up(arr))
