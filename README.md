# Simple Stock Exchange 
The simple Stock exchange is a mini pre - interview project created for Hedge Fund Capital Management

# Getting Started 

1. Make sure thay you have python3 installed and open the directory in your command line or terminal.

2. Run the main.py file to execute the programme 

```
$ python3 main.py
```
3. To run the unit tests for the controller function execute 

```
$ python3 test_resolve_order.py
```

ond

```
$ python3 test_transfer_share.py
```

4. To quit the main programma anytime type QUIT (case sensitive) after the action prompt

# Description 
1. The stock Exchange supports market and limit buy/sell orders, every time a new order is placed the programme automatically runs the resolve order function.
2. Market prices are assumed to be 0 by default if there are no active orders. 
3. All commands are case sensitive, and must be capitalised.
4. User input is prefixed by Action. 

# Sample run of the programme

```
Action: BUY SNAP LMT $30 100
You have placed a limit buy order for 100 SNAP shares at $30.00 each.

Action: VIEW ORDERS
1. SNAP LMT BUY $30.00 0/100 PENDING

Action: BUY FB MKT 20
You have placed a market order for 20 FB shares.

Action: VIEW ORDERS
1. SNAP LMT BUY $30.00 0/100 PENDING
2. FB MKT BUY 0/20 PENDING

Action: SELL FB LMT $20.00 20
You have placed a limit sell order for 20 FB shares at $20.00 each

Action: VIEW ORDERS
1. SNAP LMT BUY $30.00 0/100 PENDING
2. FB MKT BUY $20.00 20/20 FILLED
3. FB LMT SELL $20.00 20/20 FILLED

Action: SELL SNAP LMT $30.00 20
You have placed a limit sell order for 20 SNAP shares at $30.00 each

Action: VIEW ORDERS
1. SNAP LMT BUY $30.00 20/100 PARTIAL
2. FB MKT BUY $20.00 20/20 FILLED
3. FB LMT SELL $20.00 20/20 FILLED
4. SNAP LMT SELL $30.00 20/20 FILLED

Action: SELL SNAP LMT $31.00 10
You have placed a limit sell order for 10 SNAP shares at $31.00 each

Action: QUOTE SNAP
SNAP BID: $30.00 ASK: $31.00 LAST: $30.00
```
