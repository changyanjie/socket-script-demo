# coding: utf-8
import sys
import arrow
from prettytable import PrettyTable
sys.path.insert(1, '..')


def search_retailer_info(retailer_id):
    """查询基本信息"""
    print(u'当前主承运商:')
    x = PrettyTable([u'ID', u'名称', u'所在城市', u'采购服务'])
    x.add_row([
        retailer_id,
        u'张三',
        u'上海',
        u'服务1'
    ])
    print(x)
    return x


def search_current_agents(retailer_id):
    """"""
    print(u'当前主承运商:')
    x = PrettyTable([u'商户ID', u'商户名称', u'网格ID', u'主承运商', u'绑定时间'])
    x.add_row([
        retailer_id,
        u'张三',
        1,
        u'李四',
        arrow.now().date()
    ])
    print(x)
    return x


def main(retailer_id):
    search_current_agents(retailer_id)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("参数错误，正确使用姿势：python {} 14946827".format(__file__))
        sys.exit(1)
    ops_retailer_id = args[1]
    main(ops_retailer_id)
