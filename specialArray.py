class Solution(object):
    def isArraySpecial(self, nums):
        
        n = len(nums)
        if n == 1 or n == 0:
            return True
        
        for i in range(n - 1):
            if ((nums[i] + nums[i+1]) % 2 == 0):
                return False
        return True
        