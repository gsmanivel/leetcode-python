def slicingList():
    letters = 'abcdefghi'
    letterList = list(letters)

    # slicing string
    print('letters-', letters)
    sliced_string = letters[::2]
    print('sliced_string-', sliced_string)

    # Reversing string
    reversed_string = letters[::-1]
    print('reversed_string-', reversed_string)

    # Working with List
    print('--------------------')
    # slicing list
    print('letterList-', letterList)
    sliced_letter = letterList[::2]
    print('Sliced List-', sliced_letter)

    # Reverse using slicing
    reversed_letters = letterList[::-1]
    print('Reversed List-', reversed_letters)


if __name__ == '__main__':
    slicingList()
