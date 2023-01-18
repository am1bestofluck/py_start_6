"""
progression - арифметическая прогрессия

positions - индексы элементов массива

pow-positive - возведение  a в степень б
"""
# *lambda, filter, *map, *zip, *enumerate, *list comprehension


from typing import List


def progression(start_: int, step: int, len_: int):
    if not isinstance(len_,int): 
        raise TypeError 
    if len_ <= 1:
        raise ValueError 
    # values = map()
    keys = list(range(1, len_+1))
    values = list(map(lambda pos: start_ + (pos-1)*step, keys))
    out = list(zip(keys,values))
    return out

def positions(lst: List[int | float] = [-5, 9, 0, 3, -1, -2, 1, 4, -2,
                                        10, 2, 0, -9, 8, 10, -9, 0, -5,
                                        -5, 7],
              min_: int | float = 5,
              max_: int | float = 15) -> List[int]:
    out = [ind for ind,val in enumerate( lst) if min_ < val < max_]
    sorted( out)
    return out


pow_positive = lambda a, b: 1 if b == 0 else a*pow_positive(a, b-1)


def main():
    print(progression(10,5,5))
    assert positions() == [1, 9, 13, 14, 19]
    assert pow_positive(2, 10) == 2**10


if __name__ == "__main__":
    main()
