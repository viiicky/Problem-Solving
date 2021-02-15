class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        start = 0
        answer = ''
        stack.append(S[0])

        for i in range(1, len(S)):
            if S[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(S[i])

            if not stack:
                answer += S[start + 1:i]
                start = i + 1

        return answer
