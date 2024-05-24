## Link to the problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for i in nums:
            x = nums.count(i)
            if x > 1: # appears more than once
                while x > 1: # remove the duplicates leaving out the last one
                    nums.remove(i)
                    x -= 1

        return len(nums)
