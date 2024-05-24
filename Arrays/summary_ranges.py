## Link to the problem: https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        result = []

        if n == 0: # empty
            return result
        if n == 1: # one number; no seq
            result.append(str(nums[0]))
            return result

        f = nums[0]
        prev = nums[0]
        i = 1

        while i < n:
            j = i
            y = 1
            while (j < n) and (nums[j] == (prev + 1)):
                prev = nums[j]
                y += 1
                j += 1

            x = str(f)
            if f != prev: # first != last; consec nums/seq
                x += "->"
                x += str(prev)
            result.append(x)

            if j < n: # reset first&last to start next seq,
                f = nums[j]
                prev = nums[j]
            
            i += y # skip nums in prev seq
            if (i - 1) == n - 1: # next seq = last & only one num
                x = str(nums[i - 1])
                result.append(x)
                break

        return result
            











        
        
