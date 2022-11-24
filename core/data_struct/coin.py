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
        pass

    def GetCount(self):
        return self.count_


class TxInput(object):
    # 交易输入中间包括的coin??? coin这个结构体有没有必要??
    coin_list_ = []  # list[Coin]
    from_address_ = None
    from_address_sign_ = None
    to_address = None
    tx_count_ = None

    def __init__(self, coin_list: List[Coin], from_address: str, from_address_sign: str, to_address: str, tx_count: int):
        self.coin_list_ = coin_list
        self.from_address_ = from_address
        self.from_address_sign_ = from_address_sign
        self.to_address = to_address
        self.tx_count_ = tx_count

    # 做验证签名/是否正确
    def VerifySign(self) -> bool:
        for one_coin in self.coin_list_:
            if one_coin.Verify(self.from_address_sign_, self.from_address_):
                return False

        return True

    # 验证钱是否够了
    def VerifyCount(self) -> bool:
        if not self.verify_sign:
            # 签名不正确
            return False

        if sum([one_coin.GetCount() for one_coin in self.coin_list_]) < self.tx_count_:
            return False

        return True


class TxOutput(object):
    coin_output_ = []
    pass
