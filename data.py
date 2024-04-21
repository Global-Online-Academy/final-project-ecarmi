from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange
import pandas
from bokeh.io import output_notebook
output_notebook()  

#monthly = open("Monthly.csv", "r")
#annual = open("Annual.csv", "r")

annual = pandas.read_csv('Annual.csv', usecols=["Emirate_En","Year", "Value"])
lena = len(annual.index)
monthly = pandas.read_csv('Monthly.csv', usecols=["Emirate_En","Year","Month_En", "Value"])
lenm = len(monthly.index)

emiratesName = [ "Abu Dhabi  ", "Dubai", "Sharjah", "Ajman", "Ras Al-Khaimah ", "Fujairah"]

emirates = [annual.at[i, "Emirate_En"] for i in range(lena)]
values = [annual.at[i, "Value"] for i in range(lena)]
time = [annual.at[i, "Year"] for i in range(lena)]


AbuDhabi = [values[i] for i in range(lena) for i in range(lena) if annual.at[i, "Emirate_En"] == "Abu Dhabi  " and values[i] != "-"]
Dubai =  [values[i] for i in range(lena) if annual.at[i, "Emirate_En"] == "Sharjah" and values[i] != "-"]
Sharjah = [values[i] for i in range(lena) if annual.at[i, "Emirate_En"] == "Dubai" and values[i] != "-"]
Ajman = [values[i] for i in range(lena) if annual.at[i, "Emirate_En"] == "Ajman" and values[i] != "-"]
RasAlKhaimah = [values[i] for i in range(lena) if annual.at[i, "Emirate_En"] == "Ras Al-Khaimah " and values[i] != "-"]
Fujairah = [values[i] for i in range(lena) if annual.at[i, "Emirate_En"] == "Fujairah" and values[i] != "-"]

abuDict = {t:v for (t,v, e) in zip(time, values, emirates) if e == "Abu Dhabi  " and v != "-"}
sharjahDict = {t:v for (t,v, e) in zip(time, values, emirates) if e == "Sharjah" and v != "-"}
dubaiDict = {t:v for (t,v, e) in zip(time, values, emirates) if e == "Dubai" and v != "-"}
ajmanDict = {t:v for (t,v, e) in zip(time, values, emirates) if e == "Ajman" and v != "-"}
rasDict = {t:v for (t,v, e) in zip(time, values, emirates) if e == "Ras Al-Khaimah " and v != "-"}
fujairahDict = {t:v for (t,v, e) in zip(time, values, emirates) if e == "Fujairah" and v != "-"}

print(ajmanDict)
for i in range(273):
    #print(emirates[i], time[i], values[i])
    None
#emirates = [ AbuDhabi, Dubai, Sharjah, Ajman, RasAlKhaimah, Fujairah ]


'''data = {"Emirates" : emiratesName,
        "2006": [values]

}'''

data = {'emirates': emirates, 'years': [str(year) for year in time], 'values': values}
x = [(emirate, year) for emirate, year in zip(data['emirates'], data['years'])]
counts = data['values']

source = ColumnDataSource(data=dict(x=x, counts=counts))

# Setting up the figure
p = figure(x_range=FactorRange(*x), height=350, title="Values by Emirates and Year",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

# Display the plot
show(p)

'''with open('Monthly.csv') as csv_file:
    m = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in m:
        print(', '.join(row))'''


'''monthlyLines = [i for i in monthly.readlines()]
print(monthlyLines)
actors = []
for i in monthlyLines:
    i = i.strip()
    j = i.split("|")
    k = j[3]
    if len(j) >= 3:
        if (",") in k:
            l = k.split(",")
            for m in l:
                actors.append(m)
        else:
            actors.append(k)'''