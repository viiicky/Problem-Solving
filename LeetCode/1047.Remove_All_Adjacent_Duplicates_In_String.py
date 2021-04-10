class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [S[0]]

        for letter in S[1:]:
            if len(stack) > 0 and letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)

        return ''.join(stack)
