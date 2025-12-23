import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(piles, h, k):
            hours_left = h
            for n in piles:
                hours_req = math.ceil(n / k)
                hours_left -= hours_req
            return hours_left >= 0
        
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            k = (l + r) // 2
            if feasible(piles, h, k):
                r = k - 1
                res = k
            else:
                l = k + 1
        return res


        