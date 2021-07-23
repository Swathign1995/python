#!/usr/bin/python

x=[2,4,1,6,7,9,10,100,0]


print x


"""
thi is multiline comment
ok
"""

'''
print biggest number in the list
'''
x.sort()
f=x[-1]

print(x)
print(f)

'''
print last biggest number
'''
f=x[-2]
print(f)

'''
print list in reverse order
'''
x.reverse()
print(x)
'''
take a back of original variable to another variable using copy module 
i.e import copy and copy.deepcopy()
then remove element from original variable and print both variable with proper message
'''
import copy
x=[1,2,3,4,5,6,7,8,77]
y=copy.deepcopy(x)
print(y)
print(len(y))
print 'Hello x variable value is ' ,x,' this is continuation'




