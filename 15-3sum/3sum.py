class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        fix_set = set()
        for fix in range(len(nums) - 2):
            if nums[fix] in fix_set:
                continue
            fix_set.add(nums[fix])
            l = fix + 1
            r = len(nums) - 1
            rem = 0 - nums[fix]
            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum < rem:
                    l += 1
                elif cur_sum > rem:
                    r -= 1
                else:
                    res.append([nums[fix], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res