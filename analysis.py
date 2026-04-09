import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 900, 500]}
df = pd.DataFrame(data)
print("Продажі в містах: ")
print(df)
print("Середнє значення: ", df["sales"].mean())