base_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
}

def parse_int_less_100(string):
    if '-' in string:
        splitted_string = string.split('-')
        return base_number[splitted_string[0]] + base_number[splitted_string[1]]
    return base_number[string]

def parse_int_less_1000(string):
    hundred_pos = string.index('hundred') if 'hundred' in string else -1
    result = 0
    if hundred_pos != -1:
        result += parse_int_less_100(string[:hundred_pos-1]) * 100
    base_string = string[hundred_pos+8:] if hundred_pos != -1 else string
    base_string = base_string.replace('and ', '')
    if base_string:
        result += parse_int_less_100(base_string)

    return result

def parse_int(string):
    if string == 'zero':
        return 0
    if string == 'one million':
        return 1000000
    result = 0

    thousand_pos = string.index('thousand') if 'thousand' in string else -1
    if thousand_pos != -1:
        result += parse_int_less_1000(string[:thousand_pos-1]) * 1000

    base_string = string[thousand_pos+9:] if thousand_pos != -1 else string
    if base_string:
        result += parse_int_less_1000(base_string)

    return result


print(parse_int("one hundred"))
# print(parse_int("twenty"))
# print(parse_int("two hundred forty-six"))
# print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))