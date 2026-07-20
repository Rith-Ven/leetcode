class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        threshold = len(nums) / 2
        
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        for key in hashmap:
            print("Checking " + str(key))
            if hashmap[key] >= threshold:
                return key
            
### NOTE This uses time complexity of O(n) and space complexity of O(n)
# Most optimal can be achieved in O(1) space using Boyer-Moore



def main():
    nums = [8,8,7,7,7]

    solution = Solution()
    print(solution.majorityElement(nums))


if __name__ == "__main__":
    main()