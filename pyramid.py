hello="welcome to pyhon"
print(hello)
import sys
n=int(sys.argv[1])

def pypart(n):
 for i in range(0,n):
        tmp=''
        for j in range(0,i+1):
            tmp = '%s *' % tmp
        print tmp
       # print
            
pypart(n)
