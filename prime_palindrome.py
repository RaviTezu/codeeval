#!/usr/bin/python
from __future__ import print_function
N=1000
pp = 0

def pP(n):
    """ Takes a number and return True if Palindrom or else False"""
    s = str(n)
    l = len(s)
    if l%2 == 0:
        return s.count(s[0]) == l
    else:    
        sm = l/2
        return s[:sm] == s[sm:][::-1]

for num in xrange(0,N):
    print("num", num)
    if pP(num):
        pp = num
print(pp)
        
