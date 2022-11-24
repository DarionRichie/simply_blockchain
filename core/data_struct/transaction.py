from typing import *
from coin import *


class Tx(object):
    tx_hash_ = None
    tx_input_: TxInput = None
    tx_ouput_: TxOutput = None

    from_address_ = None
    from_address_sign_ = None
    to_address = None
    tx_count_ = None

    def __init__(self):
        pass

    def GenTxInput(self):
        # 利用from_address去拉数据
        # tx内容可以序列化进去(简单json就可以)
        # 累加>count就可以
        pass
