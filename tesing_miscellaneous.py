print(stocks_table.info())
print()
print(stocks_dataframe["Ticker"][64:65])
print()
print(stocks_dataframe[stocks_dataframe["Ticker"].str.contains("BRK.B")])
print()
print(batch_stocks_dataframe["Ticker"][63:66])
print()
print(batch_stocks_dataframe["Ticker"][64:65])
print()
print(batch_stocks_dataframe[stocks_dataframe["Ticker"].str.contains("BRK.B")])