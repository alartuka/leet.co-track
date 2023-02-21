## Link to problem: https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :requires:
            1 <= s.length <= 2 * 105
            s consists only of printable ASCII characters.
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        if s.isalpha() == False:
            for i in s:
                if i.isalnum() == False:
                    s = s.replace(i, "")
        return s[::-1] == s
