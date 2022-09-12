import pandas as pd

csv_file = "/home/administrator/Desktop/python-folder/pandas/sample.csv"

l = pd.read_csv(csv_file).to_numpy()


name_list = []
age_list = []
state_list = []
point_list = []

for i in l:
    name_list.append(i[0])
    age_list.append(i[1])
    state_list.append(i[2])
    point_list.append(i[3])

print(state_list)