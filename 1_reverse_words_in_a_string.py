#!/usr/bin/python
class Solution:

    def reverse_words(self, s):
        """Reverses the words of the given string"""

	# s.split() returns ['blue', 'is', 'sky', 'the']
	# convert the list to a string using join
	return ' '.join(s.split()[::-1])

s = "the sky is blue"
so = Solution()
ans = so.reverse_words(s)
expected = "blue is sky the"
assert ans == expected
print ans
