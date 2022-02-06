import unittest 
from controllers import *
from orders import *

#input is validated by main function the following tests validate the working of the controllers


   
class TestSSE(unittest.TestCase):
    def test_market_transfer_share_1(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, 22)
        sell_order = orders("SELl", "SNAP", "MKT", None, 22)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "FILLED")
    
    def test_market_transfer_share_2(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, 30)
        sell_order = orders("SELl", "SNAP", "MKT", None, 22)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "PARTIAL")
        self.assertEqual(sell_order.status, "FILLED")
        self.assertEqual(buy_order.filled, sell_order.filled)
    
    def test_market_transfer_share_3(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, 22)
        sell_order = orders("SELl", "SNAP", "MKT", None, 30)
        buy_order_1 = orders("BUY", "SNAP", "MKT", None, 8)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "PARTIAL")
        self.assertEqual(buy_order.filled, sell_order.filled)
        transfer_share(buy_order_1, sell_order)
        self.assertEqual(buy_order_1.status, "FILLED")
        self.assertEqual(sell_order.status, "FILLED")

    def test_market_transfer_share_4(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, 0)
        sell_order = orders("SELl", "SNAP", "MKT", None, 0)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "FILLED")

    def test_market_transfer_share_5(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, 0)
        sell_order = orders("SELl", "SNAP", "MKT", None, 10)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "PENDING")
    
    def test_market_transfer_share_6(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, 10)
        sell_order = orders("SELl", "SNAP", "MKT", None, 0)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "PENDING")
        self.assertEqual(sell_order.status, "FILLED")

    def test_market_transfer_share_7(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, -1)
        sell_order = orders("SELl", "SNAP", "MKT", None, -1)
        self.assertRaises(Exception ,transfer_share(buy_order, sell_order)) 

    def test_market_transfer_share_8(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, -10)
        sell_order = orders("SELl", "SNAP", "MKT", None, 0)
        self.assertRaises(Exception ,transfer_share(buy_order, sell_order))  

    def test_market_transfer_share_9(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, 0)
        sell_order = orders("SELl", "SNAP", "MKT", None, -10)
        self.assertRaises(Exception ,transfer_share(buy_order, sell_order))

    def test_limit_transfer_share_1(self):
        buy_order =  orders("BUY", "SNAP", "LMT", 100, 22)
        sell_order = orders("SELl", "SNAP", "LMT", 100, 22)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "FILLED")

    def test_limit_transfer_share_2(self):
        buy_order =  orders("BUY", "SNAP", "LMT", 105, 22)
        sell_order = orders("SELl", "SNAP", "LMT", 100, 22)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "FILLED")

    def test_limit_transfer_share_3(self):
        buy_order =  orders("BUY", "SNAP", "LMT", 105, -22)
        sell_order = orders("SELl", "SNAP", "LMT", 100, 22)
        self.assertRaises(Exception ,transfer_share(buy_order, sell_order)) 
    
    def test_limit_transfer_share_4(self):
        buy_order =  orders("BUY", "SNAP", "LMT", 105, 22)
        sell_order = orders("SELl", "SNAP", "MKT", None, 22)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "FILLED")

    def test_limit_transfer_share_5(self):
        buy_order =  orders("BUY", "SNAP", "LMT", 105, 22)
        sell_order = orders("SELl", "SNAP", "MKT", None, 22)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "FILLED")

    def test_limit_transfer_share_6(self):
        buy_order =  orders("BUY", "SNAP", "MKT", None, 22)
        sell_order = orders("SELl", "SNAP", "MKT", 10, 22)
        transfer_share(buy_order, sell_order)
        self.assertEqual(buy_order.status, "FILLED")
        self.assertEqual(sell_order.status, "FILLED")        
    



if __name__ == '__main__':
    unittest.main()