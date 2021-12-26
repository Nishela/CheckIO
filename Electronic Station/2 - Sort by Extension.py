'''You are given a list of files.
You need to sort this list by the file extension. The files with the same extension should be sorted by name.'''

from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    # your code here
    # num_dict = {}
    # result = []
    # for file in files:
    #     num_dict.setdefault(file.count('.'), list()).append(file)
    # for key, value in num_dict.items():
    #     if key == 1:
    #         result.extend(sorted(value, key=lambda x: x))
    #     else:
    #         result.extend(sorted(value, key=lambda x: x[:x.rfind('.')]))
    # return result
    names = {}
    result = []
    null_names = []
    for file in files:
        name = file[:file.rfind('.') + 1]
        sec_name = file[file.rfind('.') + 1:]
        if name == '.':
            null_names.append(file)
        else:
            names.setdefault(sec_name, list()).append(name)
    for key, value in sorted(names.items()):
        for item in sorted(value):
            result.append(item+key)
    print(0)
    return sorted(null_names) + result

if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")

