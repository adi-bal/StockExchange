class quote:        #class to store quotes of each unique quote 
    def __init__(self, share_name):
        self.share_name = share_name
        self.bid = 0.0
        self.ask = 0.0
        self.last = 0.0
    
    def get_quote(self):    #perfroms linear search on the buy and sell order list to retrieve bid and ask
        find_bid = 0
        for buy in buy_orders:
            if(buy.share_name == self.share_name and buy.price is not None and buy.status != "FILLED"):
                find_bid = max(find_bid, buy.price)
        
        find_ask = float("inf")
        for sell in sell_orders:
            if(sell.share_name == self.share_name and sell.price is not None and sell.status != "FILLED"):
                find_ask = min(find_ask, sell.price)
        self.bid = find_bid

        if find_ask != float("inf"):
            self.ask = find_ask
    
    def view(self):
        self.get_quote()
        print("{} BID: ${} ASK: ${} LAST: ${}".format(self.share_name, self.bid, self.ask, self.last))