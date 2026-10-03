class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set(nums)
        return not len(nums) == len(num_set)