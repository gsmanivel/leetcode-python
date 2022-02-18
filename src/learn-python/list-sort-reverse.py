def reverseAndSort():
    nums = [5, 4, 1, 2, 10, 9]
    letters = ['a', 'c', 'b', 'f', 'd']
    flag = [True, True, False, True, False]

    # reverse numbers
    print('Reverse numbers:')
    reversed_nums = list(reversed(nums))
    print(nums)
    print(reversed_nums)
    print('-------------------')

    # reverse letters
    print('Reverse letters:')
    reversed_letters = list(reversed(letters))
    print(letters)
    print(reversed_letters)
    print('-------------------')

    # reverse boolean
    print('Reverse boolean:')
    reversed_boolean = list(reversed(flag))
    print(flag)
    print(reversed_boolean)
    print('-------------------')

    # sort Numbers - Ascending order
    print('Sort Nums - Ascending order:')
    sorted_nums = sorted(nums)
    print(nums)
    print(sorted_nums)
    print('-------------------')

    # sort Numbers - Descending order
    print('Sort Nums - Descending order:')
    sorted_nums = sorted(nums, reverse=True)
    print(nums)
    print(sorted_nums)
    print('-------------------')

    # sort Letters - Ascending order
    print('Sort Letters - Ascending order:')
    sorted_letters = sorted(letters)
    print(letters)
    print(sorted_letters)
    print('-------------------')

    # sort Letters - Descending order
    print('Sort Letters - Descending order:')
    sorted_letters = sorted(letters, reverse=True)
    print(letters)
    print(sorted_letters)
    print('-------------------')

    # sort Boolean - Ascending order
    print('Sort Boolean - Ascending order:')
    sorted_Boolean = sorted(flag)
    print(flag)
    print(sorted_Boolean)
    print('-------------------')

    # sort Boolean - Descending order
    print('Sort Boolean - Descending order:')
    sorted_Boolean = sorted(flag, reverse=True)
    print(flag)
    print(sorted_Boolean)
    print('-------------------')

    # Sorting using list.sort()
    nums.sort(reverse=True)
    letters.sort(reverse=True)
    flag.sort(reverse=True)
    print(nums)
    print(letters)
    print(flag)


if __name__ == '__main__':
    reverseAndSort()
