import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
for i in range(1,x):
    for j in range(1,y):
       z=i*j
       print('%s * %s = %s' % (i,j,z))

