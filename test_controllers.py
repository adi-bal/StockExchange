import unittest 
from controllers import *
from orders import *

#input is validated by main function the following tests validate the working of the controllers

buy_order_list_limit =[
    orders("BUY", "SNAP", "LMT", 105, 22),
    orders("BUY", "SNAP", "LMT", 105, 10)
    
]

buy_order_list_market = [
    orders("BUY", "SNAP", "MKT", None, 22),
    orders("BUY", "SNAP", "MKT", None, 1)
   
]

sell_order_list_limit = [
    orders("SELL", "SNAP", "LMT", 100, 26),
    orders("SELL", "SNAP", "LMT", 100, 22),
]

sell_order_list_market =[
    orders("SELl", "SNAP", "MKT", None, 22),
    orders("SELL", "SNAP", "MKT", None, 1)
]


class TestSSE(unittest.TestCase):
    def test_market_transfer_share_1(self):
        transfer_share(buy_order_list_market[0], sell_order_list_market[0])
        self.assertEqual(buy_order_list_market[0].status, "FILLED")
        self.assertEqual(sell_order_list_market[0].status, "FILLED")

    def test_market_transfer_share_2(self):
        transfer_share(buy_order_list_market[1], sell_order_list_market[1])
        self.assertEqual(buy_order_list_market[1].status, "FILLED")
        self.assertEqual(sell_order_list_market[1].status, "FILLED")

    def test_limit_transfer_share_1(self):
        transfer_share(buy_order_list_limit[0], sell_order_list_limit[0])
        self.assertEqual(buy_order_list_limit[0].status, "FILLED")
        self.assertEqual(sell_order_list_limit[0].status, "PENDING")

    def test_limit_transfer_share_2(self):
        transfer_share(buy_order_list_limit[0], sell_order_list_market[0])
        self.assertEqual(buy_order_list_limit[0].status, "FILLED")
        self.assertEqual(sell_order_list_market[1].status, "PENDING")


if __name__ == '__main__':
    unittest.main()