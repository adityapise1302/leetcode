class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        trackHash = dict()
        resKFreq = []
        for num in nums:
            trackHash[num] = trackHash.get(num, 0) + 1
        for i in range(k):
            maxFreq = 0
            n = -1
            for num, freq in trackHash.items():
                if freq > maxFreq:
                    n = num
                    maxFreq = freq
            resKFreq.append(n)
            trackHash[n] = 0
        return resKFreq