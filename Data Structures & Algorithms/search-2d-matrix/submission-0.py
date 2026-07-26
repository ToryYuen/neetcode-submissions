class Solution:
    def binary_search(self, target, row) -> bool:
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            if matrix[r][0] <= target <= matrix[r][-1]:
                return self.binary_search(target, matrix[r])
        return False
        