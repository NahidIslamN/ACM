import pandas as pd
import numpy as np
N=pd.read_csv("Nahid.csv")
print(N.head(2))
x=N["Studnet Name"][2]="Sahibar Azad"
y=N["Studnet Name"][2]
N.to_csv("Nahid.csv")


#accessing part
#print(L.head(1))
#$print(L.tail(2))
#print(L.describe())
