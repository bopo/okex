# -*- coding: utf-8 -*-

from .context import OKExMarketAPI

import unittest


class MarketTestSuite(unittest.TestCase):
    """Basic test cases."""

    apikey = '0b72f8d4-b5dd-4b0c-b8d6-7c55c8405799'
    secret = '31F73BBC196B0472DFFFFAA215F22B45'
    
    def test_exchange_rate(self):
        client = OKExMarketAPI('https://www.okex.com',self.apikey, self.secret)
        assert client.exchange_rate()


if __name__ == '__main__':
    unittest.main()