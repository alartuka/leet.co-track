## Link to the problem: https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = dict() # hold the #occurrances of each letter in ransomNote
        m = dict() # hold the #occurrances of each letter in magazine that is in ransomNote

        for i in ransomNote: # count the occurrances of each letter in RansomNote
            r[i] = r.get(i, 0) + 1

        for i in magazine: # count the occurrances of each letter in magazine that is in ransomNote
            if i in ransomNote:
                m[i] = m.get(i, 0) + 1
        # now dicts r & m contaim same keys 
        for i in r: # compare the #occurrances of each letter in r & m
            if r.get(i, 0) > m.get(i, 0): # m doesn't have enough of same letter for r
                return False

        # dicts r & m contain same keys & values/ r can be made from m 
        return True
            
