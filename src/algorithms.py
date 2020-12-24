import math


def swap(data, left_index, right_index):
    data[left_index], data[right_index] = data[right_index], data[left_index]
    return data


def bubble_sort(data):
    data = list(data)
    while True:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data = swap(data, i, i + 1)
                swapped = True
        if not swapped:
            return data


def insert_sort(data):
    data = list(data)
    result = [data[0]]
    data.pop(0)
    while data:
        for i in range(len(result)):
            if data[0] <= result[i]:
                result.insert(i, data[0])
                break
            elif i == len(result) - 1:
                result.append(data[0])
        data.pop(0)
    return result


def selection_sort(data):
    data = list(data)
    result = []
    while data:
        min_value = data[0]
        min_index = 0
        for i in range(len(data)):
            if data[i] < min_value:
                min_value = data[i]
                min_index = i
        result.append(min_value)
        data.pop(min_index)
    return result


def merge_sort(data):
    data = list(data)

    if len(data) == 2 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    elif len(data) > 2:
        left = merge_sort(data[:(len(data) // 2)])
        right = merge_sort(data[(len(data) // 2):])
        data = []

        while left:
            if right:
                if left[0] <= right[0]:
                    data.append(left[0])
                    left.pop(0)
                else:
                    data.append(right[0])
                    right.pop(0)

        for i in right:
            data.append(i)

    return data


def quick_sort(data):
    """
    mid := (low + high) / 2
        if A[mid] < A[low]
            swap A[low] with A[mid]
        if A[high] < A[low]
            swap A[low] with A[high]
        if A[mid] < A[high]
            swap A[high] with A[mid]
    pivot := A[high]
    :param data:
    :return:
    """
    def partition(partition_data):
        pivot_index = len(partition_data) - 1
        pivot_value = partition_data[pivot_index]
        i = 0
        while i < pivot_index:
            if partition_data[i] > pivot_value:
                replace_value = partition_data.pop(i)
                partition_data.insert(len(partition_data), replace_value)
                pivot_index -= 1
                continue
            i += 1
        return partition_data, pivot_index

    data = list(data)

    if len(data) < 2:
        return data

    packed_data = partition(data)
    data = packed_data[0]
    pivot_index = packed_data[1]

    left = quick_sort(data[:pivot_index])
    right = quick_sort(data[pivot_index:])

    return left + right