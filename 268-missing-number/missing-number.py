class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_res = 0
        for num in nums:
            xor_res = xor_res ^ num
        for i in range(len(nums) + 1):
            xor_res = xor_res ^ i
        return xor_res
