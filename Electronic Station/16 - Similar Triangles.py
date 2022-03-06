'''Это миссия по проверке сходства двух треугольников.

Вам даны два списка в качестве координат вершин каждого треугольника.
Ты должен вернуть буль. (Трассеугольники похожи или нет)'''

from typing import List, Tuple
from itertools import combinations
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: list, coords_2: list) -> bool:
    first = sorted([(x[0] - y[0])**2 + (x[1] - y[1])**2 for x, y in combinations(coords_1, 2)])
    second = sorted([(x[0] - y[0])**2 + (x[1] - y[1])**2 for x, y in combinations(coords_2, 2)])
    res = tuple(itm[0] / itm[1] for itm in zip(first, second))
    return all(itm == res[0] for itm in res)


if __name__ == '__main__':
    # similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)])
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
