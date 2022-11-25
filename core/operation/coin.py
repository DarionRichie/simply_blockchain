import data_struct.coin
from db.coin import TestCoinDB

def InitCoin(coin_id):
    # 读取数据库获取coin的内容
    return TestCoinDB.GetCoinById(coin_id)


def GetOwnerCoin(owner):
    # 读取数据库的coin的内容
    return TestCoinDB.GetCoinByOwner(owner)