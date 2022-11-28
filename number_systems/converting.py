def convertToBase(self, n: int, base: int) -> List[int]:
    result = []
    current_number = n
    
    while current_number != 0:
        if current_number % base == 0:
            result.append(0)
        else:
            value = current_number - (current_number // base) * base
            result.append(value)
        current_number = current_number // base
    return result