class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        
        prevMap = {} # value -> index

        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i
        return []
