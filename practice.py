import sys
n=sys.argv[1]
n=int(sys.argv[1])


def find_prime(n):
    for i in range(1,n/2):
         if[(n//i)==0]:
             print("not prime number")
             return true
         break
    return false
    #else:
        # print("prime number")
     #return false
find_prime(n)   
