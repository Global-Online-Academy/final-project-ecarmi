from collections import defaultdict
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange
import pandas

annual = pandas.read_csv('Annual.csv', usecols=["Emirate_En","Year", "Value"])
lena = len(annual.index)
monthly = pandas.read_csv('Monthly.csv', usecols=["Emirate_En","Year","Month_En", "Value"])
lenm = len(monthly.index)

emiratesName = [ "Abu Dhabi  ", "Dubai", "Sharjah", "Ajman", "Ras Al-Khaimah ", "Fujairah"]
yearsName = ["2006","2007","2008","2009","2010","2013","2014","2015","2016"]

emirates = [annual.at[i, "Emirate_En"] for i in range(lena)]
years = [annual.at[i, "Year"] for i in range(lena)]
values = [annual.at[i, "Value"] for i in range(lena) if annual.at[i, "Value"] .isdigit()]


data_by_year = defaultdict(lambda: defaultdict(list))
for emirate, year, value in zip(emirates, years, values):
    if value != "-":
        data_by_year[year][emirate].append(int(value))  
print(data_by_year)
sorted_emirates = sorted(set(emirates))  

data = {"emirates" : emiratesName}
for year, emirates_dict in data_by_year.items():
    data[year] = [sum(emirates_dict[emirate])/len(emirates_dict[emirate]) if emirate in emirates_dict else None for emirate in sorted_emirates]

x = [ (emirate,  year) for emirate in emiratesName for year in yearsName ]
counts = sum(zip(data[2013], data[2014], data[2015], data[2016], data[2006], data[2007],data[2008], data[2009], data[2010]),()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), height=750,width = 1400, title="Amount of PM-10 in Emirates Annually",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source)


p.y_range.start = 0
p.x_range.range_padding = .00001
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None
p.yaxis.axis_label = "Inhalable Particulate Matter Concentration  (PM-10) [µg/m³]"
p.xaxis.axis_label = "Emirates of UAE"


show(p)