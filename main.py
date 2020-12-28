import pandas as pd
import numpy as np
from os import listdir
frames = []
# just put the directories of the phases you want to analyze in a "data" directory
for n in listdir("data"):
    frames.append(pd.read_stata("data/" + n + "/" + n + ".dta"))

data = pd.concat(frames)
print(data["hispanic"])
latinos = data.loc[data["hispanic"].isin(["Mexican", "Cuban", "Argentinian", "Colombian", "Ecuadorian", "Salvadorean", "Guatemalan", "Nicaraguan", "Panamanian", "Peruvian", "Venezuelan", "Other Hispanic", "Puerto Rican"])]
voting_latinos = latinos.loc[latinos["registration"].isin(["Registered"])]

trumpbiden = pd.get_dummies(voting_latinos["trump_biden"])
trumpsanders = pd.get_dummies(voting_latinos["trump_sanders"])
print(trumpsanders["Bernie Sanders"].value_counts())
print(trumpbiden["Joe Biden"].value_counts())