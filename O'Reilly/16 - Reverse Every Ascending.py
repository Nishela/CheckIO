'''Создайте и верните новую итерацию, которая содержит те же элементы, что и итерируемые элементы аргумента,
но с обратным порядком элементов внутри каждого максимального строго возрастающего подсписка.
Эта функция не должна изменять содержимое исходной итерации.'''

def reverse_ascending(items):
    # your code here
	res_list = []
	sublist = []
	prev_number = None
	for itm in items:
		if prev_number == None or itm > prev_number:
			sublist.append(itm)
		else:
			res_list.append(sublist[::-1])
			sublist = [itm]
		prev_number = itm
	if sublist:
		res_list.append(sublist[::-1])
	return [itm for i in res_list for itm in i]
		

if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
