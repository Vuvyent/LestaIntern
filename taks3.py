# ЗАДАНИЕ 3
# На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
# Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы
# считаете, что функция соответствует заданным критериям.

# Для реализации был выбран алгоритм сортировки слиянием. Причиной, по которой был выбран данный алгоритм заключается в
# следующем: все простые сортировки, такие как пузырьковая, вставками и им подобные работают в худшем случае за О(N^2).
# Быстрая сортировка и сортировка слиянием работают в среднем за О(n*logn), но быстрая может уходить в О(N^2), тогда
# как слиянием выполнятется стабильно О(n*logn)ю

def merge(data, left, mid, right):
    first = mid - left + 1
    second = right - mid

    left_arr = [0] * first
    right_arr = [0] * second

    for i in range(0, first):
        left_arr[i] = data[left + i]

    for j in range(0, second):
        right_arr[j] = data[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < first and j < second:
        if left_arr[i] <= right_arr[j]:
            data[k] = left_arr[i]
            i += 1
        else:
            data[k] = right_arr[j]
            j += 1
        k += 1

    while i < first:
        data[k] = left_arr[i]
        i += 1
        k += 1

    while j < second:
        data[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(data, left, right):
    if left < right:
        mid = left + (right - left) // 2

        # Sort first and second halves
        merge_sort(data, left, mid)
        merge_sort(data, mid + 1, right)
        merge(data, left, mid, right)


if __name__ == "__main__":
    data = [3, 2, 1, 5, 4, 4, 8, 7]
    print(data)
    merge_sort(data, 0, len(data) - 1)
    print(data)