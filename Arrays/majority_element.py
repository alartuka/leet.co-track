## Link to the problem: https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in nums:
            x = nums.count(i)
            if x > (n/2):
                return i
