"""
假定街道是棋盘型的，每格距离相等，车辆通过每格街道需要时间均为 timePerRoad；
街道的街口（交叉点）有交通灯，灯的周期 T（=lights[row][col]）各不相同；
车辆可直行、左转和右转，其中直行和左转需要等相应 T 时间的交通灯才可通行，右转无需等待。
现给出 n * m 个街口的交通灯周期，以及起止街口的坐标，计算车辆经过两个街口的最短时间。
其中：
1.起点和终点的交通灯不计入时间，且可以在任意方向经过街口
2.不可超出 n * m 个街口，不可跳跃，但边线也是道路（即：lights[0][0] -> lights[0][1] 是有效路径）
/**
 * @param lights：n*m个街口每个交通灯的周期，值范围[0, 120]，n和m的范围为[1,9]
 * @param timePreRoad：相邻两个街口之间街道的通行时间，范围为[0,600]
 * @param rowStart：起点的行号
 * @param colStart：起点的列号
 * @param rowEnd：终点的行号
 * @param colEnd：终点的列号
 * @return lights[rowStart][colStart] 与 lights[rowEnd][colEnd] 两个街口之间的最短通行时间
 */
int calcTime(int[][] lights, int timePreRoad, int rowStart, int colStart, int rowEnd, int colEnd)
"""
import heapq

# 定义四个方向的偏移量：上、右、下、左
offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def calc_time(lights, time_per_road, row_start, col_start, row_end, col_end):
    n, m = len(lights), len(lights[0])

    # 初始化距离数组
    dist = [[[float('inf') for _ in range(4)] for _ in range(m)] for _ in range(n)]
    for k in range(4):
        dist[row_start][col_start][k] = 0

    # 使用heapq实现的优先队列
    pq = []
    for k in range(4):
        heapq.heappush(pq, (0, row_start, col_start, -1, -1, k))

    while pq:
        v, x, y, px, py, direction = heapq.heappop(pq)

        for k, (dx, dy) in enumerate(offsets):
            new_x, new_y = x + dx, y + dy

            if not (0 <= new_x < n and 0 <= new_y < m) or (new_x == px and new_y == py):
                continue

            new_cost = v + time_per_road
            if (direction + 1) % 4 != k:  # 如果不是右转
                new_cost += lights[x][y]

            if new_cost < dist[new_x][new_y][k]:
                dist[new_x][new_y][k] = new_cost
                heapq.heappush(pq, (new_cost, new_x, new_y, x, y, k))

    return min(dist[row_end][col_end])


# 读取输入
n, m = map(int, input().split())
lights = [list(map(int, input().split())) for _ in range(n)]
time_per_road = int(input())
row_start, col_start = map(int, input().split())
row_end, col_end = map(int, input().split())

# 计算并输出结果
print(calc_time(lights, time_per_road, row_start, col_start, row_end, col_end))
