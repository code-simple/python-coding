import os

# s = "file.exe"

# f_name = s.split('.')[0]
# f_ext = s.split('.')[1]
# print(f_name+'.'+f_ext)
# print("Working in Nano")


# Convert any string to show only 2 decimal 
# First convert to float, if it has comma replace it
# 
gold_price = "1,680.5345"
print(f"XAUUSD : {round(float(gold_price.replace(',', '')),2)}")
