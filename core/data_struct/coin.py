from typing import List


class Coin(object):
    id_ = None
    block_ = None
    tx_hash_ = None
    owner_ = None
    count_ = None
    is_spent_: bool = True

    def __init__(self, id: str, block: str, tx_hash: str, owner: str, count: int, is_spent : bool):
        self.id_ = id
        self.block_ = block   # int
        self.tx_hash_ = tx_hash  # 0x string
        self.owner_ = owner   # 0x string
        self.count_ = count   # int
        self.is_spent_ = is_spent

    def SelfCheck(self):
        assert (self.block_ is not None), "self block_ is None"
        assert (self.tx_hash_ is not None), "self tx_hash_ is None"
        assert (self.owner_ is not None), "self owner_ is None"

    def Verify(self, sign: str, spent_user: str) -> bool:
        # 校验目前是否可以被spent_user来花费
        assert self.is_spent_ == False

    def GetCount(self):
        return self.count_
    
    def Spented(self):
        self.is_spent_ = True

    def Serilized(self):
        return {
            "id": self.id_,
            "block": self.block_,
            "tx_hash": self.tx_hash_,
            "owner": self.owner_,
            "count": self.count_,
            "is_spent": self.is_spent_,
        }
    
    def __str__(self):
        return self.Serilized()
    


class TxInput(object):
    # 交易输入中间包括的coin??? coin这个结构体有没有必要??
    coin_list_ = []  # list[Coin]
    from_address_ = None
    from_address_sign_ = None

    def __init__(self, coin_list: List[Coin], from_address: str, from_address_sign: str):
        self.coin_list_ = coin_list
        self.from_address_ = from_address
        self.from_address_sign_ = from_address_sign

    # 做验证签名/是否正确
    def VerifySign(self) -> bool:
        for one_coin in self.coin_list_:
            if one_coin.Verify(self.from_address_sign_, self.from_address_):
                return False

        return True

    # 总体校验
    def Verify(self) -> bool:
        if not self.VerifySign():
            return False

        return True

    # TODO(kingxinwang): 要校验状态
    def Spented(self):
        for one_coin in self.coin_list_:
            one_coin.Spented()


class TxOutput(object):
    coin_output_ = []

    # 每一个coin都需要做序列化存储下来
    def Save(self):
        for one_coin in self.coin_output_:
            pass