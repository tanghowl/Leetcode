"""
标题：多道批处理调度 | 时间限制：1秒 | 内存限制：32768K | 语言限制： 不限
【多道批处理调度】某多处理器多道批处理系统一次允许将所有作业调入内存，且能并行执行，其并行数等于处理器个数。该系统采用SJF的调度方式（最短作业优
先，系统在调度时，总是优先调度执行处理时间最短的作业）。
现给定处理器个数m，作业数n, 每个作业的处理时间分别为t1,t2…tn。
当n>m时，首先处理时间短的m个作业进入处理器处理，其他的进入等待，当某个作业处理完成时，依次从等待队列中取处理时间最短的作业进入处理。
求系统处理完所有作业的耗时为多少？
注：不考虑作业切换的消耗。
输入描述：
输入2行，第一行为2个整数（采用空格分隔），分别表示处理器个数m和作业数n；第二行输入n个整数（采用空格分隔），表示每个作业的处理时长t1,t2…tn。0<
m,n<100，0<t1,t2…tn<100。
注：不用考虑输入合法性。
输出描述：
输出处理总时长
示例1：
输入
3 5
8 4 3 1 10

输出
13

------
"""


class SJF(object):
    def __init__(self, cpu_num: int, work_num: int, job_lst: list):
        self.cpu_num = cpu_num
        self.work_num = len(job_lst)
        self.sort_job_lst = sorted(job_lst)

    def count_time(self):
        all_time = 0

        if self.cpu_num >= self.work_num:
            all_time = max(self.sort_job_lst)
        else:
            queue = self.sort_job_lst[:3]
            for n, each_job_time in enumerate(self.sort_job_lst[3:], 4):
                if n == self.work_num:
                    min_job_time = min(queue)
                    all_time += min_job_time
                    all_time += each_job_time
                else:
                    min_job_time = min(queue)
                    queue = [e - min_job_time for e in queue]
                    min_job_idx = queue.index(0)
                    queue[min_job_idx] = each_job_time
                    all_time += min_job_time
        return all_time


def main():
    cpu_num = 3
    work_num = 11
    job_lst = [5, 5, 5, 5, 5, 6, 6, 6, 7, 8, 9]
    sjf = SJF(cpu_num, work_num, job_lst)
    print(sjf.count_time())


if __name__ == '__main__':
    main()
