def finalVal():
    gain = [-4,-3,-2,-1,4,3,2]
    maxi = 0
    result = 0
    for i in gain:
        maxi += i
        result = max(result, maxi)
    return result


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/minimum-time-visiting-all-points/
