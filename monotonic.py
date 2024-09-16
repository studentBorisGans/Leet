class Solution(object):
    def isMonotonic(self, nums):
        n = len(nums)

        first= nums[0]
        last= nums[n-1]
        if first>last:
            for k in range(n-1):
                if nums[k]<nums[k+1]:
                    return False
        elif first==last:
            for k in range(n-1):
                if nums[k]!=nums[k+1]:
                    return False
        else:
            for k in range(n-1):
                if nums[k]>nums[k+1]:
                    return False
        return True
