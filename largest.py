import sys
x=int(sys.argv[1])
y=int(sys.argv[2])

if(x>y):
    print("{0} is greater than {1}".format(x,y))
elif(y>x):
    print("{0} is greater than {1}".format(y,x))
else:
    print("both x and y are equal")
