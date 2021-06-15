'''You have to split a given array into two arrays.
If it has an odd amount of elements, then the first array should have more elements.
If it has no elements, then two empty arrays should be returned.'''

def split_list(items: list) -> list:
    # your code here
    # if len(items) == 0:
    #     l1 = []
    #     l2 = []
    # elif len(items) % 2 != 0:
    #     l1 = items[: len(items) // 2 + 1]
    #     l2 = items[len(items) - len(l1) + 1:]
    # else:
    #     l1 = items[: len(items) // 2]
    #     l2 = items[len(items) - len(l1):]

    if len(items) == 0:
        return [[], []]
    elif len(items) % 2 == 0:
        mid_p = int(len(items) / 2)
    else:
        mid_p = int((len(items) / 2) + 1)
    return [items[:mid_p], items[mid_p:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1,1,1,1,1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")