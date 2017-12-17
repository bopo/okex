# -*- coding: utf-8 -*-

from .context import SYMBOLS, CONTRACT_TYPE, TYPES, ENDPOINT
from .helpers import Request


class OKExBase(object):
    """
    基础类
    """
    def __init__(self, host, apikey, secret):
        """
        Constructor for class of OKExBase.
        :param host: Base URL for REST API of Future
        :param apikey: String of API KEY
        :param secret: String of SECRET KEY
        :return: None
        """
        self._apikey = apikey
        self._secret = secret
        self._request = Request(host=host, key=secret)


class OKExMarketAPI(OKExBase):

    def __init__(self, host=None, apikey=None, secret=None):
        """
        Constructor for class of OKExMarketAPI.
        :param url: Base URL for REST API of Future
        :param apikey: String of API KEY
        :param secret: String of SECRET KEY
        :return: None
        """
        super(OKExMarketAPI, self).__init__(host, apikey, secret)

    def build_string(self, name, value, params='', choice=()):
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

    def ticker(self, symbol, contract_type, future=True):
        """
        行情信息
        :param symbol:
        :param contract_type:
        :param future:
        :return:
        """
        params = self.build_string('symbol', symbol, '', SYMBOLS)
        params = self.build_string('contract_type', contract_type, params, CONTRACT_TYPE)
        url = ENDPOINT['ticker'].format('future_' if future else '')
        return self._request.get(url, params)

    def depth(self, symbol, contract_type, size=0, merge=0, future=True):
        """
        市场深度信息
        :param symbol:
        :param contract_type:
        :param size:
        :param merge:
        :param future:
        :return:
        """
        params = self.build_string('symbol', symbol, '', SYMBOLS)
        params = self.build_string('contract_type', contract_type, params, CONTRACT_TYPE)
        params = self.build_string('size', size, params, range(1, 201))
        params = self.build_string('merge', merge, params, (0, 1))
        return self._request.get(ENDPOINT['depth'].format('future_' if future else ''), params)

    def trades(self, symbol, contract_type, future=True):
        """
        交易记录信息
        :param symbol:
        :param contract_type:
        :param future:
        :return:
        """
        params = self.build_string('symbol', symbol, '', SYMBOLS)
        params = self.build_string('contract_type', contract_type, params, CONTRACT_TYPE)
        url = ENDPOINT['trades'].format('future_' if future else '')
        return self._request.get(url, params)

    def index(self, symbol=None, future=True):
        """
        合约期货指数
        :param symbol:
        :return:
        """
        params = self.build_string('symbol', symbol, '', SYMBOLS)
        url = ENDPOINT['index'].format('future_' if future else '')
        return self._request.get(url, params)

    def exchange_rate(self):
        """
        获取美元人民币汇率
        :return:
        """
        return self._request.get(ENDPOINT['exchange_rate'], '')

    def future_estimated_price(self, symbol):
        """
        获取合约预估交割价
        :param symbol:
        :return:
        """
        params = self.build_string('symbol', symbol, '', SYMBOLS)
        return self._request.get(ENDPOINT['estimated_price'], params)

    def kline(self, symbol=None, type_=None, future=True):
        """
        获取K线数据
        :param future:
        :param symbol:
        :param type_:
        :return:
        """
        params = self.build_string('symbol', symbol, '', SYMBOLS)
        params = self.build_string('type', type_, params, TYPES)
        uri = ENDPOINT['kline'].format('future_' if future else '')
        return self._request.get(uri, params)

    def future_hold_amount(self, symbol, contract_type):
        """
        获取当前可用合约总持仓量
        :param symbol:
        :param contract_type:
        :return:
        """
        params = self.build_string('symbol', symbol, '', SYMBOLS)
        params = self.build_string('contract_type', contract_type, params, CONTRACT_TYPE)
        return self._request.get(ENDPOINT['hold_amount'], params)

    def future_price_limit(self, symbol, contract_type):
        """
        获取合约最高买价和最低卖价
        :param symbol:
        :param contract_type:
        :return:
        """
        params = self.build_string('symbol', symbol, '', SYMBOLS)
        params = self.build_string('contract_type', contract_type, params, CONTRACT_TYPE)
        return self._request.get(ENDPOINT['price_limit'], params)


class OKExTraderAPI(OKExBase):

    def __init__(self, host=None, apikey=None, secret=None):
        """
        Constructor for class of OKExFuture.
        :param url: Base URL for REST API of Future
        :param apikey: String of API KEY
        :param secret: String of SECRET KEY
        :return: None
        """
        super(OKExTraderAPI, self).__init__(host, apikey, secret)

    def user_info(self, future=True):
        """
        合约期货全仓账户信息
        :return:
        """
        params = {'api_key': self._apikey}
        url = ENDPOINT['user_info'].format('future_' if future else '')
        return self._request.post(url, params, True)

    def future_position(self, symbol, contract_type):
        """
        合约期货全仓持仓信息
        :param symbol:
        :param contract_type:
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type
        }

        return self._request.post(ENDPOINT['position'], params, True)

    def future_trade(self, symbol, contract_type, price='', amount='', trade_type='', match_price='', lever_rate=''):
        """
        合约期货下单
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

        return self._request.post(ENDPOINT['trades'], params, True)

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

        return self._request.post(ENDPOINT['trades_history'], params, True)

    # 合约期货批量下单
    def future_batch_trade(self, symbol, contract_type, orders_data, lever_rate):
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'orders_data': orders_data,
            'lever_rate': lever_rate
        }

        return self._request.post(ENDPOINT['batch_trade'], params, True)

    def future_cancel(self, symbol, contract_type, order_id):
        """
        合约期货取消订单
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

        return self._request.post(ENDPOINT['cancel'], params, True)

    def future_order_info(self, symbol, contract_type, order_id, status, current_page, page_length):
        """
        合约期货获取订单信息
        :param symbol:
        :param contract_type:
        :param order_id:
        :param status:
        :param current_page:
        :param page_length:
        
        :param amount: 委托数量
        :param contract_name: 合约名称
        :param create_date: 委托时间
        :param deal_amount: 成交数量
        :param fee: 手续费
        :param order_id: 订单ID
        :param price: 订单价格
        :param price_avg: 平均价格
        :param status: 订单状态(0等待成交 1部分成交 2全部成交 -1撤单 4撤单处理中)
        :param symbol: btc_usd ltc_usd eth_usd etc_usd bch_usd
        :param type: 订单类型 1：开多 2：开空 3：平多 4： 平空
        :param unit_amount:合约面值
        :param lever_rate: 杠杆倍数  value:10\20  默认10 
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

        return self._request.post(ENDPOINT['order_info'], params, True)

    def future_orders_info(self, symbol, contract_type, order_id):
        """
        合约期货获取订单信息
        :param symbol:
        :param contract_type:
        :param order_id:
        

        :param amount: 委托数量
        :param contract_name: 合约名称
        :param created_date: 委托时间
        :param deal_amount: 成交数量
        :param fee: 手续费
        :param order_id: 订单ID
        :param price: 订单价格
        :param price_avg: 平均价格
        :param status: 订单状态(0等待成交 1部分成交 2全部成交 -1撤单 4撤单处理中)
        :param symbol: btc_usd   ltc_usd    eth_usd    etc_usd    bch_usd
        :param type: 订单类型 1：开多 2：开空 3：平多 4：平空
        :param unit_amount:合约面值
        :param lever_rate: 杠杆倍数  value:10 or 20  默认10         
        :return:
        """
        params = {
            'api_key': self._apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'order_id': order_id
        }

        return self._request.post(ENDPOINT['orders_info'], params, True)

    def future_user_info_4fix(self):
        """
        合约期货逐仓账户信息
        :return:
        """
        params = {'api_key': self._apikey}

        return self._request.post(ENDPOINT['user_info_4fix'], params, True)

    def future_position_4fix(self, symbol, contract_type, trade_type):
        """
        合约期货逐仓持仓信息
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

        return self._request.post(ENDPOINT['position_4fix'], params, True)

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

        return self._request.post(ENDPOINT['explosive'], params, True)

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

        return self._request.post(ENDPOINT['withdraw'], params, True)

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

        return self._request.post(ENDPOINT['cancel_withdraw'], params, True)

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

        return self._request.post(ENDPOINT['withdraw_info'], params, True)
