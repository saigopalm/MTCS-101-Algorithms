'''
Rabin Karp algorithm
Author: Mantha Sai Gopal
Reg.no: 23358
'''

def RabinKarp(text, pattern):
    n = len(text)
    m = len(pattern)

    i = 0 # iterator over the text
    count = 0

    for i in range(n - m + 1):
        if(hash(pattern) == hash(text[i:i+m])):
            if pattern == text[i:i+m]:
                print(f"Pattern occured at index:{i}")
                count = count + 1
    print(f"Total number of occurences of the pattern in text:{count}")

def main():
    file = open("/home/dmacs-9/Desktop/MTech/Semester_1/Algos/Assignment4/sample.txt","r")
    text = file.read()
    pattern = "Turing"
    RabinKarp(text,pattern)

main()