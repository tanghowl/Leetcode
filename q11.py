"""
标题：优先级队列 | 时间限制：1秒 | 内存限制：32768K | 语言限制： 不限
【优先级队列】
输入一组字符串,其中英文逗号作为分割作为队列的输入,分割后的每个字符串的最后一位字符为队列入栈的优先级,优先级是ascii码越大优先级越高, 请按照优先级从
高到低输出出栈的字符串,同样以英文逗号作为分割。如优先级相同入栈顺序即为出栈顺序.
输入描述：
一个长度不超过100的字符串
输出描述：
按照优先级输出出栈的字符串,
以英文逗号作为分割
示例1：
输入

A1,B2,C3,a9,d0
输出

a9,C3,B2,A1,d0
"""
from collections import defaultdict


def main():
    input_info = 'A1,B2,C3,a9,d0'
    lst = input_info.strip().split(',')
    ascii_set = defaultdict(list)
    for e in lst:
        ascii_k = ord(e[-1])
        ascii_set[ascii_k].append(e)

    new_lst = [','.join(ascii_set.get(k)) for k in sorted(ascii_set, reverse=True)]
    result = ','.join(new_lst)
    print(result)


if __name__ == '__main__':
    main()
