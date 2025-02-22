# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        for idx in range(len(strx)):
            if strx[idx] != strx[len(strx)-1-idx]: 
                return False 

        return True