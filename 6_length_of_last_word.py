#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
	s_split = s.split()
	# Splits 'Hello World' into ['Hello', 'World']
	if s_split:
            # s_split[-1] returns the last index in the array, here, the string 'World'
	    last_word = s_split[-1]
	    return len(last_word)
        else:
            return 0

so = Solution()
s1 = "Hello World"
s1_len = so.lengthOfLastWord(s1)
assert s1_len == 5
print "The length of the last word in [%s] is [%s]" %(s1, s1_len)
s2 = "Hi"
s2_len = so.lengthOfLastWord(s2)
assert s2_len == 2
print "The length of the last word in [%s] is [%s]" %(s2, s2_len)
s3 = "   "
s3_len = so.lengthOfLastWord(s3)
assert s3_len == 0
print "The length of the last word in [%s] is [%s]" %(s3, s3_len)
		    
