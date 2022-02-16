def finalVal():
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"

    count = 0
    itemDesc = ["type", "color", "name"]
    for item in items:
        flag = False
        for element in range(len(item)):
            if ruleKey is itemDesc[element] and item[element] is ruleValue:
                flag = True
            if flag:
                count += 1
                break
    return count


if __name__ == '__main__':
    print(finalVal())

# https://leetcode.com/problems/count-items-matching-a-rule/
