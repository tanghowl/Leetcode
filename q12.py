"""
标题：在字符串中找出连续最长的数字串 | 时间限制：1秒 | 内存限制：65536K | 语言限制： 不限
【在字符串中找出连续最长的数字串】请在一个字符串中找出连续最长的数字串，并返回这个数字串；如果存在长度相同的连续数字串，返回最后一个。
注意：数字串是由数字和“.”组成的（长度包括“.”在内），“.”的两边必须是数字，比如：
数字串“1234”的长度小于数字串“00055”；数字串“1234.56789”的长度大于数字串“123456789”
输入描述：
字符串输入为ASCII编码，长度不定，可能含有空格，请读取完整一行数据作为输入

输出描述：

如果没有符合条件的数字串，返回空字符串""
示例1：
输入

abcd123.4567.890.123

输出

4567.890
"""
import re


def get_max_num(strs):
    split_pat = re.compile(r'[^0-9.]+')
    num_lst = split_pat.split(strs)
    max_num = ''
    for num_pat in num_lst:
        if r'.' in num_pat:
            each_num_lst = [e for e in num_pat.strip('.').split('.')]
            for n in range(len(each_num_lst) - 1):
                integer = each_num_lst[n]
                fractional = each_num_lst[n + 1]
                num = f'{integer}.{fractional}'
                max_num = judge(max_num, num)
        else:
            max_num = judge(max_num, num_pat)
    return max_num


def judge(max_num, num):
    max_len = len(max_num)
    num_len = len(num)
    if num_len >= max_len:
        max_num = num
    return max_num


def main():
    strs = '1asdf123456780abcd.123.4567.89012345.123.'
    result = get_max_num(strs)
    print(result)


if __name__ == '__main__':
    main()
