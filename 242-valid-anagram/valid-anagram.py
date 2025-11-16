class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_arr = [0]*26
        if len(s) != len(t):
            return False
        for char in s:
            char_arr[ord(char) - ord("a")] += 1
        for char in t:
            if char_arr[ord(char) - ord("a")] > 0:
                char_arr[ord(char) - ord("a")] -= 1
            else:
                return False
        return True