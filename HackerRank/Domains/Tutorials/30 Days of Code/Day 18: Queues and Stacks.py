class Solution:
    # Write your code here
    def __init__(self):
        self.stack = ''
        self.queue = ''
        
    def pushCharacter(self, ch):
        self.stack += ch
        
    def enqueueCharacter(self, ch):
        self.queue += ch
        
    def popCharacter(self):
        temp = self.stack[-1]
        self.stack = self.stack[:-1]
        return temp
        
    def dequeueCharacter(self):
        temp  =self.queue[0]
        self.queue = self.queue[1:]
        return temp
