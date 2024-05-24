## Link to the problem: https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:

        x = n
        while True:
            if x == 1 or x == 7: # happy number found
                return True
            if (x%10) != 0 and (x//10) == 0: # x = single digit & != 1 or 7; not happy number
                return False
            
            t = 0
            while x > 0: # square and sum digits of x
                t += (x % 10)**2
                x = x//10
            x = t
        pass
