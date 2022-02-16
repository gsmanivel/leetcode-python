def finalVal():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    maxInCandies = max(candies)
    rest = [False] * (len(candies))
    for i in range(len(candies)):
        if (candies[i] + extraCandies) > maxInCandies:
            rest[i] = True
    return rest


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
