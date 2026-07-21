class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        divider = 1 

        while x >= 10 * divider: # determine how large divier should be
            divider *= 10
        
        while x:
            right = x % 10 # Checks rightmost digit
            left = x // divider # Checks leftmost digit
            if left != right: return False

            x = (x % divider) // 10 #Chops of left digit using % and right using //
            divider /= 100
        return True
    



        #     if x < 0 or (x > 0 and x % 10 == 0):
        #     return False
        
        # reversed_half = 0
        # while reversed_half < x:
        #     reversed_half = reversed_half * 10 + x % 10
        #     x //=10

        # return x == reversed_half or x == reversed_half // 10

        