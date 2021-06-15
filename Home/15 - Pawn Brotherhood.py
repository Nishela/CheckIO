from pprint import pprint


def safe_pawns(pawns: set) -> int:
    indexes = set()
    safe = 0
    for paw in pawns:
        row, col = int(paw[1]), ord(paw[0])
        indexes.add((row, col))
    for row, col in indexes:
        is_safe = ((row - 1, col - 1) in indexes or (row - 1, col + 1) in indexes)
        if is_safe:
            safe += 1
    return safe


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    # assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

