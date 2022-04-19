'''
Link: https://leetcode.com/problems/valid-parentheses/
'''


def isValid(s):
    # Method 2 - Runtime 53 ms, Memory 13.8 MB
    list_of_character = []  # Like stack
    for character in range(0, len(s)):
        current_character = s[character]
        if current_character == "(" or current_character == "{" or current_character == "[":
            list_of_character.append(current_character)
            continue
        if len(list_of_character) == 0:
            return False
        ascii_number = ord(current_character)
        previous_character = ord(list_of_character.pop())
        subtraction = ascii_number - previous_character
        if subtraction != 1 and subtraction != 2:
            return False
    if len(list_of_character) == 0:
        return True
    return False


def isValid2(s):
    # Method 1 - Runtime 38 ms, Memory 13.8 MB
    list_of_character = [s[0]]
    for character in range(1, len(s)):
        current_character = s[character]
        if current_character == "}":
            if len(list_of_character) == 0:
                return False
            previous_character = list_of_character.pop()
            if previous_character != "{":
                return False
            continue
        if current_character == "]":
            if len(list_of_character) == 0:
                return False
            previous_character = list_of_character.pop()
            if previous_character != "[":
                return False
            continue
        if current_character == ")":
            if len(list_of_character) == 0:
                return False
            previous_character = list_of_character.pop()
            if previous_character != "(":
                return False
            continue
        list_of_character.append(current_character)
    if len(list_of_character) == 0:
        return True
    return False


def test_cases():
    list_of_cases = [
        {
            "s": "()",
            "o": True
        },
        {
            "s": "()[]{}",
            "o": True
        },
        {
            "s": "(]",
            "o": False
        },
        {
            "s": "(){}}{",
            "o": False
        }
    ]
    for case in range(len(list_of_cases)):
        output = isValid(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()
# ord("(")  # 40
# ord(")")  # 41
# ord("{")  # 123
# ord("}")  # 125
# ord("[")  # 91
# ord("]")  # 93
