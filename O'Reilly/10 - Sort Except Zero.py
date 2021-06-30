'''Sort the numbers in an array. But the position of zeros should not be changed.'''

from typing import Iterable


def except_zero(items: list) -> Iterable:
    # your code here
	d = [itm for itm in items if itm != 0]
	indexes = [idx for idx, itm in enumerate(items) if itm == 0]
	d.sort()
	if indexes != []:
		for idx in indexes:
			d.insert(idx, 0)
	return d


# def except_zero(items: list) -> Iterable:
#     sorted_items = filter(lambda x: x != 0, sorted(items))
#     print(list(sorted_items))
#     print(items)
#     for item in items:
#         yield next(sorted_items) if item else item


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    # assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    # assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    # assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    # assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")
