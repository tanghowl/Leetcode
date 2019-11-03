"""
题目:
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

思路:
暴力搜索：主要是构建3个不同元素的组合,更改成n个元素...

"""
from typing import List
from copy import deepcopy


def bak():
    """
    运算超时
    :return:
    """

    class Solution:

        def threeSum(self, nums: List[int]) -> List[List[int]]:
            tuple_num = 3
            sort_nums = sorted(nums)
            nums_len = len(sort_nums)
            combination = Combination(nums_len, tuple_num)
            combination()
            idxs_set = combination.ids_set
            result = self.check_sum(idxs_set, sort_nums)
            return [[int(x) for x in i.split()] for i in result]

        def check_sum(self, idxs_set, num):
            result = set()
            for idxs in idxs_set:
                each_num = self.combination_num(idxs, num)
                if sum(each_num) == 0:
                    result.add('\t'.join(map(str, each_num)))
            return result

        @staticmethod
        def combination_num(idxs, num):
            return [int(num[idx]) for idx in idxs]

    class Combination:

        def __init__(self, nums_len, tuple_num):
            self.nums_len = nums_len
            self.tuple_num = tuple_num
            self.idxs_init = [0] * tuple_num
            self.ids_set = []

        def __call__(self, *args, **kwargs):
            self.next_num(0, 0)

        def next_num(self, start, idx_subscript):
            if idx_subscript != self.tuple_num:
                for idx in range(start, self.nums_len):
                    self.idxs_init[idx_subscript] = idx
                    start += 1
                    self.next_num(start, idx_subscript + 1)
            else:
                tmp = deepcopy(self.idxs_init)
                self.ids_set.append(tmp)


"""算法流程：
特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
对数组进行排序。
遍历排序后数组：
若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
对于重复元素：跳过，避免出现重复解
令左指针 L=i+1L=i+1，右指针 R=n-1R=n−1，当 L<RL<R 时，执行循环：
当 nums[i]+nums[L]+nums[R]==0nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
若和大于 00，说明 nums[R]nums[R] 太大，RR 左移
若和小于 00，说明 nums[L]nums[L] 太小，LL 右移
复杂度分析
时间复杂度：O\left(n^{2}\right)O(n 
2
 )，数组排序 O(N \log N)O(NlogN)，遍历数组 O\left(n\right)O(n)，双指针遍历 O\left(n\right)O(n)，总体 O(N \log N)+O\left(n\right)*O\left(n\right)O(NlogN)+O(n)∗O(n)，O\left(n^{2}\right)O(n 
2
 )
空间复杂度：O(1)O(1)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        if (not nums) or (n < 3):
            return []
        sort_nums = sorted(nums)
        res = []
        for i in range(n):
            if sort_nums[i] > 0:
                return res
            if i > 0 and sort_nums[i] == sort_nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                if sort_nums[i] + sort_nums[left] + sort_nums[right] == 0:
                    res.append([sort_nums[i], sort_nums[left], sort_nums[right]])
                    while (left < right) and (sort_nums[left] == sort_nums[left + 1]):
                        left = left + 1
                    while (left < right) and (sort_nums[right] == sort_nums[right - 1]):
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif (sort_nums[i] + sort_nums[left] + sort_nums[right]) > 0:
                    right = right - 1
                else:
                    left = left + 1
        return res


if __name__ == '__main__':
    nums = [0, 7, -4, -7, 0, 14, -6, -4, -12, 11, 4, 9, 7, 4, -10, 8, 10, 5, 4, 14, 6, 0, -9, 5, 6, 6, -11, 1, -8, -1,
            2, -1, 13, 5, -1, -2, 4, 9, 9, -1, -3, -1, -7, 11, 10, -2, -4, 5, 10, -15, -4, -6, -8, 2, 14, 13, -7, 11,
            -9, -8, -13, 0, -1, -15, -10, 13, -2, 1, -1, -15, 7, 3, -9, 7, -1, -14, -10, 2, 6, 8, -6, -12, -13, 1, -3,
            8, -9, -2, 4, -2, -3, 6, 5, 11, 6, 11, 10, 12, -11, -14]
    t = Solution().threeSum(nums)
    print(t)
