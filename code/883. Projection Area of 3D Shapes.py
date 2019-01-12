# coding = utf-8
__author__ = "Yufeng Yang"

"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

 

Example 1:

Input: [[2]]
Output: 5


Example 2:

Input: [[1,2],[3,4]]
Output: 17
"""


def projectionArea(grid):
    """
    :param grid: List[List[int]]
    :return int

    Explanation: the total area of all three projections consists of three parts:
        1) sum(map(max,grid))                       the sum of the max of all rows
        2) sum(map(max,zip(*grid)))                 the sum of the max of all columns
        3) sum(map(len, grid)) if element!=0        the number of squares which have at least one cube

    """
    if not grid:
        return 0
    ans = 0
    for l in grid:
        for num in l:
            if num != 0:
                ans += 1
        ans += max(l)

    for e in zip(*grid):
        ans += max(e)

    return ans


# one-line solution
def projectionArea2(grid):
    """
    :param grid: List[List[int]]
    :return: int
    """

    return sum(map(len, [[row for row in col if row] for col in grid])) + sum(map(max, grid)) + sum(
        map(max, zip(*grid)))

