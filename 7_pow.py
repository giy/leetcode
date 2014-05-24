#!/usr/bin/python
class Solution:
     # @param x, a float
     # @param n, a integer
     # @return a float
     def pow(self, x, n):
         if n == 0: return 1
	 else:
	     return x*pow(x, n-1)

so = Solution()
p1 = so.pow(2,8)
assert p1 == 256
print "2^8 is %s" %p1
p2 = so.pow(5,3)
assert p2 == 125
print "5^3 is %s" %p2
p3 = so.pow(2,-4)
assert p3 == 0.0625
print "2^-4 is %s" %p3
