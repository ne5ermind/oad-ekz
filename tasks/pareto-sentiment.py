import pandas as pd
import plotly.graph_objects as pg
from plotly.subplots import make_subplots

# %%

data = pd.read_csv("~/py-scripts/oad/sentimentdataset.csv")
data
# %%

data.columns
# %%

df = pd.DataFrame()
df["user"] = data["User"]
df["engagement"] = data["Likes"] + data["Retweets"]
df = df.groupby(by="user").sum().sort_values(by="engagement", ascending=False)
df
# %%

total_engagement = sum(df["engagement"])
df["cumsum"] = df["engagement"].cumsum()
df["from-total"] = df["cumsum"] / total_engagement * 100
df
# %%

result = df[df["from-total"] <= 80]
result
# %%

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    pg.Bar(
        x=result.index, y=result["engagement"], name="взаимодействие с пользователем"
    ),
    secondary_y=False,
)
fig.add_trace(
    pg.Scatter(x=result.index, y=result["from-total"], name="Накопительная сумма"),
    secondary_y=True,
)
fig.update_xaxes(tickvals=result.index, tickfont=dict(size=6), tickangle=45)

fig.show(renderer="browser")
# %%
