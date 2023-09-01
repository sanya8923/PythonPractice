def count_positives_sum_negatives(arr):
    count = 0
    summ = 0
    arr2 = []
    if arr is None or len(arr) == 0:
        return []
    for i in arr:
        if i > 0:
            count += 1
        elif i < 0:
            summ += i
    arr2.append(count)
    arr2.append(summ)
    return arr2
