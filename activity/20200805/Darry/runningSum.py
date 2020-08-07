class Solution:
    def runningSum(self, nums):
        res = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            res.append(temp)
        return res
