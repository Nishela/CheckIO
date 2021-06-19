
from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
	"""
		how long the light bulb has been turned on
	"""
	on = els[::2]
	off = els[1::2]
	res = sum([(itm - on[off.index(itm)]).total_seconds() for itm in off])
	# result = sum([i.seconds + i.days * 24 * 3600 for i in res])
	# for i in res:
	# 	sec = i.seconds
	# 	day = i.days * 24 * 3600
	# 	result.append(sec + day)
	return res


if __name__ == '__main__':
	print("Example:")
	print(sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	]))
	
	# These "asserts" are used for self-checking and not for an auto-testing
	assert sum_light(els=[
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
	]) == 610
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	]) == 1220
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
		datetime(2015, 1, 12, 11, 10, 10),
		datetime(2015, 1, 12, 12, 10, 10),
	]) == 4820
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 1),
	]) == 1
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 13, 11, 0, 0),
	]) == 86410
	
	print("The first mission in series is completed? Click 'Check' to earn cool rewards!")

