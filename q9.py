"""
标题：图书管理系统 | 时间限制：1秒 | 内存限制：65536K | 语言限制： 不限
【图书管理系统】
每个用户借阅卡初始充值金额为300元。
1、借阅图书的租金扣除规则
价格大于等于100元的图书，累计借出天数小于等于15天时每本每天租金为5元；累计借出天数大于15天时，大于15天的时间每本每天租金3元。
价格大于等于50元小于100元的图书，累计借出天数小于等于15天时每本每天租金3元，累计借出天数大于15时，大于15天的时间每本每天租金2天；
价格小于50元的每天租金1元。
2、余额少于当前所借书的价格时不能借当前的书，但可以继续借阅其他更便宜的书。
3、需要考虑借书期间图书累计借出天数变化导致的租金变化（比如原价为120元图书，预借天数为25，那么前15天租金为5元，后10天为3元，借书时扣除租金
为105元）。扣除的租金最大不超过当前所借书的价格。
4、借书时需要说明预借天数，超期还书时，每超期一天，额外扣除1元。
处理完用户借阅记录后，求出卡内余额？
输入描述：
每一行为一条借阅记录
图书价格,预借天数,还书时的实际天数
图书价格,预借天数,还书时的实际天数之间用半角的逗号分隔。不考虑格式错误。
输出描述：
对于每组测试数据，输出一行一个整数，表示卡内余额。
示例1：
输入
120,10,10
80,10,3
30,10,12

输出

227
"""


class BookCost(object):

    def __init__(self, book_price, days_num, real_days_num):
        self.book_price = book_price
        self.days_num = days_num
        self.real_days_num = real_days_num

    def count_price(self):
        if self.book_price >= 100:
            return self.exceedt_time(frist_price=5, second_prce=3, split_day=15)
        elif 50 <= self.book_price < 100:
            return self.exceedt_time(frist_price=3, second_prce=2, split_day=15)
        elif 0 <= self.book_price < 50:
            return self.exceedt_time(frist_price=1, second_prce=1, split_day=0)

    def exceedt_time(self, frist_price, second_prce, split_day):
        if self.real_days_num > split_day:
            price = frist_price * split_day + second_prce * (self.real_days_num - split_day)
        else:
            price = frist_price * self.real_days_num
        if self.days_num < self.real_days_num:
            price += self.real_days_num - self.days_num
        return price


def main():
    input_info = """120,10,10
80,10,3
30,10,12"""
    recodes = input_info.strip().split('\n')
    cost = 0
    init = 300
    for recode in recodes:
        book_price, days_num, real_days_num = map(int, recode.strip().split(','))
        bc = BookCost(book_price, days_num, real_days_num)
        each_book_price = bc.count_price()
        cost += each_book_price
    balance = init - cost
    print(balance)


if __name__ == '__main__':
    main()
