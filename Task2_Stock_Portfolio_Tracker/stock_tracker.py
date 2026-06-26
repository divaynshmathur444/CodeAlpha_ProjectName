# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 330,
    "AMZN": 190
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

num_stocks = int(input("Enter the number of different stocks you own: "))

# Open file for writing
file = open("portfolio.txt", "w")

file.write("----- Stock Portfolio -----\n")

for i in range(num_stocks):

    stock_name = input("\nEnter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")

        file.write(f"{stock_name} : {quantity} shares = ${investment}\n")

    else:
        print("Stock not found!")
        file.write(f"{stock_name} : Stock not found\n")

print("\nTotal Investment Value: $", total_investment)

file.write(f"\nTotal Investment = ${total_investment}")

file.close()

print("Portfolio saved successfully in portfolio.txt")