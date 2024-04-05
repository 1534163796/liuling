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

