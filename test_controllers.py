import unittest 
from controllers import *
from orders import *

buy_order_list_limit =[
    orders("BUY", "SNAP", "LMT", 95, 22)
    
]

buy_order_list_market = [
    orders("BUY", "SNAP", "MKT", None, 22)
   
]

sell_order_list_limit = [
    orders("SELL", "SNAP", "LMT", 100, 22)  
]

sell_order_list_market =[
    orders("SELl", "SNAP", "MKT", None, 22)
]


class TestSSE(unittest.TestCase):
    def test_resolve_order(self):
        transfer_share(buy_order_list_market[0], sell_order_list_market[0])
        self.assertEqual(buy_order_list_market[0].status, "FILLED")

if __name__ == '__main__':
    unittest.main()