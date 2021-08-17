!pip install xlsxwriter
import xlsxwriter

excel_writer = pandas.ExcelWriter("stocks.xlsx", engine = "xlsxwriter")

batch_stocks_dataframe.to_excel(excel_writer, sheet_name = "S&P 500 Stocks", index = False)

excel_writer.save()
