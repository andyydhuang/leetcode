class Solution:   
    def evalRPN(self, tokens: List[str]) -> int:
        def isNumber(s:str) -> bool:
            if s.isdigit():
                return True
            return s.lstrip('-').isdigit()

        def mathFunc(stack:List[str], token:str) -> int:
            num2 = stack.pop()
            num1 = stack.pop()

            if token == "+":
                return num1+num2
            elif token == "-":
                return num1-num2
            elif token == "*":
                return num1*num2
            elif token == "/":
                return int(num1/num2)

        stack = []
        for token in tokens:
            if len(stack) < 2:
                stack.append(int(token))
                continue

            if isNumber(token):
                stack.append(int(token))
            else:
                stack.append(mathFunc(stack, token))

        if len(stack) != 1:
            print('Code Error')
            return None
        return stack[0]