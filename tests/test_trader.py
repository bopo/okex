# -*- coding: utf-8 -*-

import unittest

from .context import *


class TraderTestSuite(unittest.TestCase):
    """Trader test cases."""

    def setUp(self):
        self.client = OKExTraderAPI(apikey=APIKEY, secret=SECRET)

    def test_user_info(self):
        assert self.client.user_info(future=True)
        assert self.client.user_info(future=False)

    # 期货全仓持仓信息
    def test_future_position(self):
        assert self.client.future_position(symbol='btc_usd', contract_type='this_week')

    # def test_future_trade(self):
    #     assert self.client.future_trade(symbol='btc_usd', contract_type='this_week', price='', amount='', trade_type='', match_price='',
    #                                     lever_rate='')

    # def test_future_trade_history(self):
    #     assert self.client.future_trade_history(symbol='btc_usd', date, since)

    # def test_future_batch_trade(self):
    #     assert self.client.future_batch_trade(symbol='btc_usd', contract_type='this_week', orders_data, lever_rate)

    def test_future_cancel(self):
        assert self.client.future_cancel(symbol='btc_usd', contract_type='this_week', order_id='123123123123')

    # def test_future_order_info(self):
    #     assert self.client.future_order_info(symbol='btc_usd', contract_type='this_week', order_id, status, current_page, page_length)

    def test_future_orders_info(self):
        assert self.client.future_orders_info(symbol='btc_usd', contract_type='this_week', order_id='123123123123')

    def test_future_user_info_4fix(self):
        assert self.client.future_user_info_4fix()

    def test_future_position_4fix(self):
        assert self.client.future_position_4fix(symbol='btc_usd', contract_type='this_week', trade_type='ss')

    # def test_future_explosive(self):
    #     assert self.client.future_explosive(symbol='btc_usd', contract_type='this_week', status, current_page, page_number, page_length)

    # def test_future_withdraw(self):
    #     assert self.client.future_withdraw(symbol='btc_usd', charge_fee, trade_pwd, withdraw_address, withdraw_amount, target)

    def test_future_cancel_withdraw(self):
        assert self.client.future_cancel_withdraw(symbol='btc_usd', withdraw_id='sssss')

    def test_future_withdraw_info(self):
        assert self.client.future_withdraw_info(symbol='btc_usd', withdraw_id='2342432424')


if __name__ == '__main__':
    unittest.main()
