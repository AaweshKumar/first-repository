import math
try:
    a = int(input("please enter first number :"))
    A =a
    b = input("please enter operator(ex- +,-,^,*,%,/,!,sqrt):")

    if b != ('!' and 'sqrt'):
        c = int(input("please enter second number : "))
        

    if b == '+' :   #for addition of the two numbers
        print(int(a+(c)))

    elif b == '-':  #for subtraction of the two numbers
        print(int(a-(c)))

    elif b == '*' : #for multiplication of two numbers
        print(int(a*(c)))

    elif b == '^' : #for raising the first numbers to the power equivalent to the second digit
        print(int(a**(c)))

    elif  b == '/' :#for division of two numbers
         print(int(a/(c)))
              
    elif b == '%' : #for finding the remainder after didiving first number with second number
        print(int(a%(c)))

    elif b =='!':   #for finding the factorial
        for i in range(a,1,-1):
            f = (A*(i-1))
            A=f
        print(A)

    elif b== 'sqrt':#for findind the squareroot
        print(math.sqrt(a))

    else :          #if anything other than a number is given as input
       print ("Invalid operator!")

except ZeroDivisionError:
    print("can't divide by zero!")
except ValueError:
    print("invalid input!")
