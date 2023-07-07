class Solution:
    output = []

    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.gen(0, 0 , [], output, n)
        return output

    def gen(self, left, right, comb, output, n):  
        '''
        print("-----")
        print(f" left:{left}")  
        print(f" right:{right}")
        print(f" comb:{comb}")
        '''  
        if left == n and right == n:
            output.append(''.join(comb))
            return
        elif left == right:
            comb.append("(")
            self.gen(left+1, right, comb, output, n)
            comb.pop()
        else:
            for i in range(2):
                if i == 0 and left < n:
                    comb.append("(")
                    self.gen(left+1, right, comb, output, n)
                    comb.pop()
                elif i == 1 and right < n:
                    comb.append(")")
                    self.gen(left, right+1, comb, output, n)
                    comb.pop()