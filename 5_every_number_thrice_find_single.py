#!/usr/bin/env
import collections
class Solution:
    # @param A, a list of integers, every number except one appears twice
    # @return integer - The number that only appeared once
    def singleNumber(self, A):
        """The solution for this is the same as the solution to the previous problem, using collections.Counter we end up with a generic solution for both problems"""

	c = collections.Counter(A)
        # Return the counter in the reverse order, return the first element of the first tuple
        return c.most_common()[::-1][0][0]

so = Solution()
list_of_nos = [1,1,1,2,3,3,3]
single_no = so.singleNumber(list_of_nos)
assert single_no == 2
print single_no

