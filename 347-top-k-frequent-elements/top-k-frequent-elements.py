class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        idx = len(freq) - 1
        while k > 0:
            res += freq[idx]
            k -= len(freq[idx])
            idx -= 1
        return res
            