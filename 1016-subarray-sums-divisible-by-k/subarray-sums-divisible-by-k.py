class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remMap = collections.defaultdict(int)
        remMap[0] = 1
        curr_sum = 0
        ans = 0
        for num in nums:
            curr_sum += num
            prefix = curr_sum % k
            ans += remMap[prefix]
            remMap[prefix] += 1
        return ans