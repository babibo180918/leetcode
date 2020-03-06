class Solution(object):
    ids = []

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        total = 0
        union_count = 0
        rows = len(grid)
        if rows == 0: return 0
        cols = len(grid[0])
        if cols == 0: return 0
        self.ids = [-1 for i in range(cols * rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    total += 1
                    cur_root = self.root(i * cols + j)
                    if j < cols - 1 and grid[i][j + 1] == '1':
                        if self.union(i * cols + j, i * cols + j + 1):
                            union_count += 1
                    if i < rows - 1 and grid[i + 1][j] == '1':
                        if self.union(i * cols + j, (i + 1) * cols + j):
                            union_count += 1

        return total - union_count

    def root(self, index):
        while self.ids[index] != -1:
            index = self.ids[index]
        return index

    def union(self, from_idx, to_idx):
        root_to = self.root(to_idx)
        root_from = self.root(from_idx)
        if root_to != root_from:
            self.ids[root_to] = root_from 
            return True
        return False


sol = Solution()
lst = [['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']]
print(sol.numIslands(lst) == 1)


lst = [['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']]
print(sol.numIslands(lst) == 3)

lst = [['1'],
        ['1']]
print(sol.numIslands(lst) == 1)

lst = [['1'],
        ['0'],
        ['1']]
print(sol.numIslands(lst) == 2)

lst = []
print(sol.numIslands(lst) == 0)

lst = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(sol.numIslands(lst) == 1)
