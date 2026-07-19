class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0   #left pointer

        for r in range(len(nums)): # iterate right pointer through
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l] # swap left and right 
                l += 1
                