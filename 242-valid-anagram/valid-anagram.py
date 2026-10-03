class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = [0] * 26
        t_table = [0] * 26
        for char in s:
            s_table[ord(char) - ord('a')] += 1
        for char in t:
            t_table[ord(char) - ord('a')] += 1
        return s_table == t_table