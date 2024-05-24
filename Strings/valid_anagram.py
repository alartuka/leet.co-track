## Link to the problem: https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        st = dict() # hold the num of occurrances for each letter in s
        ts = dict() # hold the num of occurrances for each letter in t

        for i in s: # count each letter's occurances and map it to st
            st[i] = st.get(i, 0) + 1 # [i]key's value += 1; [i]key not  exist in st => adds [i]key with value = 1 to st

        for k in t: # count each letter's occurances and map it to ts
            ts[k] = ts.get(k, 0) + 1 # [i]key's value += 1; [i]key not  exist in st => adds [i]key with value = 1 to st

        return st == ts # compare keys & thier values of each dicts
