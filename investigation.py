import networkx as nx
import pandas as pd
import itertools
import json
import matplotlib.pyplot as plt


path = '../Data/matrices_julio_csv/matrices_julio/VI_J00.csv'
data = pd.read_csv(path, delimiter=",")
data.columns = ["Origin", "Destination", "Year", "Month","Day", "Period", "Mode",
                "Distance", "Residence","Activity_Source", "Activity_Destination", 
                "Travelers", "Travelers -km "]

plt.plot([1,2,3,4,5,6,7,8,9,10],data[ "Travelers"][0:10])