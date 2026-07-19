class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {} # Creates dictionaries 

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)      #Accesses the key 
            print("CountS: " + str(countS))
            countT[t[i]] = 1 + countT.get(t[i], 0)
            print("CountT: " + str(countT))

        return countS == countT


def main():
    s = "jar"
    t = "jam"

    solution = Solution()
    print(solution.isAnagram(s, t))


if __name__ == "__main__":
    main()