"""
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


def letterCombinations(digits):
    all_digits = {
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"],
    }
    digits_length = len(digits)
    if digits_length == 0:
        return []
    if digits_length == 1:
        return all_digits[digits]
    output = []
    from itertools import product
    all_lists = [all_digits[digit] for digit in digits]
    product_output = list(product(*all_lists))
    for element in product_output:
        element = "".join(element)
        output.append(element)
    return output


def test_cases():
    list_of_cases = [
        {
            "s": "23",
            "o": ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        },
        {
            "s": "",
            "o": []
        },
        {
            "s": "2",
            "o": ["a","b","c"]
        },
        {
            "s": "2",
            "o": ["a", "b", "c"]
        },
    ]
    for case in range(len(list_of_cases)):
        output = letterCombinations(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


# print(countVowelStrings(7))
test_cases()
