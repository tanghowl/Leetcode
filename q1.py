"""
考题1：
标题：促销活动 | 时间限制：1秒 | 内存限制：131072K | 语言限制： 不限
【促销活动】系统需要提供人民币(CNY)、美元(USD)、英镑(GBP)、港币(HKD) 价值转换功能。
为了简单处理,题目的说明和考生调试可以用下面的默认汇率：
1 CNY = 2 HKD
1 USD = 8 CNY
1 GBP = 2 USD
请按照汇率实现货币最大兑换和最小兑换功能。
例如：
最大兑换
Currency(1200, CNY) = 75 GBP
Currency(127, HKD) = 3 GBP 1 USD 7 CNY 1 HKD
最小兑换
Currency(20, CNY) = 40 HKD
汇率是实时变化的,但是短期内大致符合当前价值规律,即相同数值的货币,价值满足GBP>USD>CNY>HKD，每组输入数据都会有不同的输入汇率,需要按设置的汇率
进行兑换。
输入描述：
输出描述：
示例1：
输入
输出
他的代码：
空
示例输入如下：2 8 2 127 HKD MAX
⑴第1个数字表示1CNY可以换成多少HKD。
⑵第2个数字表示1USD可以换成多少CNY
⑶第3个数字表示1GBP 可以换成多少USD
⑷第4个和第5个 表示 数量和货币类型(大写)
⑸第6个表示最大兑换(MAX)还是最小兑换(MIN)
⑹需要校验前4个数字必须是大于0的整数。不合法直接返回"ERROR"
⑺货币字母大写简称(HKD、CNY、USD、GBP)、兑换方式字母大写简称(MIN/MAX)需要判断合法性,只有全部字母大写并且内容相同才是合法。
⑻任何其它形式(空缺、大小写不一致、出现负数、小数点、非法字符等)均不合法,直接输出字符串 "ERROR"
输出字符串 "3 GBP 1 USD 7 CNY 1 HKD"
⑴注意输出每组货币都是 数字+空格+货币种类简称
⑵多组不同货币也是以1个空格分开，例如"3 GBP 1 USD"
⑶输出字符串前后没有空格
⑷输出字符串前后没有双引号(")
(5)若输入不合法直接输出字符串"ERROR"

示例1：
输入：
2 8 2 127 HKD MAX
1 6 1 127 HKD max

输出
3 GBP 1 USD 7 CNY 1 HKD
ERROR
"""
import logging

moneySpecies = ['GBP', 'USD', 'CNY', 'HKD']


def logger():
    logging.basicConfig(level='INFO', format='%(levelname)s The PUTOUT: %(message)s')
    log = logging.getLogger(__name__)
    return log


class CountExchangeRate(object):
    """
    1 CNY = 2 HKD
    1 USD = 8 CNY
    1 GBP = 2 USD
    GBP>USD>CNY>HKD
    """

    def __init__(self, money_num: int, currency_type: str, count_type: str, c2h: int = 2, u2c: int = 8, g2u: int = 2):

        self.hkd_unit_value = 1
        self.c2h = c2h
        self.u2c = u2c
        self.g2u = g2u
        self.money_num = money_num
        self.currency_type = currency_type
        self.count_type = count_type
        self.hkd_unit = 'HKD'
        self.cny_unit = 'CNY'
        self.gbp_unit = 'GBP'
        self.usd_unit = 'USD'
        self.min_value_currency = self.hkd_unit
        self.parities()

    def parities(self):
        self.cny_unit_value = self.c2h * self.hkd_unit_value
        self.usd_unit_value = self.u2c * self.cny_unit_value
        self.gbp_unit_value = self.g2u * self.usd_unit_value

    def get_input_type(self):
        return {'HKD': self.hkd_unit_value,
                'CNY': self.cny_unit_value,
                'GBP': self.gbp_unit_value,
                'USD': self.usd_unit_value}

    def get_min_unit_value(self):
        value = self.money_num * self.get_input_type().get(self.currency_type)
        return value

    def get_max_unit_value(self):
        min_money_value = self.get_min_unit_value()
        gbp_value, remainder = self.get_integer_remainder(min_money_value, self.gbp_unit_value)
        usd_value, remainder = self.get_integer_remainder(remainder, self.usd_unit_value)
        cny_value, hkd_value = self.get_integer_remainder(remainder, self.cny_unit_value)
        return gbp_value, usd_value, cny_value, hkd_value

    @staticmethod
    def get_integer_remainder(dividend, divisor):
        integer = dividend // divisor
        remainder = dividend % divisor
        return integer, remainder

    def exe(self):
        if self.count_type == 'MAX':
            gbp_value, usd_value, cny_value, hkd_value = self.get_max_unit_value()
            tmp_unit = {self.gbp_unit: gbp_value,
                        self.usd_unit: usd_value,
                        self.cny_unit: cny_value,
                        self.hkd_unit: hkd_value}
            result = []
            for money_s in moneySpecies:
                value = tmp_unit.get(money_s)
                if value != 0:
                    result.append(value)
                    result.append(money_s)
            return ' '.join(map(str, result))
        elif self.count_type == 'MIN':
            value = self.get_min_unit_value()
            result = [value, self.min_value_currency]
            return ' '.join(map(str, result))
        else:
            raise


def check_integer(num):
    try:
        value = int(num)
        if value > 0:
            return value
        else:
            raise
    except TypeError:
        raise


def check_input_error(input_info):
    c2h, u2c, g2u, money_num, currency_type, count_type = input_info.strip().split()
    if currency_type not in moneySpecies:
        raise
    elif count_type not in {'MAX', 'MIN'}:
        raise
    money_num = check_integer(money_num)
    c2h = check_integer(c2h)
    u2c = check_integer(u2c)
    g2u = check_integer(g2u)
    return c2h, u2c, g2u, money_num, currency_type, count_type


def main():
    log = logger()
    try:
        input_info = input("intput:")  # 2 8 2 127 HKD MAX
        print(f'input_info--->{input_info}')
        c2h, u2c, g2u, money_num, currency_type, count_type = check_input_error(input_info)
        cer = CountExchangeRate(money_num, currency_type, count_type, c2h, u2c, g2u)
        log.info(cer.exe())
    except Exception as e:
        log.warning('ERROR')
        log.exception(e)


if __name__ == '__main__':
    main()
