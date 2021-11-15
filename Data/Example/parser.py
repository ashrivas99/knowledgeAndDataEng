import pandas as pd

COLUMN_LIST = ["Countries"]
COUNTRY_LIST_PLAYERS = ["country_of_birth", "country_of_citizenship"]
df_who = pd.read_csv("./Datasets/WHOdata.csv", usecols=COLUMN_LIST)
df_GDP = pd.read_csv("./Datasets/GDPdata.csv", usecols=COLUMN_LIST)
df_countries = pd.read_csv("./Datasets/players.csv", usecols=COUNTRY_LIST_PLAYERS)


set1 = set(df_who["Countries"].apply(lambda x: x.lower()))
set2 = set(df_GDP["Countries"].apply(lambda x: x.lower()))
set3 = set(df_countries["country_of_citizenship"].apply(lambda x: x.lower()))

intersection_set = set1.intersection(set2).intersection(set3)
print(intersection_set)
