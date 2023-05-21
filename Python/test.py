class Solution:    
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(b // a)
            else:
                stack.append(int(c))

        return stack[0]
        
s = Solution()
print(s.evalRPN(["2","1","+", "3", "*"]))