'''
Link: https://leetcode.com/problems/roman-to-integer/
'''


def romanToInt(s):
    # Method 2 - Runtime 55 ms, Memory 13.9 MB
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total_sum = 0
    character = 0
    previous_value = 1000
    while character < len(s):
        current_value = roman_numbers[s[character]]
        if current_value <= previous_value:
            total_sum += current_value
        else:
            total_sum -= previous_value
            total_sum += current_value - previous_value
        previous_value = current_value
        character += 1
    return total_sum


def romanToInt2(s):
    # Method 1 - Runtime 85 ms, Memory 13.9 MB
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total_sum = 0
    character = 0
    while character < len(s):
        if character == (len(s)-1):
            total_sum += roman_numbers[s[character]]
            break
        if s[character] == "I":
            if s[character+1] == "V":
                total_sum += 4
                character += 2
            elif s[character+1] == "X":
                total_sum += 9
                character += 2
            else:
                total_sum += 1
                character += 1
        elif s[character] == "X":
            if s[character+1] == "L":
                total_sum += 40
                character += 2
            elif s[character+1] == "C":
                total_sum += 90
                character += 2
            else:
                total_sum += 10
                character += 1
        elif s[character] == "C":
            if s[character+1] == "D":
                total_sum += 400
                character += 2
            elif s[character+1] == "M":
                total_sum += 900
                character += 2
            else:
                total_sum += 100
                character += 1
        else:
            total_sum += roman_numbers[s[character]]
            character += 1
    return total_sum


def test_cases():
    list_of_cases = [
        {"s": "III",
         "o": 3},
        {"s": "LVIII",
         "o": 58},
        {"s": "MCMXCIV",
         "o": 1994},
    ]
    for case in range(len(list_of_cases)):
        output = romanToInt(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()