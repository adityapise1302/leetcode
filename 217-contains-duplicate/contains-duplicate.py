class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        track_dup_set = set()
        for num in nums:
            if num in track_dup_set:
                return True
            track_dup_set.add(num)
        return False
