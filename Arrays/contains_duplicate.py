## Link to problem: https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        Return true if any value appears at least twice in the array, and false if every element is distinct.
        :requires:
            1 <= nums.length <= 105
            109 <= nums[i] <= 109
        :type nums: List[int]
        :rtype: bool
        """
        
        return not(len(nums) == len(set(nums)))
