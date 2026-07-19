class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {} # Creates dictionaries 

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)      #Accesses the key 
        #     print("CountS: " + str(countS))
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        #     print("CountT: " + str(countT))

        # return countS == countT

        ds, dt = {}, {}

        for letter in list(s):
            if letter in ds:
                ds[letter] += 1
            else:
                ds[letter] = 1
        for letter in list(t):
            if letter in dt:
                dt[letter] += 1
            else:
                dt[letter] = 1
        return ds == dt



def main():
    s = "jar"
    t = "jam"

    solution = Solution()
    print(solution.isAnagram(s, t))


if __name__ == "__main__":
    main()