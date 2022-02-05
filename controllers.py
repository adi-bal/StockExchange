def view_orders(order_list):
    num = 1
    for order in order_list:
        if(order.price is None):
            print("{}. {} {} {} {}/{} {}".format(num, order.share_name, order.limit, order.type, order.filled, order.qty, order.status))
        else:
            print("{}. {} {} {} ${} {}/{} {}".format(num, order.share_name, order.limit, order.type, order.price, order.filled, order.qty, order.status))
        num +=1

def transfer_share(buy_order, sell_order):      #transfers shares and updates latest transaction
    try:
        n_sell = sell_order.qty - sell_order.filled
        n_buy = buy_order.qty - buy_order.filled
        assert(n_sell >= 0)
        assert(n_buy>=0)
    except:
        print("Invalid Transaction")

    if n_sell > n_buy :
        buy_order.filled =buy_order.qty
        sell_order.filled += n_buy
    elif n_sell < n_buy :
        sell_order.filled = sell_order.qty
        buy_order.filled += n_sell
    elif n_sell == n_buy:
        buy_order.filled =buy_order.qty
        sell_order.filled = sell_order.qty
    
    if sell_order.qty == sell_order.filled:     #updating the status of orders
        sell_order.status = "FILLED"
    elif sell_order.filled > 0:
        sell_order.status == "PARTIAL"
    
    if buy_order.qty == buy_order.filled:
        buy_order.status = "FILLED"
    elif buy_order.filled > 0:
        buy_order.status = "PARTIAL"

    if buy_order.limit == "LMT":
        bid[buy_order.share_name].last = buy_order.price
    elif sell_order.limit == "LMT":
        bid[sell_order.share_name].last = sell_order.price


def resolve_order(order_list, buy_orders, sell_orders):  #resolves order, called eveytime a new order is placed
    try:
        new_order = order_list[-1]
        if new_order.type == "BUY":
            for sell in sell_orders:
                if sell.share_name == new_order.share_name and sell.status != "FILLED" and new_order.status != "FILLED":
                    if (sell.limit == "LMT" and new_order.limit == "LMT") and (sell.price <= new_order.price):
                        transfer_share(new_order, sell)
                    elif sell.limit == "LMT" and new_order.limit == "LMT":
                        continue
                    transfer_share(new_order, sell)
        else:
            for buy in buy_orders:
                if buy.share_name == new_order.share_name and buy.status != "FILLED" and new_order.status != "FILLED":
                    if (buy.limit == "LMT" and new_order.limit == "LMT") and (buy.price >= new_order.price):
                        transfer_share(buy, new_order)
                    elif buy.limit == "LMT" and new_order.limit == "LMT":
                        continue 
                    transfer_share(buy, new_order)
    except IndexError:
        print("Invalid list sizes")
