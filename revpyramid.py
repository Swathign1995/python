import sys
n=int(sys.argv[1])
for i in range(n, -1, -1):
    tmp=''
    for j in range(0, i + 1):
        tmp='%s *' % tmp
    print tmp
    #print
 
