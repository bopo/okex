# -*- coding: utf-8 -*-


from okex.core import OKExTradeAPI
import unittest


class TraderTestSuite(unittest.TestCase):
    """Advanced test cases."""
    apikey = '0b72f8d4-b5dd-4b0c-b8d6-7c55c8405799'
    secret = '31F73BBC196B0472DFFFFAA215F22B45'
    
    def test_user_info(self):
        client = OKExTradeAPI('https://www.okex.com', self.apikey, self.secret)
        assert client.future_user_info()


if __name__ == '__main__':
    unittest.main()
