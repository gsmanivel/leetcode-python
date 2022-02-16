def finalVal():
    arr = [1,1,2,2,3]
    a = 0
    b = 0
    c = 1
    result = 0
    arrLength = len(arr)
    for i in range(arrLength):
        for j in range(i+1, arrLength):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j+1, arrLength):
                    if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        result += 1
    return result


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/count-good-triplets/
