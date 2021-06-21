import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    ice_cream_sales = []
    temperature = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))
    return{"x" : temperature, "y" : ice_cream_sales}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between temperature vs ice-cream sales is: ", corelation[0,1])

def main():
    data_path = "D:\code\python\pro-107\Temperature.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

main()