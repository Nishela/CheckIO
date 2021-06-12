

from typing import Union
from datetime import datetime

def sun_angle(time: str) -> Union[int, str]:
    sun_up = 6 * 60
    sun_down = 18 * 60
    my_time = datetime.strptime(time, '%H:%M')
    cur_time = my_time.time().hour * 60 + my_time.time().minute
    if cur_time in range(sun_up, sun_down + 1):
        res_angel = 180 * ((cur_time - sun_up) / (sun_down - sun_up))
        return res_angel
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

