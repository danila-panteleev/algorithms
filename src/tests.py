import algorithms as alg
from collections import OrderedDict


TEST_CASE = OrderedDict({
    (1, 2, 3, 4, 5, 6, 7): [1, 2, 3, 4, 5, 6, 7],
    (7, 6, 5, 4, 3, 2, 1): [1, 2, 3, 4, 5, 6, 7],
    (-1, 4, 6, 3, 0, 6, 5): [-1, 0, 3, 4, 5, 6, 6],
    (4, 4, 4, 0, -1, 0, 2): [-1, 0, 0, 2, 4, 4, 4],
    (-5, -2, 6, -3, 88, 3423, -56654): [-56654, -5, -3, -2, 6, 88, 3423]
})


def test_fabric(sort_func):
    for case in TEST_CASE.keys():
        print(f'case {case} for {sort_func.__name__} testing')
        result = sort_func(case)
        print(f'result {result}')
        assert result == TEST_CASE[case]
        print(f'case {case} ok')


def test_bubble_sort():
    test_fabric(alg.bubble_sort)


def test_insert_sort():
    test_fabric(alg.insert_sort)


def test_selection_sort():
    test_fabric(alg.selection_sort)


def test_merge_sort():
    test_fabric(alg.merge_sort)


if __name__ == '__main__':
    test_bubble_sort()
    test_insert_sort()
    test_selection_sort()
    test_merge_sort()