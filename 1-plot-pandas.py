import pandas as pd
import numpy as np
from matplotlib import pyplot as ptl

df = pd.read_csv("./avocado.csv")

chicago = df[ df["region"] == "Chicago" ]

chicago = chicago.set_index("Date")
chicago = chicago.sort_values(by="Date")

print(chicago.head(10))