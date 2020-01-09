class State(object):

    G = 0
    P = 0
    group = []
    profit = []

    def __init__(self, index, curgroup, curprofit, remainGroup, remainProfit):
        self.index = index
        self.curgroup = curgroup 
        self.curprofit = curprofit 
        self.remainGroup = remainGroup 
        self.remainProfit = remainProfit

    def checkFeasible(self):
        return self.curgroup <= State.G and self.curprofit >= State.P

    def countFeasibleState(self):
        if self.index == len(State.group):
            return (self.checkFeasible() and 1) or 0
        elif self.curgroup > State.G:
            return 0
        elif self.curprofit + self.remainProfit < State.P:
            return 0
        elif self.curprofit >= State.P and self.curgroup + self.remainGroup <= State.G:
            """print('cutoff index={}'.format(self.index))"""
            return 2 ** (len(State.group) - self.index)
        else:
            nodeGroup = State.group[self.index]
            nodeProfit = State.profit[self.index]
            leftState = State(self.index + 1, self.curgroup, self.curprofit, self.remainGroup - nodeGroup, self.remainProfit - nodeProfit)
            rightState = State(self.index + 1, self.curgroup + nodeGroup, self.curprofit + nodeProfit, self.remainGroup - nodeGroup, self.remainProfit - nodeProfit)
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
        if len(set(group)) > len(set(profit)):
            profit = [x for _,x in sorted(zip(group, profit), reverse=True)]
            group = sorted(group, reverse=True)
        else:
            group = [x for _,x in sorted(zip(profit, group), reverse=True)]
            profit = sorted(profit, reverse=True)

        print(group)
        print(profit)
        State.G = G
        State.P = P
        State.group = group
        State.profit = profit
        state = State(0, 0, 0, sum(group), sum(profit))
        return state.countFeasibleState()

sol = Solution()
a = sol.profitableSchemes(5, 3, [2,2], [2,3])
print(a)

sol = Solution()
a = sol.profitableSchemes(10, 5, [2,3,5], [6,7,8])
print(a)

sol = Solution()
a = sol.profitableSchemes(1, 10, [2,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,2,2,2,1,1,2,1,2,2,2,1,2,1,2,1,2,1,1,2,2,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,2,2,2,2,1,1,1,2,1,2,2,2,1,1,1,1,2,1,2,1,2,1,1,2,2,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,2,2], [1,2,5,6,3,0,4,11,3,6,2,6,5,8,2,3,11,3,0,10,10,6,3,0,5,3,6,6,10,2,5,11,2,1,6,9,1,3,10,3,6,8,9,10,6,6,11,0,10,11,2,9,5,0,11,3,1,7,8,5,3,11,1,1,2,8,11,8,5,10,5,8,0,2,9,6,0,0,5,1,5,9,4,10,3,5,7,2,2,4,1,7,10,5,3,9,9,2,4,3])
print(a)

sol = Solution()
a = sol.profitableSchemes(100, 1, [60,36,37,80,66,96,61,14,43,18,35,98,38,49,66,83,90,60,80,88,14,44,65,78,31,55,79,46,1,90,74,53,62,68,24,37,73,56,37,48,86,51,56,66,51,72,29,34,96,57,84,13,99,69,47,45,55,58,31,60,94,9,60,72,27,59,95,100,40,98,77,10,62,78,32,100,51,96,52,85,40,61,31,8,20,75,32,78,53,67,22,2,40,29,74,68,2,46,3,93], [2,2,0,0,2,2,0,1,2,2,2,2,2,1,0,0,2,1,2,0,1,1,2,2,0,0,2,0,2,0,1,1,0,0,0,1,2,2,0,2,2,1,0,1,2,0,1,0,2,1,2,2,2,0,1,1,0,0,0,2,1,2,1,0,2,1,1,1,0,1,1,2,2,0,1,1,1,1,1,0,1,0,1,2,0,0,1,2,1,1,0,1,2,2,1,1,0,0,0,1])
print(a)

sol = Solution()
a = sol.profitableSchemes(10, 100, [8,8,7,4,3,1,1,6,11,3,1,7,6,9,9,1,8,9,3,10,10,8,7,6,9,10,6,2,2,6,9,7,5,6,2,1,2,10,11,6,8,9,9,8,11,6,2,2,4,5,1,2,1,11,3,2,11,7,11,4,5,7,6,9,6,7,10,10,9,10,10,8,8,6,9,8,5,1,2,5,10,1,4,2,1,5,1,3,6,6,10,6,2,3,2,1,9,6,6,4], [23,36,94,35,73,7,65,25,22,4,62,62,12,18,89,62,2,66,85,94,73,31,56,95,71,91,53,75,100,47,68,4,64,52,97,8,52,32,98,64,2,64,33,21,52,44,41,50,59,40,48,47,39,9,100,1,43,94,63,23,21,92,36,69,100,8,75,16,79,98,72,83,70,11,3,41,91,18,17,76,71,58,71,62,34,49,58,59,90,84,12,43,27,60,47,89,31,14,11,15])
print(a)
