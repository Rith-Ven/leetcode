class Solution:
    def romanToInt(self, s: str) -> int:
        # going from left to right, largest to smallest
        # if smaller comes before the larger, subtract it out

        rn = {"I":  1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0

        for i in range(len(s)):
            if i+1 < len(s) and rn[s[i]] < rn[s[i+1]]:  # This means subtract
                result -= rn[s[i]]
            else:
                result += rn[s[i]]

        return result
