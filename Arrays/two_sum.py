## Link to problem: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        Returns the indices of the two numbers in nums such that they add up to target
        :requires:
            2 <= nums.length <= 104
            -109 <= nums[i] <= 109
            -109 <= target <= 109
            Only one valid answer exists.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idc = list()
        for i in range(len(nums)):
            x = 0
            if (target - nums[i]) in nums:
                x = nums.index(target - nums[i])
            if x != i and nums[x] + nums[i] == target:
                idc.append(i)
                idc.append(x)
                return idc
        return idc
