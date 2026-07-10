'''
Problem name: Valid Anagram
Problem no: 242
Difficulty: Easy
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)