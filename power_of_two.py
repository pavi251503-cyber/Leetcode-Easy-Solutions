'''
Problem name: Power of two
Problem no:231
Difficulty:Easy
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        return n > 0 and (n & (n - 1)) == 0
        