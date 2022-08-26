a = int(input("please enter a number:"))     # input taken from user. 

if a > 15:
    print("Given number is greater than 15") # to compare the number to 15.

elif a < 15:
    print("Given number is smaller than 15")
    
else:
    print("Given number is equal to 15.")

if a%2 == 0:                                  # to find wether the number is even or odd.
    print("and is even")

elif a%2==1:
    print("and is odd") 
    
else:
    print("Invalid Input!")