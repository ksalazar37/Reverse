#  File: Reverse.py
#  Description: A short program that reverses the order of digits of a user-entered four-digit number.
#  Date Created: 09 / 14 / 2018
#  Date Last Modified: 01 / 06 / 2019

def main():
    number = int(input("Enter an integer: "))
    
    a = number % 10                # a: first digit of reversed number

    b = (number % 100) - a
    c = b // 10                    # c: second digit of reversed number

    d = (number % 1000) - a - c
    e = d // 100                   # e: third digit of reversed number

    f = number - (number % 1000)
    g = f // 1000                  # g: fourth digit of reversed number

    print("The reversed number is " + str(a) + str(c) + str(e) + str(g) + ".")

main()
