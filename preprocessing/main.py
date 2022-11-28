def create_2darray_from_strings(arr):
    result = []
    for i in range(len(arr)):
        result.append(list(arr[i]))
    return result

def create_str_arr_from_2d(arr):
    for i in range(len(arr)):
        arr[i] = ''.join(arr[i])
    return arr