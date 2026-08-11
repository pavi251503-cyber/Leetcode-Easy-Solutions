"""
Problem name: Ransom Note
Problem no:383
Difficulty:Easy
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        # Count letters in magazine
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Use letters for ransomNote
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False

            count[ch] -= 1

        return True