from numpy import False_
import pandas as pd 
import csv
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("./height-weightData.csv")

height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

height_stdev = statistics.stdev(height_list)
weight_stdev = statistics.stdev(weight_list)

print("mean, median and mode of Height is {},{} and {} respectively" .format(height_mean,height_median,height_mode))
print("mean, median and mode of Weight is {},{} and {} respectively" .format(weight_mean,weight_median,weight_mode))

print("Standard Deviation of Height Data",height_stdev)
print("Standard Deviation of Weight Data",weight_stdev)


fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist= False)
fig.show()

fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist= False)
fig.show()