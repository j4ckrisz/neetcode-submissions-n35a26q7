class Solution:
    def findMin(self, nums: List[int]) -> int:
        val=0
        if len(nums)  == 1:
            val=nums[0]
            return val
        for n in range(0, len(nums)):
            if nums[n] < nums[n-1]:
                val = nums[n]

        return val