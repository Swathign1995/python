import sys


#print sys.argv[1]

#n=sys.argv[1]
n=int(sys.argv[1])
type(n)
print(type(n))
for i in range (1,10):
    x=n*i
    print('%s * %s = %s' % (n,i,x) )
