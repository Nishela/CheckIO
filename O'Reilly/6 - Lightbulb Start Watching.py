# Taken from mission Lightbulb Intro

# from datetime import datetime
# from typing import List
#
#
# def sum_light(els: List[datetime]) -> int:
#     """
#         how long the light bulb has been turned on
#     """
#     on = els[::2]
#     off = els[1::2]
#     res = [(itm - on[off.index(itm)]).total_seconds() for itm in off]
#     return sum(res)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sum_light(els=[
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#     ]) == 610
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ]) == 1220
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#         datetime(2015, 1, 12, 11, 10, 10),
#         datetime(2015, 1, 12, 12, 10, 10),
#     ]) == 4820
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 1),
#     ]) == 1
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 13, 11, 0, 0),
#     ]) == 86410
#
#     print("The first mission in series is completed? Click 'Check' to earn cool rewards!")

from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    if not start_watching:
        on = els[::2]
        off = els[1::2]
        return sum([(itm - on[off.index(itm)]).total_seconds() for itm in off])
    else:
        if start_watching not in els:
            els.append(start_watching)
            els = sorted(els)
        els = els[els.index(start_watching):]
        on = els[::2]
        off = els[1::2]
        return sum([(itm - on[off.index(itm)]).total_seconds() for itm in off])



if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 5)))

    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        start_watching=datetime(2015, 1, 12, 10, 0, 5)) == 5

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], datetime(2015, 1, 12, 10, 0, 0)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 0)) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 10)) == 600

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 10, 10, 0)) == 620

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 10, 11)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 9, 11)) == 60

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")