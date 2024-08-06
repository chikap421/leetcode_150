# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def is_uniform(grid, x1, y1, x2, y2):
            val = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != val:
                        return False
            return True

        def construct_quad(grid, x1, y1, x2, y2):
            if is_uniform(grid, x1, y1, x2, y2):
                return Node(val=bool(grid[x1][y1]), isLeaf=True)
            
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            
            topLeft = construct_quad(grid, x1, y1, mid_x, mid_y)
            topRight = construct_quad(grid, x1, mid_y, mid_x, y2)
            bottomLeft = construct_quad(grid, mid_x, y1, x2, mid_y)
            bottomRight = construct_quad(grid, mid_x, mid_y, x2, y2)
            
            return Node(
                val=True,  # This value can be anything as it's not used when isLeaf is False
                isLeaf=False,
                topLeft=topLeft,
                topRight=topRight,
                bottomLeft=bottomLeft,
                bottomRight=bottomRight
            )

        return construct_quad(grid, 0, 0, len(grid), len(grid[0]))

