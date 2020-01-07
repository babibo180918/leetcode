class State(object):

    def __init__(self, G, P, group, profit):
        self.G = G
        self.P = P
        self.group = group
        self.profit = profit 
        self.curgroup = 0
        self.curprofit = 0

    def addCrime(self, groupsize, profit):
        self.curgroup += groupsize
        self.curprofit += profit

    def checkFeasible(self):
        return self.curgroup <= self.G and self.curprofit >= self.P

    def countFeasibleState(self):
        if len(self.group) == 0:
            return (self.checkFeasible() and 1) or 0
        else:
            leftState = State(self.G, self.P, self.group[1:], self.profit[1:])
            leftState.curgroup = self.curgroup
            leftState.curprofit = self.curprofit
            rightState = State(self.G, self.P, self.group[1:], self.profit[1:])
            rightState.curgroup = self.curgroup + self.group[0]
            rightState.curprofit = self.curprofit + self.profit[0]
            return leftState.countFeasibleState() + rightState.countFeasibleState()

class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        state = State(G, P, group, profit)
        return state.countFeasibleState()

sol = Solution()
a = sol.profitableSchemes(5, 3, [2,2], [2,3])
print(a)

sol = Solution()
a = sol.profitableSchemes(10, 5, [2,3,5], [6,7,8])
print(a)



