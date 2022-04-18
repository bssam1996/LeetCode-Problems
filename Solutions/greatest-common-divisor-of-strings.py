'''
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
'''


def gcdOfStrings2(str1, str2):
    # Method 2 - Runtime 34 ms, Memory 13.9 MB
    if len(str1) < len(str2):
        shorter_string = str1
        longer_string = str2
    else:
        shorter_string = str2
        longer_string = str1
    list_of_possibilities = [1]
    for counter in range(2, int(len(shorter_string) / 2) + 1):
        if len(shorter_string) % counter == 0:
            list_of_possibilities.append(counter)
    list_of_possibilities.append(len(shorter_string))
    gcd = 0
    for value in list_of_possibilities[-1::-1]:
        if len(longer_string) % value == 0:
            gcd = value
            break
    if gcd != 0:
        partial_string = shorter_string[:gcd]
        number_of_times_longer = int(len(longer_string) / len(partial_string))
        number_of_times_shorter = int(len(shorter_string) / len(partial_string))
        if longer_string != (partial_string * number_of_times_longer) or shorter_string != (partial_string * number_of_times_shorter):
            return ""
    return shorter_string[:gcd]


def gcdOfStrings(str1, str2):
    # Method 1 - Runtime 144 ms, Memory 13.9 MB
    if len(str1) < len(str2):
        shorter_string = str1
        longer_string = str2
    else:
        shorter_string = str2
        longer_string = str1
    concatenated_string = ""
    final_string = ""
    for character in shorter_string:
        concatenated_string += character
        temp_short_string = shorter_string.replace(concatenated_string, "")
        temp_long_string = longer_string.replace(concatenated_string, "")
        if len(temp_short_string) == 0 and len(temp_long_string) == 0:
            final_string = concatenated_string
    return final_string


def test_cases():
    list_of_tests = [
        {
            "str1": "ABCABC",
            "str2": "ABC",
            "O": "ABC"
        },
        {
            "str1": "ABABAB",
            "str2": "ABAB",
            "O": "AB"
        },
        {
            "str1": "ABABABAB",
            "str2": "ABAB",
            "O": "ABAB"
        },
        {
            "str1": "LEET",
            "str2": "CODE",
            "O": ""
        },
        {
            "str1": "TAUXXTAUXXTAUXXTAUXXTAUXX",
            "str2": "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX",
            "O": "TAUXX"
        },
        {
            "str1": "ABCDEF",
            "str2": "ABC",
            "O": ""
        },
        {
            "str1": "CXTXNCXTXNCXTXNCXTXNCXTXN",
            "str2": "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN",
            "O": "CXTXN"
        },
        {
            "str1": "AAAAAAAAA",
            "str2": "AAACCC",
            "O": ""
        },
    ]
    for case in range(len(list_of_tests)):
        expected_output = list_of_tests[case]["O"]
        actual_output = gcdOfStrings2(list_of_tests[case]["str1"], list_of_tests[case]["str2"])
        print("#", str(case), str(expected_output == actual_output))
        if expected_output != actual_output:
            print("Expected Output",expected_output)
            print("Actual Output",actual_output)


test_cases()
