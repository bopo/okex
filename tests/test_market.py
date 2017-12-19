# -*- coding: utf-8 -*-

import unittest

from ddt import ddt, data, unpack

from .context import *


@ddt
class MarketTestSuite(unittest.TestCase):
    """Market test cases."""

    def setUp(self):
        self.client = OKExAPI(apikey=APIKEY, secret=SECRET)

    @unpack
    def tearDown(self):
        pass

    def test_exchange_rate(self):
        assert self.client.get('exchange_rate')

    @data({'symbol': SYMBOLS[0], 'contract_type': CONTRACT_TYPE[0]})
    @unpack
    def test_ticker(self, symbol, contract_type):
        assert self.client.get('future_ticker', symbol=symbol, contract_type=contract_type, future=True)
        assert self.client.get('ticker', symbol=symbol, contract_type=contract_type, future=False)

    @data({'symbol': SYMBOLS[0], 'contract_type': CONTRACT_TYPE[0]})
    @unpack
    def test_depth(self, symbol, contract_type):
        assert self.client.get('future_depth', symbol=symbol, size=10, merge=0, contract_type=contract_type)
        assert self.client.get('future_depth', symbol=symbol, size=10, merge=1, contract_type=contract_type)
        assert self.client.get('depth', symbol=symbol, size=10, merge=0, contract_type=contract_type)
        assert self.client.get('depth', symbol=symbol, size=10, merge=1, contract_type=contract_type)

    def test_trades(self):
        assert self.client.get('future_trades', symbol='btc_usd', contract_type='this_week')
        assert self.client.get('trades', symbol='btc_usd', contract_type='this_week')

    def test_index(self):
        assert self.client.get('future_index', symbol='btc_usd')
        assert self.client.get('future_index', symbol='ltc_usd')

    def test_future_estimated_price(self):
        assert self.client.get('future_estimated_price', symbol='btc_usd')

    def test_future_kline(self):
        assert self.client.get('future_kline', symbol='ltc_btc', type_='1min')
        assert self.client.get('kline')

    def test_future_hold_amount(self):
        assert self.client.get('future_hold_amount', symbol='btc_usd', contract_type='this_week')

    def test_future_price_limit(self):
        assert self.client.get('future_price_limit', symbol='btc_usd', contract_type='this_week')

        # client.future(method='hold_amount', symbol='btc_usd', contract_type='this_week')
        # client.spot(method='', params=None)

if __name__ == '__main__':
    unittest.main()
