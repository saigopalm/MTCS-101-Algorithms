'''
KMP Algorithm 
Author: Mantha Sai Gopal
Reg.no: 23358
'''

# function that builds the prefix table given a pattern as input
def PrefixFunction(pattern):
    m = len(pattern)
    prefix_table = [0] * m

    # variable to hold the length of largest prefix that is also a suffix
    length = 0
    i = 1

    while i < m:
        if pattern[length] == pattern[i]:
            prefix_table[i] = length + 1
            length = length + 1
            i = i + 1
        else:
            if length != 0:
                length = prefix_table[length - 1]
            else:
                prefix_table[i] = 0
                i = i + 1
    return prefix_table

def KmpMatcher(text, pattern):
    n = len(text)
    m = len(pattern)

    # 'i' iterates over the text and 'j' iterates over the pattern
    i = 0
    j = 0
    count = 0

    prefix_table = PrefixFunction(pattern)

    while i < (n - m + 1):
        if text[i] == pattern[j]:
            i = i + 1 
            j = j + 1
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i = i + 1
        if j == m: # pattern matches
            count = count + 1
            print(f"Pattern occured at index:{i - j}") # index from which the pattern starts
            j = prefix_table[j - 1] # in order to find all the occurences of the pattern in the text
    print(f"Total occurences of the pattern in text:{count}")


def main():
    file = open("/home/dmacs-9/Desktop/MTech/Semester_1/Algos/Assignment4/sample.txt","r")
    text = file.read()
    pattern = "Hilbert"
    KmpMatcher(text,pattern)

main()