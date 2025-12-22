class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        l_m, r_m = 0, len(matrix) - 1
        row = -1
        while l_m <= r_m:
            mid_m = (l_m + r_m) // 2
            first = matrix[mid_m][0]
            last  = matrix[mid_m][-1]
            if first <= target <= last:
                row = mid_m
                break
            elif target < first:
                r_m = mid_m - 1
            else: 
                l_m = mid_m + 1

        if row == -1:
            return False

        l_n, r_n = 0, len(matrix[row]) - 1
        while l_n <= r_n:
            mid_n = (l_n + r_n) // 2
            val = matrix[row][mid_n]
            if val == target:
                return True
            elif val < target:
                l_n = mid_n + 1
            else:
                r_n = mid_n - 1

        return False
