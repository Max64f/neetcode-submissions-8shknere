class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        actions = {"+", "-", "*", "/"}
        for char in tokens:
            if char not in actions: #Значит это цифра
                stack.append(char)
            else:
                SecondOperator = int(stack.pop())
                FirstOperator = int(stack.pop())
                if char == "+":
                    stack.append(FirstOperator + SecondOperator)
                elif char == "-":
                    stack.append(FirstOperator - SecondOperator)
                elif char == "*":
                    stack.append(FirstOperator * SecondOperator)
                elif char == "/":
                    stack.append(int(FirstOperator / SecondOperator))
        return int(stack.pop())