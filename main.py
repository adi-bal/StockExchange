from orders import *
from quotes import * 
from controllers import *

buy_orders = []     #list to store buy order objects
sell_orders = []      #list to store sell order objects
order_list = []        # list to store all order objects
bid = dict()    # dictionary to store all quote objects


while True:     # loop receives and validates user input 
    command = input("Action : ").split()
    try:
        if command[0] == "VIEW" and command[1] == "ORDERS":
            view_orders(order_list)
        elif command[0] == "QUIT":
            break
        elif command[0] == "QUOTE":
            try:
                share_name = command[1]
                bid[share_name].view()
            except KeyError:
                print("No quotes for {} found".format(share_name))
            except IndexError:
                print("Invalid Input!")
                continue

        elif command[0] in {"BUY", "SELL"} and command[2] in {"LMT", "MKT"}:
            try:
                Type = str(command[0])
                share_name = str(command[1]) 
                limit = str(command[2])
                qty = int(command[-1])

                qty = int(qty)

                assert(qty>0)
            except ValueError:
                print("Invalid Input!")
            except AssertionError:
                print("Qty of shares must be greater than 0.")
                continue
            except IndexError:
                print("Invalid Input!")
                continue

            new_quote = quote(command[1])
            bid[share_name] = new_quote

            if command[2] == "LMT":
                try:
                    assert(len(command) == 5)
                    price = command[-2]
                    price  = float(price.strip('$'))
                    assert(price >= 0)
                except:
                    print("invalid price for limit order")
                    continue
                new_order = orders(Type, share_name, limit, price, qty)
            else:
                new_order = orders(Type, share_name, limit, None, qty)
            new_order.print_mes()
            
            if Type == "BUY":
                buy_orders.append(new_order)
            else:
                sell_orders.append(new_order)
            order_list.append(new_order)
            resolve_order(order_list, buy_orders, sell_orders)

        else:
            print("Invalid Input!")
    except:
        print("Invalid Input!")