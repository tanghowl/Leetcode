"""集五福作为近年来大家喜闻乐见迎新春活动，集合爱国福、富强福、和谐福、友善福、敬业福即可分享超大红包
题目：以0和1组成的长度为5的字符串代表每个人所得到的福卡，每一位代表一种福卡，1表示已经获得该福卡，单类型福卡不超过1张，随机抽取一个小于10人团队，求该团队最多可以
集齐多少套五福
"""

import numpy
import random


def max_all(team_card: list, sample: int):
    matrix = check_info(team_card, sample)
    matrix = numpy.asarray(matrix)
    return min(matrix.sum(axis=0))


def check_info(team_card, sample):
    matrix = []
    if sample >= 10:
        raise Exception('sample num si greater than 10 ')
    samples = random.sample(team_card, sample)
    for each in samples:
        each = each.strip()
        if len(each) != 5:
            raise Exception('the card species num is ERROR')
        tmp_sample = []
        for e in each:
            if e not in {'0', '1'}:
                raise Exception('the card is not 1 or 0')
            else:
                tmp_sample.append(int(e))
        matrix.append(tmp_sample)
    return matrix


def main():
    team_card = ['11010', '10101', '11000', '01110', '00011', '00000']
    sample = 5
    a = max_all(team_card, sample)
    print(a)


if __name__ == '__main__':
    main()
