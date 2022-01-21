import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#plotting the graph
# fig = ff.create_distplot([data], ["Math Scores"], show_hist= False)
# fig.show()

#calculating the mean and standard deviation of the population data
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
# print("mean of popultion:-,mean")
# print("Standard deviation of popultion:- ",std_deviation)



## code to find the mean of 100 data points 1000 times
#function to get the mean of the given data samples
# pass the number of data points you want as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
        mean = statistics.mean(dataset)
        return mean



# Pass the number of time you want the mean of the data points as a parameter in range i n a loop
mean_list = []
for i in range(0,1000)
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)


    std_deviation = statistics.stdev(mean_list)

    #plotting the mean of the sampling

    first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
    second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
    third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

    #finding the standard deviation starting and ending values
    #plotting the graph with traces

    #finding the mean of the THIRD data (STUDENS WHO GOT FUNSHEET) and plotting it on the plot
    df = pd.read_csv("data3.csv")
    data = df["Math_score"].tolist()
    mean_of_sample3 = statistics.mean(data)
    print("mean of sample3:- ", mean_of_sample3)
    fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN OF STUDENT WHO GOT FUNSHEETS"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
    fig.show()