'''
Program to find the second largest element in a given array using divide and conquer approach.
Author: Mantha Sai Gopal
Reg.no: 23358
'''
import random

def find_second_largest(array):
    # Exception case
    if len(array) == 0:
        return float('-inf'), float('-inf')
    # Boundary case
    if len(array) == 1:
        return array[0], float('-inf')
    else:
        max_1, second_max_1 = find_second_largest(array[:len(array)//2])
        max_2, second_max_2 = find_second_largest(array[len(array)//2:])

        if max_1 > max_2:
            max_val = max_1
            if max_2 > second_max_1:
                second_max_val = max_2
            else:
                second_max_val = second_max_1
        else:
            max_val = max_2
            if max_1 > second_max_2:
                second_max_val = max_1
            else:
                second_max_val = second_max_2
                
        return max_val, second_max_val

def main():
    arr = [random.randint(1, 1000) for _ in range(0)]
    print("Generated array:", arr)
    max, min = find_second_largest(arr)
    print(f"The second largest element in the array is: {min}")

main()
