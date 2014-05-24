#!/usr/bin/env
import collections
class Solution:
    # @param A, a list of integers, every number except one appears twice
    # @return integer - The number that only appeared once
    def singleNumber(self, A):
        c = collections.Counter(A)
        # Return the counter in the reverse order, return the first element of the first tuple
        return c.most_common()[::-1][0][0]

so = Solution()
list_of_nos = [1,1,2,3,3]
print so.singleNumber(list_of_nos)

