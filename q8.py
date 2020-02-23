"""
标题：猴子吃桃 | 时间限制：1秒 | 内存限制：65536K | 语言限制： 不限
【猴子吃桃】孙悟空喜欢吃蟠桃，一天他乘守卫蟠桃园的天兵天将离开了而偷偷的来到王母娘娘的蟠桃园偷吃蟠桃。已知蟠桃园有N棵蟠桃树，第i棵蟠桃树上有 N[i]
（大于0）个蟠桃，天兵天将将在H（不小于蟠桃树棵数）小时后回来。孙悟空可以决定他吃蟠桃的速度K（单位：个/小时），每个小时他会选则一颗蟠桃树，从中
吃掉K个蟠桃，如果这棵树上的蟠桃数小于K，他将吃掉这棵树上所有蟠桃，然后这一小时内不再吃其余蟠桃树上的蟠桃。孙悟空喜欢慢慢吃，但仍想在天兵天将回
来前将所有蟠桃吃完。求孙悟空可以在H小时内吃掉所有蟠桃的最小速度K（K为整数）。
输入描述：

从标准输入中读取一行数字，前面数字表示每棵数上蟠桃个数，最后的数字表示天兵天将将离开的时间。

输出描述：

吃掉所有蟠桃的最小速度K（K为整数）或输入异常时输出-1。
示例1：
输入
3 11 6 7 8
输出
4
"""

from math import ceil


class Solution(object):
    def __init__(self, n_lst: list):
        *self.peach_nums, self.leave_time = n_lst

    def get_min_speed(self):
        min_peach_num = min(self.peach_nums)
        max_peach_num = max(self.peach_nums)

        for speed in range(min_peach_num, max_peach_num + 1):
            all_time = sum(ceil(peach_num / speed) for peach_num in self.peach_nums)
            if all_time <= self.leave_time:
                return speed


def main():
    imput_info = '3 11 6 7 8'
    lst = list(map(int, imput_info.strip().split()))
    s = Solution(lst)
    speed = s.get_min_speed()
    print(speed)


if __name__ == '__main__':
    main()
