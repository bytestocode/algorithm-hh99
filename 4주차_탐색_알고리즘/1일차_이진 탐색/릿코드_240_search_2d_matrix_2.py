def searchMatrix(matrix, target) -> bool:
    row = 0

    while row < len(matrix):
        start = 0
        end = len(matrix[0]) - 1

        if matrix[row][0] > target:
            return False

        while start <= end:
            mid = (start + end) // 2
            # 아래 코드 리스트 인덱스 벗어남...
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                return True

        row += 1


    return False


print(
    searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
                 5))
