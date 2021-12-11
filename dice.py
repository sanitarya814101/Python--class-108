import plotly.express as px
import pandas as pd
import csv
import plotly.figure_factory as ff
import numpy as np

df = pd.read_csv('data.csv')

# Height
# fig = ff.create_distplot([df["Height(Inches)"].tolist()], [
#                         "Height"], show_hist=False)

# Weight
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()], [
                         "weight"], show_hist=False)


fig.show()
