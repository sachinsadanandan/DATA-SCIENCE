import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('9_data.csv')
country_data = df["country"]
medal_data = df["gold_medal"]
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show()