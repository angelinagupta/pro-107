import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    daysPresent = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks"]))
            daysPresent.append(float(row["Days Present"]))
    return{"x" : marks, "y" : daysPresent}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between marks vs days present is: ", corelation[0,1])

def main():
    data_path = "D:\code\python\pro-107\Student.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

main()