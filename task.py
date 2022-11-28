def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    reverseStringRecursion(s, 0);


def reverseStringRecursion(s, position):
    s_length = len(s)
    if position >= (s_length // 2):
        return

    s[position], s[s_length - position - 1] = s[s_length - position - 1], s[position]
    reverseStringRecursion(s, position + 1)

arr = [1,2,3,4,5]
reverseString(arr);
print(arr)
