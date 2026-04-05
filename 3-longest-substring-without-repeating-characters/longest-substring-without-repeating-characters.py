class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = collections.defaultdict(int)
        l, r = 0, 0
        res = 0
        while r < len(s):
            if charMap[s[r]] == 1:
                res = max(res, r - l)
                charMap[s[l]] -= 1
                l += 1
            else:
                charMap[s[r]] += 1
                r += 1
        res = max(res, r - l)
        return res

        
        