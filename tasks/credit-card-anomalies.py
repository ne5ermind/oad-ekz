import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.ensemble import IsolationForest

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

temp = data[["category", "amt"]]

data_enc = pd.get_dummies(temp, columns=["category"])

model = IsolationForest(contamination=0.05, random_state=67)

data_enc["anomaly"] = model.fit_predict(data_enc)
# %%

temp = data_enc.columns[1:-1]

dummy_cols = data_enc[list(temp)]

data_enc["category"] = pd.from_dummies(dummy_cols)
data_enc = data_enc.drop(columns=temp)

anomalies_iso = data_enc[data_enc["anomaly"] == -1]
anomalies_iso
# %%

fig = px.strip(
    data_enc,
    x="anomaly",
    y="amt",
    color="category",
    hover_data=["category", "amt"],
    title="анализ аномалий в банковских переводах по типам покупок",
)
fig.update_layout(yaxis_type="log")
fig.show()
# %%
