class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashComplement = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashComplement:
                return [i, hashComplement[complement]]
            hashComplement[num] = i
            