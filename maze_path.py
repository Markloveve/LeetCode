'''
Description
You are trapped in a chessboard designed by a god, and now you must find your way out.
The chessboard consists of n⇥n squares. The god has placed exactly k pieces (obstacles) on k (k  10)
distinct squares. You cannot pass through these squares, but all other squares are accessible.
You start at the top-left corner of the chessboard at position (1, 1), and your goal is to reach the
bottom-right corner at (n, n). You can only move one square down or one square to the right at a time
(no diagonal moves or moves upward or leftward).
To escape, you must answer the god’s challenge: How many distinct paths can you take from (1, 1) to
(n, n) without passing through any obstacle? Since the result may be large, return it modulo 998244353.
Input Format
The first line contains two integers n and k, representing the size of the chessboard and the number of
obstacles, respectively.
The next k lines contain two integers x and y, representing the coordinates of each obstacle.
Output Format
Output one integer, representing the number of valid paths modulo 998244353.
Sample Input 1
3 1
2 2
Sample Output 1
2
Sample Input 2
7 3
1 4
5 3
3 6
Sample Output 2
540
'''

from itertools import combinations

MOD = 998244353

# 计算组合数 从n里面选k个
def comb(n, k):
    if k > n or k < 0:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (n - i) % MOD
        denominator = denominator * (i + 1) % MOD
    return numerator * pow(denominator, MOD - 2, MOD) % MOD

# 从一个障碍到另一个障碍的路径数，都需要补进总路径数，因为减多了
def paths_from_obstacle_to_another_obstacle(x1, y1, x2, y2):
    return comb(x2 + y2 - x1 - y1, x2 - x1)

# 从起点到该障碍的路径数目
def paths_to_obstacle(x1, y1):
    return comb(x1 + y1, x1)

# 从该障碍到终点的路径数目
def paths_from_obstacle(n, x1, y1):
    return comb(2 * (n - 1) - (x1 + y1), n - x1 - 1)

# 所有路径情况
def all_paths(n):
    return comb(2 * (n - 1), n - 1)

# 示例计算
n = 7
obstacles = [(1, 4), (5, 3), (3, 6)]

all_paths_num = all_paths(n)
accessible_path = all_paths_num

# 减去通过每个障碍的路径数
for x, y in obstacles:
    to_obstacle = paths_to_obstacle(x - 1, y - 1)
    from_obstacle = paths_from_obstacle(n, x - 1, y - 1)
    accessible_path = (accessible_path - to_obstacle * from_obstacle % MOD + MOD) % MOD

# 补上从一个障碍到另一个障碍的路径数
for (x1, y1), (x2, y2) in combinations(obstacles, 2):
    if x1 <= x2 and y1 <= y2:
        obstacle_to_another = paths_from_obstacle_to_another_obstacle(x1 - 1, y1 - 1, x2 - 1, y2 - 1)
        from_second_obstacle = paths_from_obstacle(n, x2 - 1, y2 - 1)
        accessible_path = (accessible_path + paths_to_obstacle(x1 - 1, y1 - 1) * obstacle_to_another % MOD * from_second_obstacle % MOD) % MOD

print(f"All Paths: {all_paths(n)}")
print(f"Accessible Path: {accessible_path}")