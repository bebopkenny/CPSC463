def bubble_sort(arr):
    n = len(arr)
    data = list(arr) 
    if n < 2:
        return data

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

def in_place_sort(arr):
    for i in range(0, len(arr) - 1):
        curr_min_index = i 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr_min_index]:
                curr_min_index = j
        
        arr[i], arr[curr_min_index] = arr[curr_min_index], arr[i]
    return arr

def out_place_sort(arr):
    U = list(arr)
    S = []
    while U:
        min_index = 0
        for j in range(1, len(U)):
            if U[j] < U[min_index]:
                min_index = j

        U[min_index], U[-1] = U[-1], U[min_index]
        S.append(U.pop())
    return S

print(in_place_sort([1, 4, 5, 6, 3, 7, 0, 12]))
print(out_place_sort([1, 4, 5, 6, 3, 7, 0, 12]))



