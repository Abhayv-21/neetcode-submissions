class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        ## TC - O(mlogn)
        # for row in matrix:
        #     left = 0
        #     right = len(row)-1
        #     while left<right:
        #         mid = (left+right)//2
        #         if target>row[mid]:
        #             left = mid+1
        #         elif target<row[mid]:
        #             right = mid-1
        #         elif target == row[mid]:
        #             return True
        
        # return False

        left = 0
        n = len(matrix)
        m = len(matrix[0])
        right = m*n-1

        while left<=right:
            mid = (left+right)//2
            row = mid//m
            col = mid%m
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                left = mid+1
            elif target < matrix[row][col]:
                right = mid-1
        return False