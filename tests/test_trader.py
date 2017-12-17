# -*- coding: utf-8 -*-

import unittest

from .context import *


class TraderTestSuite(unittest.TestCase):
    """Trader test cases."""

    def setUp(self):
        self.client = OKExTraderAPI('https://www.okex.com', APIKEY, SECRET)

    def test_user_info(self):
        assert self.client.user_info()


if __name__ == '__main__':
    unittest.main()
