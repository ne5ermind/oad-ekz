import pandas as pd
import plotly.express as px
# %%

data = pd.read_excel('~/py-scripts/oad-ekz/Время простоя.xlsx')
data
# %%

data.columns
# %%

time_parts = data['Время простоя под последней операцией (сутки:часы:минуты)'].str.split(':', expand=True).astype(int)
time_parts
# %%

df = pd.DataFrame()

df['station'] = data['Станция операции']
df['tot-wait-time'] = time_parts[0] * 24 + time_parts[1] + time_parts[2] / 60

df = df.groupby(by='station', as_index=False).sum()
df
# %%

q1 = df['tot-wait-time'].quantile(0.25)
q3 = df['tot-wait-time'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

anomalies = df[(df['tot-wait-time'] < lower_bound) | (df['tot-wait-time'] > upper_bound)].reset_index(drop=True)
anomalies.sort_values('tot-wait-time', ascending=False).reset_index(drop=True)
# %%

fig = px.box(data_frame=df, y='tot-wait-time', hover_data=['station'], title='Анализ аномалий среди времени простоя вагонов на станциях')
fig.show(renderer='browser')
# %% [markdowm]

# Из 267 станций 44 имеют аномально высокие значения по простою поездов, а именно - Залари, Шедок, Илецк 1, Антропшино, Киташ, Металлургическая, Кунгур, Наушки, Павшино, Черный Мыс, Карбышево, Самур, Верхний Баскунчак, Колпино, Махачкала, Промгипсовая, Игумново, Надеждинская итд.
# Полный список содержится в 5 блоке кода
# %%

