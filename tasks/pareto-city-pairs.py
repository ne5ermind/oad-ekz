import pandas as pd
import plotly.express as px

# %%

data = pd.read_csv("~/py-scripts/oad/city_pairs.csv")
data
# %%

data.columns
# %%

data_weight = pd.DataFrame()
data_weight["port"] = data["AustralianPort"]
data_weight["weight_sum"] = data["Freight_Total_(tonnes)"] + data["Mail_Total_(tonnes)"]
data_weight
# %%

data_weight = data_weight.groupby("port").sum()
data_weight = data_weight.sort_values(by="weight_sum", ascending=False)
data_weight
# %%

data_weight["cumsum"] = data_weight["weight_sum"].cumsum()
sum_total_weight = sum(data_weight["weight_sum"])
data_weight["precents"] = data_weight["cumsum"] / sum_total_weight * 100
data_weight
# %%

data_weight[data_weight["precents"] <= 80]
# %%
