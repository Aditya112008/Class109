import random 
import plotly.express as px 
import plotly.figure_factory as ff
import statistics


dice_result = []
count = []
for i in range(0,1000):

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    #print(dice1,dice2)
    dice_result.append(dice1+dice2)
    count.append(i)

mean = sum(dice_result)/len(dice_result)
print("mean of this data is {}".format(mean))

median = statistics.median(dice_result)
print("median of this data is {}".format(median))

mode = statistics.mode(dice_result)
print("mode of this data is {}".format(mode))
print("mode of this data is " , mode )

standard_deviation = statistics.stdev(dice_result)
print("standard deviation d of this data is {}".format(standard_deviation))

first_std_deviation_start, first_std_deviation_end = mean - standard_deviation, mean + standard_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*standard_deviation), mean + (2*standard_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*standard_deviation), mean + (3*standard_deviation)

list_of_data_within_first_standard_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_second_standard_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_third_standard_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1st std_deviation".format(len(list_of_data_within_first_standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2nd std_deviation".format(len(list_of_data_within_second_standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3rd std_deviation".format(len(list_of_data_within_third_standard_deviation)*100.0/len(dice_result)))


#fig = px.bar(x = dice_result,y = count)
fig = ff.create_distplot([dice_result],["Result"])
fig.show()
