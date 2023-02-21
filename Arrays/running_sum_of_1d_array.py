## Link to problem: https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        Returns the running sum of an array as sum(nums[0]…nums[i]).
        :requires: 
            1 <= nums.length <= 1000
            -10^6 <= nums[i] <= 10^6
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        run_sum = list()
        for n in nums:
            sum += n
            run_sum.append(sum)
        return run_sum
