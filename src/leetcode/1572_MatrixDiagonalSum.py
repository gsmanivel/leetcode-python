def finalVal():
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    result = 0
    length = len(mat) - 1
    for i in range(0, length + 1):
        if i != length:
            result = result + mat[i][i] + mat[i][length]
        else:
            result = result + mat[i][i]
        length = length - 1
    return result


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/matrix-diagonal-sum/
