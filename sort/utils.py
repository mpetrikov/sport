def insert_with_keep_sorting(arr, elem):
    is_inserted = False
    for i in range(len(arr)):
        if elem <= arr[i]:
            arr.insert(i, elem)
            is_inserted = True
            break
    if not is_inserted:
        arr.append(elem)

