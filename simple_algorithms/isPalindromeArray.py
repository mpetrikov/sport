def isPalindrome(self, array: List[int]) -> bool:
    middle_value = len(array) // 2
    array_length = len(array)
    for i in range(middle_value + 1):
        if array[i] != array[array_length - i - 1]:
            return False
    return True
