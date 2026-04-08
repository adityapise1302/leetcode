from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = Counter(words)
        heapWords = [(-val, key) for key, val in wordFreq.items()]
        heapq.heapify(heapWords)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heapWords)[1])
        return res