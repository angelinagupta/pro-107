import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["sleep"]))
    return{"x" : coffee, "y" : sleep}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between coffee vs days present is: ", corelation[0,1])

def main():
    data_path = "D:\code\python\pro-107\coffee_sleep.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

main()