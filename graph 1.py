import csv
import numpy as np
from bokeh.plotting import figure, show
from collections import OrderedDict


data = open("Monthly.csv")
data_proc = csv.reader(data)

header = next(data_proc)

procedData = []

for line in data_proc:
    try:
        if line[11] == "-":
            raise Exception()

        lineProcedData = [line[1].strip(), line[2].strip(), line[8].strip(), line[11].strip()]
    except: continue

    procedData.append(lineProcedData)

ADdict = {}
AJdict = {}
DBdict = {}
RAdict = {}
SHdict = {}

for entry in procedData:
    date = entry[2] + " " + entry[1]

    if entry[0] == "Abu Dhabi":
        if date in ADdict:
            ADdict[date].append(float(entry[3]))
        else:
            ADdict[date] = [float(entry[3])]
    elif entry[0] == "Ajman":
        if date in AJdict:
            AJdict[date].append(float(entry[3]))
        else:
            AJdict[date] = [float(entry[3])]
    elif entry[0] == "Dubai":
        if date in DBdict:
            DBdict[date].append(float(entry[3]))
        else:
            DBdict[date] = [float(entry[3])]
    elif entry[0] == "Ras Al-Khaimah":
        if date in RAdict:
            RAdict[date].append(float(entry[3]))
        else:
            RAdict[date] = [float(entry[3])]
    elif entry[0] == "Sharjah":
        if date in SHdict:
            SHdict[date].append(float(entry[3]))
        else:
            SHdict[date] = [float(entry[3])]

for entry in ADdict:
    ADdict[entry] = np.mean(ADdict[entry])
for entry in AJdict:
    AJdict[entry] = np.mean(AJdict[entry])
for entry in DBdict:
    DBdict[entry] = np.mean(DBdict[entry])
for entry in RAdict:
    RAdict[entry] = np.mean(RAdict[entry])
for entry in SHdict:
    SHdict[entry] = np.mean(SHdict[entry])

print(ADdict)

sorted_dataAD = OrderedDict(sorted(ADdict.items(), key=lambda x: (int(x[0].split()[1]), ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'August', 'Sept.', 'Oct.', 'Nov.', 'Dec.'].index(x[0].split()[0]))))

dates = list(sorted_dataAD.keys())
values = list(sorted_dataAD.values())

p = figure(x_range=dates, height=800, width=1500, title="UAE Air Quality from Jan. 2013 to Dec. 2015", x_axis_label='Date', y_axis_label='Inhalable Particulate Matter Concentration  (PM-10) (µg/m³)')

p.line(x=dates, y=values, line_width=2, legend_label="Abu Dhabi")

sorted_dataDB = OrderedDict(sorted(DBdict.items(), key=lambda x: (int(x[0].split()[1]), ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'August', 'Sept.', 'Oct.', 'Nov.', 'Dec.'].index(x[0].split()[0]))))

dates = list(sorted_dataDB.keys())
values = list(sorted_dataDB.values())

d = np.array(dates)
v = np.array(values)

p.line(x=dates, y=values, line_width=2, color="red", legend_label="Dubai")


#x = np.linspace(x_min, x_max, 1000)

#fig.line(x, c + m * x)

sorted_dataAJ = OrderedDict(sorted(AJdict.items(), key=lambda x: (int(x[0].split()[1]), ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'August', 'Sept.', 'Oct.', 'Nov.', 'Dec.'].index(x[0].split()[0]))))

dates = list(sorted_dataAJ.keys())
values = list(sorted_dataAJ.values())

p.line(x=dates, y=values, line_width=2, color="purple", legend_label="Ajman")

sorted_dataSH = OrderedDict(sorted(SHdict.items(), key=lambda x: (int(x[0].split()[1]), ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'August', 'Sept.', 'Oct.', 'Nov.', 'Dec.'].index(x[0].split()[0]))))

dates = list(sorted_dataSH.keys())
values = list(sorted_dataSH.values())

p.line(x=dates, y=values, line_width=2, color="black", legend_label="Sharjah")

sorted_dataRA = OrderedDict(sorted(RAdict.items(), key=lambda x: (int(x[0].split()[1]), ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'August', 'Sept.', 'Oct.', 'Nov.', 'Dec.'].index(x[0].split()[0]))))

dates = list(sorted_dataRA.keys())
values = list(sorted_dataRA.values())

p.line(x=dates, y=values, line_width=2, color="green", legend_label="Ras Al-Khaimah")

p.legend.title = "Emirates Legend"



show(p)