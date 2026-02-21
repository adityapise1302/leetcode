class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        s = []
        for i, t in enumerate(temperatures):
            while len(s) > 0 and temperatures[s[-1]] < t:
                j = s.pop()
                res[j] = i - j
            s.append(i)
        return res