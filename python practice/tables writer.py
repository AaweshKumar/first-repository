n = int(input("enter beginning value:"))
e = int(input("enter ending value:"))

for i in range(n,e+1):
    for j in range(1,11):
        if (j==1):
            print('\n' , "table of" , i , '\n')
        print( i ,'X', j ,'=',i*j)