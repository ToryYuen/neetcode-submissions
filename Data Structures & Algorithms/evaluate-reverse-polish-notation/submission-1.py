class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t == '+':
                num2 = s.pop()
                num1 = s.pop()
                s.append(num1 + num2)
            elif t == '-':
                num2 = s.pop()
                num1 = s.pop()
                s.append(num1 - num2)
            elif t == '*':
                num2 = s.pop()
                num1 = s.pop()
                s.append(num1 * num2)
            elif t == '/':
                num2 = s.pop()
                num1 = s.pop()
                s.append(int(num1 / num2))
            else:
                s.append(int(t))
        return s.pop()   
 