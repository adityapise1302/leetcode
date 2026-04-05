class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, path):
            if index == len(candidates) or sum(path) > target:
                return
            elif sum(path) == target:
                res.append(path.copy())
                return
            # Include 
            path.append(candidates[index])
            dfs(index, path)
            # Don't Include
            path.pop()
            dfs(index + 1, path)
        dfs(0, [])
        return res
            
