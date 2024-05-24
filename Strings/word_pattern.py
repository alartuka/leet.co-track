## Link to the problem: https://leetcode.com/problems/word-pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s2 = s.split(" ")
        n = len(pattern)

        if n != len(s2):
            return False
        
        pattern_to_word = dict()
        word_to_pattern = dict()
        pairs = set(zip(pattern, s2))

        for character, word in pairs:
            if character in pattern_to_word and pattern_to_word[character] != word:
                return False
            if word in word_to_pattern and word_to_pattern[word] != character:
                return False

            # character & word pair doesn't exist; add them in the dicts
            pattern_to_word[character] = word
            word_to_pattern[word] = character
      
        # s follows the pattern
        return True
