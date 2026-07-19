class Solution: 
    def hasDuplicates(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False


def main():
    nums = [1,2,3,3]

    solution = Solution()
    print(solution.hasDuplicates(nums))


if __name__ == "__main__":
    main()