class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        win_size = len(word)
        l, r = 0, win_size
        curr, max_size = 0, 0
        while r <= len(sequence):
            if sequence[l:r] == word*(curr + 1):
                curr += 1
                r += win_size
            else:
                max_size = max(curr, max_size)
                curr = 0
                l += 1
                r = l + win_size
        return max(max_size, curr)
        