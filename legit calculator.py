a = int(input("please enter first number :"))
b = input("please enter operator(ex- +,-,^,*,%,/ (here '%' means to show the remainder)  :")
c = int(input("please enter second number : "))

if b == '+' :   #for addition of the two numbers
    print(int(a+c))

elif b == '-':  #for subtraction of the two numbers
    print(int(a-c))

elif b == '*' : #for multiplication of two numbers
    print(int(a*c))

elif b == '^' : #for raising the first numbers to the power equivalent to the second digit
    print(int(a**c))

elif  b == '/' :#for division of two numbers
    print(int(a/c))

elif b == '%' : #for finding the remainder after didiving first number with second number
    print(int(a%c))

else:           #if anything other than a number is given as input
    print ("Invalid input!")