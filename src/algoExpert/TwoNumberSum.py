# Solution # 1 - Traditional way
def coding1():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                result.append(array[i])
                result.append(array[j])
    return result


# Solution # 2 - Potential Match
def coding2():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [num, potentialMatch]
        else:
            nums[num] = True


# Solution # 3 - Sort and navigate from right and left
def coding3():
    array = [3, 5, -4, 8, 11, 1, -1, 6]  # [3, 5, -4, 8, 10, 1, -1, 6, 7]  # [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        num1 = array[left]
        num2 = array[right]
        sums = num1 + num2
        if sums == targetSum:
            return [num1, num2]
        elif sums > targetSum:
            right -= 1
        else:
            left += 1
    return []


def coding4():
    array = [3, 11, -4, -1, 5, 1, 8, 6]  # [3, 5, -4, 8, 10, 1, -1, 6, 7]  # [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    length = len(array)
    for i in range(length):
        currentNum = array.pop()
        potentialMatch = targetSum - currentNum
        if potentialMatch in array:
            return [potentialMatch, currentNum]
    return []


if __name__ == '__main__':
    print(coding4())
