# -*- coding: utf-8 -*-

from .context import SYMBOLS, CONTRACT_TYPE, TYPES
from .helpers import Request


class OKExBase(object):
    """
    基础类
    """
    URI = {
        'ticker': '/api/v1/{}ticker.do',
        'depth': '/api/v1/{}depth.do',
        'kline': '/api/v1/{}kline.do',
        'trades': '/api/v1/{}trades.do',
        'index': '/api/v1/future_index.do',
        'exchange_rate': '/api/v1/exchange_rate.do',
        'estimated_price': '/api/v1/future_estimated_price.do',
        'hold_amount': '/api/v1/future_hold_amount.do',
        'price_limit': '/api/v1/future_price_limit.do',
        'user_info': '/api/v1/{}userinfo.do',

        'position': '/api/v1/future_position.do',
        'trades_history': '/api/v1/future_trades_history.do',
        'batch_trade': '/api/v1/future_batch_trade.do',
        'cancel': '/api/v1/future_cancel.do',
        'order_info': '/api/v1/future_order_info.do',
        'orders_info': '/api/v1/future_orders_info.do',
        'user_info_4fix': '/api/v1/future_userinfo_4fix.do',
        'position_4fix': '/api/v1/future_position_4fix.do',
        'explosive': '/api/v1/future_explosive.do',
        'withdraw': '/api/v1/withdraw.do',
        'cancel_withdraw': '/api/v1/cancel_withdraw.do',
        'withdraw_info': '/api/v1/withdraw_info.do'
    }

    def __init__(self, url, apikey, secret):
        """
        Constructor for class of OKExBase.
        :param url: Base URL for REST API of Future
        :param apikey: String of API KEY
        :param secret: String of SECRET KEY
        :return: None
        """
        self._apikey = apikey
        self._secret = secret
        self._request = Request(url=url, key=secret)


class OKExMarketAPI(OKExBase):

    def __init__(self, url, apikey, secret):
        """
        Constructor for class of OKExMarketAPI.
        :param url: Base URL for REST API of Future
        :param apikey: String of API KEY
        :param secret: String of SECRET KEY
        :return: None
        """
        super(OKExMarketAPI, self).__init__(url, apikey, secret)

    @classmethod
    def build_request_string(cls, name, value, params='', choice=()):
        """

        :param name:
        :param value:
        :param params:
        :param choice:
        :return:
        """
        if value:
            if value in choice:
                return params + '&' + name + '=' + str(value) if params else name + '=' + str(value)
            else:
                raise ValueError('{0} should be in {1}'.format(value, choice))
        else:
            return params

    def ticker(self, symbol, contract_type, future_or_spot=True):
        """
        OKCOIN行情信息
        :param symbol:
        :param contract_type:
        :param future_or_spot:
        :return:
        """
        params = OKExMarketAPI.build_request_string('symbol', symbol, '', SYMBOLS)
        params = OKExMarketAPI.build_request_string('contract_type', contract_type, params, CONTRACT_TYPE)
        url = OKExBase.URI['ticker'].format('future_' if future_or_spot else '')
        return self._request.get(url, params)

    def depth(self, symbol, contract_type, size=0, merge=0, future_or_spot=True):
        """
        OKEx期货市场深度信息
        :param symbol:
        :param contract_type:
        :param size:
        :param merge:
        :param future_or_spot:
        :return:
        """
        params = OKExMarketAPI.build_request_string('symbol', symbol, '', SYMBOLS)
        params = OKExMarketAPI.build_request_string('contract_type', contract_type, params, CONTRACT_TYPE)
        params = OKExMarketAPI.build_request_string('size', size, params, range(1, 201))
        params = OKExMarketAPI.build_request_string('merge', merge, params, (0, 1))
        return self._request.get(OKExBase.URI['depth'].format('future_' if future_or_spot else ''), params)

    def trades(self, symbol, contract_type, future_or_spot=True):
        """
        OKEx期货交易记录信息
        :param symbol:
        :param contract_type:
        :param future_or_spot:
        :return:
        """
        params = OKExMarketAPI.build_request_string('symbol', symbol, '', SYMBOLS)
        params = OKExMarketAPI.build_request_string('contract_type', contract_type, params, CONTRACT_TYPE)
        return self._request.get(OKExBase.URI['trades'].format('future_' if future_or_spot else ''),
                                 params)

    def future_index(self, symbol=None):
        """
        OKEx期货指数
        :param symbol:
        :return:
        """
        params = OKExMarketAPI.build_request_string('symbol', symbol, '', SYMBOLS)
        return self._request.get(OKExBase.URI['index'], params)

    def exchange_rate(self):
        """
        获取美元人民币汇率
        :return:
        """
        return self._request.get(OKExBase.URI['exchange_rate'], '')

    def future_estimated_price(self, symbol):
        """
        获取预估交割价
        :param symbol:
        :return:
        """
        params = OKExMarketAPI.build_request_string('symbol', symbol, '', SYMBOLS)
        return self._request.get(OKExBase.URI['estimated_price'], params)

    def kline(self, symbol=None, type_=None, future_or_spot=True):
        """
        获取虚拟合约的K线数据
        :param future_or_spot:
        :param symbol:
        :param type_:
        :return:
        """
        params = OKExMarketAPI.build_request_string('symbol', symbol, '', SYMBOLS)
        params = OKExMarketAPI.build_request_string('type', type_, params, TYPES)
        uri = OKExBase.URI['kline'].format('future_' if future_or_spot else '')
        return self._request.get(uri, params)

    def future_hold_amount(self, symbol, contract_type):
        """
        获取当前可用合约总持仓量
        :param symbol:
        :param contract_type:
        :return:
        """
        params = OKExMarketAPI.build_request_string('symbol', symbol, '', SYMBOLS)
        params = OKExMarketAPI.build_request_string('contract_type', contract_type, params, CONTRACT_TYPE)
        return self._request.get(OKExBase.URI['hold_amount'], params)

    def future_price_limit(self, symbol, contract_type):
        """
        获取合约最高买价和最低卖价
        :param symbol:
        :param contract_type:
        :return:
        """
        params = OKExMarketAPI.build_request_string('symbol', symbol, '', SYMBOLS)
        params = OKExMarketAPI.build_request_string('contract_type', contract_type, params, CONTRACT_TYPE)
        return self._request.get(OKExBase.URI['price_limit'], params)


class OKExTraderAPI(OKExBase):

    def __init__(self, url, apikey, secret):
        """
        Constructor for class of OKExFuture.
        :param url: Base URL for REST API of Future
        :param apikey: String of API KEY
        :param secret: String of SECRET KEY
        :return: None
        """
        super(OKExTraderAPI, self).__init__(url, apikey, secret)

    def user_info(self):
        """
        期货全仓账户信息
        :return:
        """
        params = {'api_key': self._apikey}
        return self._request.post(OKExBase.URI['user_info'], params, True)

    def future_position(self, symbol, contract_type):
        """
        期货全仓持仓信息
        :param symbol:
        :param contract_type:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type
        }

        return self._request.post(OKExBase.URI['position'], params, True)

    def future_trade(self, symbol, contract_type, price='', amount='', trade_type='', match_price='', lever_rate=''):
        """
        期货下单
        :param symbol:
        :param contract_type:
        :param price:
        :param amount:
        :param trade_type:
        :param match_price:
        :param lever_rate:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'amount': amount,
            'type': trade_type,
            'match_price': match_price,
            'lever_rate': lever_rate
        }

        if price:
            params['price'] = price

        return self._request.post(OKExBase.URI['trades'], params, True)

    def future_trade_history(self, symbol, date, since):
        """
        获取OKEX合约交易历史（非个人）
        :param symbol:
        :param date:
        :param since:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'date': date,
            'since': since
        }

        return self._request.post(OKExBase.URI['trades_history'], params, True)

    # 期货批量下单
    def future_batch_trade(self, symbol, contract_type, orders_data, lever_rate):
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'orders_data': orders_data,
            'lever_rate': lever_rate
        }

        return self._request.post(OKExBase.URI['batch_trade'], params, True)

    def future_cancel(self, symbol, contract_type, order_id):
        """
        期货取消订单
        :param symbol:
        :param contract_type:
        :param order_id:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'order_id': order_id
        }

        return self._request.post(OKExBase.URI['cancel'], params, True)

    def future_order_info(self, symbol, contract_type, order_id, status, current_page, page_length):
        """
        期货获取订单信息
        :param symbol:
        :param contract_type:
        :param order_id:
        :param status:
        :param current_page:
        :param page_length:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'order_id': order_id,
            'status': status,
            'current_page': current_page,
            'page_length': page_length
        }

        return self._request.post(OKExBase.URI['order_info'], params, True)

    def future_orders_info(self, symbol, contract_type, order_id):
        """
        期货获取订单信息
        :param symbol:
        :param contract_type:
        :param order_id:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'order_id': order_id
        }

        return self._request.post(OKExBase.URI['orders_info'], params, True)

    def future_user_info_4fix(self):
        """
        期货逐仓账户信息
        :return:
        """
        params = {'api_key': self._apikey}

        return self._request.post(OKExBase.URI['user_info_4fix'], params, True)

    def future_position_4fix(self, symbol, contract_type, trade_type):
        """
        期货逐仓持仓信息
        :param symbol:
        :param contract_type:
        :param trade_type:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'type': trade_type
        }

        return self._request.post(OKExBase.URI['position_4fix'], params, True)

    def future_explosive(self, symbol, contract_type, status, current_page, page_number, page_length):
        """
        获取合约爆仓单
        :param symbol:
        :param contract_type:
        :param status:
        :param current_page:
        :param page_number:
        :param page_length:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'status': status,
            'current_page': current_page,
            'page_number': page_number,
            'page_length': page_length
        }

        return self._request.post(OKExBase.URI['explosive'], params, True)

    def future_withdraw(self, symbol, charge_fee, trade_pwd, withdraw_address, withdraw_amount, target):
        """
        提币BTC/LTC
        :param symbol:
        :param charge_fee:
        :param trade_pwd:
        :param withdraw_address:
        :param withdraw_amount:
        :param target:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'charge_fee': charge_fee,
            'trade_pwd': trade_pwd,
            'withdraw_address': withdraw_address,
            'withdraw_amount': withdraw_amount,
            'target': target
        }

        return self._request.post(OKExBase.URI['withdraw'], params, True)

    def future_cancel_withdraw(self, symbol, withdraw_id):
        """
        取消提币BTC/LTC
        :param symbol:
        :param withdraw_id:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'withdraw_id': withdraw_id
        }

        return self._request.post(OKExBase.URI['cancel_withdraw'], params, True)

    def future_withdraw_info(self, symbol, withdraw_id):
        """
        查询提币BTC/LTC信息
        :param symbol:
        :param withdraw_id:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'withdraw_id': withdraw_id
        }

        return self._request.post(OKExBase.URI['withdraw_info'], params, True)
