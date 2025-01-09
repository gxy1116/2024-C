import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Wimbledon_featured_matches.csv")
# print(data)

# 独热编码列: 'serve_width', 'winner_shot_type'
for column in ['serve_width', 'winner_shot_type']:
    insert_loc = data.columns.get_loc(column)
    data = pd.concat([data.iloc[:,:insert_loc], pd.get_dummies(data.loc[:, [column]]), data.iloc[:,insert_loc+1:]], axis=1)
# Replace 'NCTL' with 0 and 'CTL' with 1 in 'serve_depth' column
data['serve_depth'] = data['serve_depth'].replace({'NCTL': 0, 'CTL': 1})
# Replace 'ND' with 0 and 'D' with 1 in return_depth
data['return_depth'] = data['return_depth'].replace({'ND': 0, 'D': 1})
# Fill missing values in speed_mph with 0
data['speed_mph'].fillna(0, inplace=True)

# Add a column named 'momentum' with all values set to 0
data['momentum'] = np.nan
m,n = data.shape
dic_column = dict(zip(data.columns, range(n)))
new_match_start = []
for i in range(m):
    if data.iloc[i,dic_column["elapsed_time"]] == "00:00:00":
        new_match_start.append(i)
new_match_start.append(m-1)
print(new_match_start)
for i in range(len(new_match_start)-1):
    data.iloc[new_match_start[i], dic_column['momentum']] = 0
    start = new_match_start[i]
    end = new_match_start[i+1]
    for j in range(start+1, end+1):
        if data.iloc[j, dic_column['server']] == data.iloc[j-1, dic_column['point_victor']]:
            data.iloc[j, dic_column['momentum']] = 1
        else:
            data.iloc[j, dic_column['momentum']] = 0
data.iloc[new_match_start[-1], dic_column['momentum']] = 0