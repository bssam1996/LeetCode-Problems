"""
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}
        for element in tokens:
            if element not in operands:
                stack.append(int(element))
            else:
                second_number = stack.pop()
                first_number = stack.pop()
                if element == "+":
                    stack.append(first_number + second_number)
                elif element == "-":
                    stack.append(first_number - second_number)
                elif element == "*":
                    stack.append(first_number * second_number)
                else:
                    stack.append(int(first_number / second_number))
        return stack.pop()