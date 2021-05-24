import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
df = pd.read_csv("StudentsPerformance.csv")
# fig = ff.create_distplot([df["math score"].tolist()], ["math"], show_hist = False)
# fig.show()
math_list = df["math score"].to_list()
mean = statistics.mean(math_list)
std_dev = statistics.stdev(math_list)
median = statistics.median(math_list)
mode = statistics.mode(math_list)
print("The mean is: ", mean)
print("The standard deviation is: ", std_dev)
print("The median is: ", median)
print("The mode is: ", mode)
first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)
data_first_std_dev = [result for result in math_list if result > first_std_dev_start and result < first_std_dev_end]
data_second_std_dev = [result for result in math_list if result > second_std_dev_start and result < second_std_dev_end]
data_third_std_dev = [result for result in math_list if result > third_std_dev_start and result < third_std_dev_end]
print("{}% of data on First Standard Deviation".format( len(data_first_std_dev)*100.0/len(math_list)))
print("{}% of data on Second Standard Deviation".format( len(data_second_std_dev)*100.0/len(math_list)))
print("{}% of data on Third Standard Deviation".format( len(data_third_std_dev)*100.0/len(math_list)))