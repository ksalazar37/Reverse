#  File: Reverse.py
#  Description: A program that reverses the order of digits of a user-entered four-digit number.
#  Student's Name: Kristina Salazar
#  Course Name: CS 303E

#  Date Created: 09 / 14 / 2018
#  Date Last Modified: 09 / 15 / 2018


def main():

    # variables:
    # number: user-entered 4 digit number
    # a, b, c etc: alphabetical variables used during algorithmic calculations


    print()

    number = int(input("Enter an integer: "))


    a = number % 10                # a: first digit of reversed number

    b = (number % 100) - a
    c = b // 10                    # c: second digit of reversed number

    d = (number % 1000) - a - c
    e = d // 100                   # e: third digit of reversed number

    f = number - (number % 1000)
    g = f // 1000                  # g: fourth digit of reversed number


    # print numbers to test algorithm:

    #print(number)
    #print("1: " + str(a))
    #print("calc 2: " + str(b))
    #print("2: " + str(c))
    #print("calc 3: " + str(d))
    #print("3: " + str(e))
    #print("calc 4: " + str(f))
    #print("4: " + str(g))


    print("The reversed number is " + str(a) + str(c) + str(e) + str(g) + ".")




main()
