## Link to the problem: https://leetcode.com/problems/reverse-integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        s = s[::-1]
        if(x < 0):
            n = -1 *  int(s[:-1])
        else:
            n = int(s)
            
        if n >= ((-2)**31) and n <= ((2**31) - 1):
            return n
        return 0
