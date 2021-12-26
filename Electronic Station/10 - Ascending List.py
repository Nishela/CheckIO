'''Determine whether the sequence of elements items is ascending such that each of its elements is strictly larger than (and not merely equal to) the preceding element.

Input: Iterable with ints.

Output: Bool.'''

from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    # your code here
    # if not items or len(items) == 1:
    #     return True
    # else:
    #     current = items[0]
    #     for idx in range(1, len(items)):
    #         if current < items[idx]:
    #             current = items[idx]
    #         else:
    #             return False
    #     return True
    return items == sorted(set(items))



if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

