class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        
        for c in tokens:
            match c:
                case "+":
                    numStack.append(numStack.pop() + numStack.pop())
                case "-":
                    b, a = numStack.pop(), numStack.pop()
                    numStack.append(a - b)
                case "*":
                    numStack.append(numStack.pop() * numStack.pop())
                case "/":
                    b, a = numStack.pop(), numStack.pop()
                    numStack.append(int(a / b))
                case _: 
                    numStack.append(int(c))
        return numStack[0]


