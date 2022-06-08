import typing


def find_insert_position(array: typing.List[int], value: int) -> int:
    d = array[0]
    i = 0
    while d < value:
        i += 1
        d = array[i]
    return i


if __name__ == "__main__":
    A = [1, 2, 3, 3, 3, 5]
    x = 4

    print(find_insert_position(A, x))
    assert find_insert_position(A, x) == 5
