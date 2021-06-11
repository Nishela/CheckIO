'''Отсортируйте данный итератор таким образом, чтобы его элементы оказались в порядке убывания частоты их появления, то есть по количеству раз, которое они появляются в элементах. Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке, в котором стояли изначально в итераторе.
Входные данные: Итератор
Выходные данные: Итератор'''
from collections import Counter


def frequency_sort(items):
    # counts = Counter(items)
    counts = {}
    first = {}
    for i, item in enumerate(items):
        counts[item] = counts.get(item, 0) + 1
        if item not in first:
            first[item] = i
    return sorted(items, key=lambda x: (-counts[x], first[x]))


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

