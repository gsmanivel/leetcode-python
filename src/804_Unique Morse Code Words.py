def finalVal():
    words = ["a"]

    encoding = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    albha = "abcdefghijklmnopqrstuvwxyz"
    resultSet = set()
    for word in words:
        tempString = ""
        for ch in word:
            tempString += encoding[albha.index(ch)]
        print(tempString)
        resultSet.add(tempString)
    return len(resultSet)


# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/unique-morse-code-words/
