from collections import defaultdict
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange
import pandas
import datetime
import numpy as np

dt = datetime.datetime
monthly = pandas.read_csv('Monthly.csv', usecols=["Emirate_En","Year","Month_En", "Value"])
lenm = len(monthly.index)

years = [monthly.at[i, "Year"] for i in range(lenm) if monthly.at[i, "Emirate_En"] == "Abu Dhabi  "]
months = [monthly.at[i, "Month_En"] for i in range(lenm) if monthly.at[i, "Emirate_En"] == "Abu Dhabi  " ]
dates = [[monthly.at[i, "Year"], monthly.at[i, "Month_En"]] for i in range(lenm) if monthly.at[i, "Value"] .isdigit() and monthly.at[i, "Emirate_En"] == "Abu Dhabi  "]
for i in range(len(dates)):
    m = dates[i][1]
    if "Jan" in m:
        dates[i][1] = 1
    elif "Feb" in m:
        dates[i][1]= 2
    elif "Mar" in m:
        dates[i][1]= 3
    elif "Apr" in m:
        dates[i][1]= 4
    elif "May" in m:
        dates[i][1]= 5
    elif "Jun" in m:
        dates[i][1]= 6
    elif "Jul" in m:
        dates[i][1]= 7
    elif "Aug" in m:
        dates[i][1]= 8
    elif "Sep" in m:
        dates[i][1]= 9
    elif "Oct" in m:
        dates[i][1]= 10
    elif "Nov" in m:
        dates[i][1]= 11
    elif "Dec" in m:
        dates[i][1]= 12
       
dates = [dt(int(i[0]),int(i[1]), 1) for i in dates]
#print(date for date in dates)
values = [monthly.at[i, "Value"] for i in range(lenm) if monthly.at[i, "Value"].isdigit()]

combined = [(monthly.at[i, "Year"], monthly.at[i, "Month_En"], monthly.at[i, "Value"])for i in range(lenm) if monthly.at[i, "Value"] .isdigit()]
data = defaultdict(lambda: defaultdict(list))
for year, month, value in zip(years, months, values):
    data[year][month].append(int(value))  
#print(data)
datesdata = defaultdict(lambda: defaultdict(list))
for dates, value in zip(dates, values):
    datesdata[dates.year][dates.month].append(int(value))  
newvalues = {}
monthsarr = [1,2,3,4,5,6,7,8,9,10,11,12]
#print(datesdata)
for year, month in datesdata.items():
   tuple(datesdata[year])
  # print(month[monthsarr]) for month in monthsarr)
  #newvalues[year] = [(np.mean(month[monthsarr]) for month in monthsarr)]

   newvalues[year] = [np.mean(month[monthsarr]) for month in monthsarr]
  # print(datesdata[year][month])
    #print(month, "sfnsanfoisfsf")
    #print(data[year]["Jan."] )
   # newvalues.append(np.mean(data[year]]))
print(newvalues)
#for year, month in datesdata.items():
  # print(datesdata[year])

p = figure(title="Amount of PM-10 in Emirates Annually", x_axis_label="Time", y_axis_label="Inhalable Particulate Matter Concentration  (PM-10) [µg/m³]"
           ,x_axis_type="datetime", y_range = (0,200))

p.scatter(dates, values)
p.line(dates, values, color="navy")

#show(p)