

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
        min = data[0]
        min_index = 0
        for i in range(len(data)):
            if data[i] < min:
                min = data[i]
                min_index = i
        result.append(min)
        data.pop(min_index)
    return result