portfolio_value = input("Enter your portfolio value: ")

try:
  portfolio_value_float = float(portfolio_value)

except:
  print("You have not entered a numerical value!")
  portfolio_value = input("Enter your portfolio value: ")

import math

position_size = float(portfolio_value) / len(batch_stocks_dataframe.index)

print("Batch Dataframe position size:", position_size)
print("Batch Dataframe index info:", batch_stocks_dataframe.index)
print("Batch DataFrame index length:", len(batch_stocks_dataframe.index))

for index in range(0, len(batch_stocks_dataframe["Ticker"])-1):

  batch_stocks_dataframe.loc[index, "Shares to Buy"] = math.floor(position_size / batch_stocks_dataframe["Price"][index])

print()

print(batch_stocks_dataframe)
