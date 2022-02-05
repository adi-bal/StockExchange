class orders:       #to store buy/sell orders
    def __init__(self, type, share_name, limit, price , qty):
        self.type = type
        self.share_name = share_name
        self.limit = limit
        self.price = price      #price is stored as none for market orders
        self.filled = 0
        self.qty = qty
        self.status = "PENDING"
    def print_mes(self):
        l = "limit" if self.limit == "LMT" else "market"
        a = "buy" if self.type == "BUY" else "sell"
        b = self.qty
        c = self.share_name 
        d = self.price
        if d is not None:   #produces different messsages based on limit and market orders 
            print("You have placed a {} {} order for {} {} shares at ${} each.".format(l,a,b,c,d))
        else:
            print("You have placed a {} {} order for {} {} shares.".format(l,a,b,c,))