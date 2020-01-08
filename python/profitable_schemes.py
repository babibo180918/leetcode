class State(object):

    G = 0
    P = 0
    group = []
    profit = []

    def __init__(self, index, curgroup, curprofit):
        self.index = index
        self.curgroup = curgroup 
        self.curprofit = curprofit 

    def checkFeasible(self):
        return self.curgroup <= State.G and self.curprofit >= State.P

    def countFeasibleState(self):
        if self.index == len(State.group):
            return (self.checkFeasible() and 1) or 0
        elif self.curgroup > State.G:
            return 0
        else:
            leftState = State(self.index + 1, self.curgroup, self.curprofit)
            rightState = State(self.index + 1, self.curgroup + State.group[self.index], self.curprofit + State.profit[self.index])
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
        State.G = G
        State.P = P
        State.group = group
        State.profit = profit
        state = State(0, 0, 0)
        return state.countFeasibleState()

sol = Solution()
a = sol.profitableSchemes(5, 3, [2,2], [2,3])
print(a)

sol = Solution()
a = sol.profitableSchemes(10, 5, [2,3,5], [6,7,8])
print(a)



