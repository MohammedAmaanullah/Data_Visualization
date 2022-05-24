from google.colab import files 
data_to_load=files.upload()

import pandas as pd
import plotly.express as pe
df = pd.read_csv("covid_data.csv")
fig= px.scatter(df, x="date", y="cases")
fig.show()