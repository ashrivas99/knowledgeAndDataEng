import pandas as pd
from pprint import pprint

COLUMN_LIST = ["Countries", "Country"]
COUNTRY_LIST_PLAYERS = ["country_of_birth", "country_of_citizenship"]
df_who = pd.read_csv("Data/Datasets/WHOdata.csv", usecols=["Countries"])
df_GDP = pd.read_csv("Data/Datasets/GDPdata.csv", usecols=["Country"])
df_countries = pd.read_csv("Data/Datasets/players.csv", usecols=COUNTRY_LIST_PLAYERS)

set1 = set(df_who["Countries"].apply(lambda x: x.lower()))
set2 = set(df_GDP["Country"].apply(lambda x: x.lower()))
set3 = set(df_countries["country_of_citizenship"].apply(lambda x: x.lower()))
set4 = set(df_countries["country_of_birth"].apply(lambda x: x.lower()))

intersection_set = set1.intersection(set2).intersection(set3)  # .intersection(set4)
# pprint(len(intersection_set))
# pprint(intersection_set)
pprint(set4)
# pprint(set2.difference(intersection_set))
