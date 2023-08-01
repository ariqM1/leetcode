class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row*col-1
        while l <= r:
            mid = (l + r) // 2
            num = matrix[mid//col][mid%col]

            if num > target:
                r = mid-1
            elif num < target:
                l = mid+1
            else:
                return True
            
        return False


