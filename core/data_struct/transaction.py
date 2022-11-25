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

    def Check(self):
        assert self.from_address_ is not None, "self from_address is None"
        assert self.from_address_sign_ is not None, "self from_address is None"

    def DoTx(self):
        self.Check()
        self.tx_input_.Spented()
        self.tx_ouput_.Save()
        
