def swap(data, left: int, right: int):
    data[left], data[right] = data[right], data[left]
    return data


def bubble_sort(data):
    data = list(data)
    while True:
        swap_counter = 0
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data = swap(data, i, i + 1)
                swap_counter += 1
        if swap_counter == 0:
            return data