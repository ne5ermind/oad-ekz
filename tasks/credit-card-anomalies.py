import pandas as pd
import matplotlib.pyplot as plt

# %%

data = pd.read_csv("~/py-scripts/oad/credit_card_transactions.csv")
data
# %%

data.columns
# %%

data_amt = data["amt"]
data_amt
# %%

q1 = data_amt.quantile(0.25)
q3 = data_amt.quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

anomalies = data_amt[(data_amt < lower_bound) | (data_amt > upper_bound)]
anomalies

# %%

plt.boxplot(data_amt)
plt.ylabel("значения")
plt.title("boxplot")
plt.show()
# %%
