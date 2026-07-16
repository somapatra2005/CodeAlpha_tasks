stock_prices={
    "AAPL":180,
    "TSLA":250,
    "GOOGLE":150,
    "AMZN":130,
    "MSFT":320,
    
}

stock_name=input("Enter stock name:").upper()
quantity = int(input("Enter  Quantity:"))

if stock_name in stock_prices:
    total =stock_prices[stock_name]* quantity
    print("Total investment value= ",total)
else:
    print("stock not found")
    
    