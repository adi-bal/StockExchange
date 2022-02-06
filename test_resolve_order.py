import unittest 
from controllers import *
from orders import *

buy_orders = []    
sell_orders = []    
order_list = []        
bid = dict()  

buy_orders.append(orders("BUY", "SNAP", "MKT", None, 22))
sell_orders.append(orders("SELL", "SNAP", "MKT", None, 22))
order_list.append(orders("BUY", "SNAP", "MKT", None, 22)) 
order_list.append(orders("SELL", "SNAP", "MKT", None, 22))

class TestResolve(unittest.TestCase):
    def test_case_1(self):
        resolve_order(order_list, buy_orders, sell_orders)
        self.assertEqual(order_list[-1].status, "FILLED")

    def test_case_2(self):
        buy_orders.append(orders("BUY", "GOOG", "MKT", None, 10))
        order_list.append(orders("BUY", "GOOG", "MKT", None, 10))
        resolve_order(order_list, buy_orders, sell_orders)
        self.assertEqual(order_list[-1].status, "PENDING")
        sell_orders.append(orders("SELL", "GOOG", "MKT", None, 10))
        order_list.append(orders("SELL", "GOOG", "MKT", None, 10))
        resolve_order(order_list, buy_orders, sell_orders)
        self.assertEqual(order_list[-1].status, "FILLED")
    
    def test_case_3(self):
        buy_orders.append(orders("BUY", "GOOG", "LMT", 50, 100))
        order_list.append(orders("BUY", "GOOG", "LMT", 50, 100))
        sell_orders.append(orders("SELL", "GOOG", "LMT", 55, 50))
        order_list.append(orders("SELL", "GOOG", "LMT", 55, 50))
        resolve_order(order_list, buy_orders, sell_orders)
        self.assertEqual(order_list[-2].status, "PENDING")
        self.assertEqual(order_list[-1].status, "PENDING")
    
    def test_case_4(self):
        buy_orders.append(orders("BUY", "APPL", "LMT", 50, 75))
        order_list.append(orders("BUY", "APPL", "LMT", 50, 75))
        sell_orders.append(orders("SELL", "APPL", "LMT", 50, 75))
        order_list.append(orders("SELL", "APPL", "LMT", 50, 75))
        resolve_order(order_list, buy_orders, sell_orders)
        self.assertEqual(order_list[-1].status, "FILLED")
    
    def test_case_5(self):
        order_list =[]
        buy_orders =[]
        sell_orders =[]
        buy_orders.append(orders("BUY", "APPL", "LMT", 50, 75))
        order_list.append(orders("BUY", "APPL", "LMT", 50, 75))
        sell_orders.append(orders("SELL", "APPL", "LMT", 70, 75))
        order_list.append(orders("SELL", "APPL", "LMT", 70, 75))
        resolve_order(order_list, buy_orders, sell_orders)
        self.assertEqual(order_list[-1].status, "PENDING")
    
    def test_case_6(self):
        order_list =[]
        buy_orders =[]
        sell_orders =[]
        buy_orders.append(orders("BUY", "APPL", "LMT", 50, 100))
        order_list.append(orders("BUY", "APPL", "LMT", 50, 75))
        sell_orders.append(orders("SELL", "APPL", "LMT", 40, 125))
        order_list.append(orders("SELL", "APPL", "LMT", 40, 125))
        resolve_order(order_list, buy_orders, sell_orders)
        self.assertEqual(order_list[-1].status, "PARTIAL")
    
    def test_case_7(self):
        order_list =[]
        buy_orders =[]
        sell_orders =[]
        self.assertRaises(Exception,resolve_order(order_list, buy_orders, sell_orders) )

    def test_case_8(self):
        order_list =[]
        buy_orders =[]
        sell_orders =[]
        buy_orders.append(orders("BUY", "APPL", "LMT", 50, 75))
        sell_orders.append(orders("SELL", "APPL", "LMT", 70, 75))
        self.assertRaises(Exception,resolve_order(order_list, buy_orders, sell_orders) )
    
    def test_case_9(self):
        order_list =[]
        buy_orders =[]
        sell_orders =[]
        buy_orders.append(orders("BUY", "APPL", "LMT", 50, 75))
        self.assertRaises(Exception,resolve_order(order_list, buy_orders, sell_orders) )
    
    def test_case_10(self):
        order_list =[]
        buy_orders =[]
        sell_orders =[]
        order_list.append(orders("BUY", "APPL", "LMT", 50, 75))
        self.assertRaises(Exception,resolve_order(order_list, buy_orders, sell_orders) )



    

        

if __name__ == '__main__':
    unittest.main()