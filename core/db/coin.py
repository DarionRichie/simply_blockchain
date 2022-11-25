# 依赖注入, 不应该受到db的影响

TEST_COIN_LIST = [
    {
        "id": "0x1",
        "block": "0x1",
        "tx_hash": "0x1",
        "owner": "0x11",
        "count": 100,
        "is_spent": False,
    },
    {
        "id": "0x2",
        "block": "0x1",
        "tx_hash": "0x1",
        "owner": "0x22",
        "count": 100,
        "is_spent": False,
    }
]


class TestCoinDB(object):
    @classmethod
    def GetCoinByOwner(cls, owner):
        return list(filter(lambda x : x["owner"] == owner, TEST_COIN_LIST))

    @classmethod
    def GetCoinById(cls, coin_id):
        return list(filter(lambda x : x["owner"] == coin_id, TEST_COIN_LIST))


if __name__ == "__main__":
    print(TestCoinDB.GetCoin("0x11"))
