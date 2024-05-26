## Link to the problem: https://leetcode.com/problems/palindrome-number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: # -xx
            return False
            
        if (x % 10) == 0 and x > 0: # x0
            return False

        y = x
        t = 0
        while y > 0:
            c = (y % 10)
            t += c
            y = y / 10
            if y > 0:
                t *= 10

        return t == x
