class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        
        for c in tokens:
            if c == '+':
                int1 = numStack.pop()
                int2 = numStack.pop()
                numStack.append(int1 + int2)
            elif c == '-':
                int1 = numStack.pop()
                int2 = numStack.pop()
                numStack.append(int2 - int1)
            elif c == '*':
                int1 = numStack.pop()
                int2 = numStack.pop()
                numStack.append(int1 * int2)
            elif c == '/':
                int1 = numStack.pop()
                int2 = numStack.pop()
                numStack.append(int(int2 / int1))
            else:
                numStack.append(int(c))
        sum = numStack.pop()
        return int(sum)


