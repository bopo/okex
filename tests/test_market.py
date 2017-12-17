# -*- coding: utf-8 -*-

import unittest

from .context import *


class MarketTestSuite(unittest.TestCase):
    """Market test cases."""

    def setUp(self):
        self.client = OKExMarketAPI('https://www.okex.com', APIKEY, SECRET)

    def test_exchange_rate(self):
        assert self.client.exchange_rate()

    def test_ticker(self):
        assert self.client.ticker(symbol='btc_usd', contract_type='this_week', future_or_spot=True)
        assert self.client.ticker(symbol='btc_usd', contract_type='this_week', future_or_spot=False)

    def test_depth(self):
        assert self.client.depth(symbol='btc_usd', size=10, merge=0, contract_type='this_week', future_or_spot=True)
        assert self.client.depth(symbol='btc_usd', size=10, merge=1, contract_type='this_week', future_or_spot=True)
        assert self.client.depth(symbol='btc_usd', size=10, merge=0, contract_type='this_week', future_or_spot=False)
        assert self.client.depth(symbol='btc_usd', size=10, merge=1, contract_type='this_week', future_or_spot=False)

    def test_trades(self):
        assert self.client.trades(symbol='btc_usd', contract_type='this_week', future_or_spot=True)
        assert self.client.trades(symbol='btc_usd', contract_type='this_week', future_or_spot=False)

    def test_index(self):
        assert self.client.future_index(symbol='btc_usd')
        assert self.client.future_index(symbol='ltc_usd')

    def test_future_estimated_price(self):
        assert self.client.future_estimated_price(symbol='btc_usd')

    def test_future_kline(self):
        assert self.client.kline(symbol='ltc_btc', type_='1min', future_or_spot=True)
        assert self.client.kline(future_or_spot=False)

    def test_future_hold_amount(self):
        assert self.client.future_hold_amount(symbol='btc_usd', contract_type='this_week')

    def test_future_price_limit(self):
        # future_price_limit.do?symbol = btc_usd & contract_type = this_week
        assert self.client.future_price_limit(symbol='btc_usd', contract_type='this_week')


# future_depth.do?symbol=btc_usd&contract_type=this_week
if __name__ == '__main__':
    unittest.main()
