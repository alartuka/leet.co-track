## Link to the problem: https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        ## Dictionary to hold the integer representations of the Roman numeral 
        rm = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        bw = s[::-1] # Reverse the Roman numeral str 
        n = len(bw)
        total = 0 
        prev = "I" # keeps track of previous r.n processed

        for i in range(0, n):
            if rm[bw[i]] >= rm[prev]:
                total += rm[bw[i]]
            else: # cases of IV/IX/XL/XC/CD/CM; 
                ## since s is processed from the back => the prev will always be the larger one for these cases; hence bw[i] is subtracted from total to give the integer it represents
                ## e.g (bw[i] = "I" and prev = "V" => bw[i] < prev; prev was already added to total => bw[i] is subtracted from total, rep. 4)
                total -= rm[bw[i]]

            prev = bw[i]

        return total

