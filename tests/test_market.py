# -*- coding: utf-8 -*-

import unittest

from ddt import ddt, data, unpack

from .context import *


@ddt
class MarketTestSuite(unittest.TestCase):
    """Market test cases."""

    def setUp(self):
        self.client = OKExMarketAPI()

    @unpack
    def tearDown(self):
        pass

    def test_exchange_rate(self):
        assert self.client.exchange_rate()

    @data({'symbol': SYMBOLS[0], 'contract_type': CONTRACT_TYPE[0]})
    @unpack
    def test_ticker(self, symbol, contract_type):
        assert self.client.ticker(symbol=symbol, contract_type=contract_type, future=True)
        assert self.client.ticker(symbol=symbol, contract_type=contract_type, future=False)

    @data({'symbol': SYMBOLS[0], 'contract_type': CONTRACT_TYPE[0]})
    @unpack
    def test_depth(self, symbol, contract_type):
        assert self.client.depth(symbol=symbol, size=10, merge=0, contract_type=contract_type, future=True)
        assert self.client.depth(symbol=symbol, size=10, merge=1, contract_type=contract_type, future=True)
        assert self.client.depth(symbol=symbol, size=10, merge=0, contract_type=contract_type, future=False)
        assert self.client.depth(symbol=symbol, size=10, merge=1, contract_type=contract_type, future=False)

    def test_trades(self):
        assert self.client.trades(symbol='btc_usd', contract_type='this_week', future=True)
        assert self.client.trades(symbol='btc_usd', contract_type='this_week', future=False)

    def test_index(self):
        assert self.client.index(symbol='btc_usd', future=True)
        assert self.client.index(symbol='ltc_usd', future=True)

    def test_future_estimated_price(self):
        assert self.client.future_estimated_price(symbol='btc_usd')

    def test_future_kline(self):
        assert self.client.kline(symbol='ltc_btc', type_='1min', future=True)
        assert self.client.kline(future=False)

    def test_future_hold_amount(self):
        assert self.client.future_hold_amount(symbol='btc_usd', contract_type='this_week')

    def test_future_price_limit(self):
        assert self.client.future_price_limit(symbol='btc_usd', contract_type='this_week')


if __name__ == '__main__':
    unittest.main()
