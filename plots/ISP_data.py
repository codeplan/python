#!/usr/bin/env python

### This uses plotly library and generates a visualization for the Market share
### of top ISP in india. For it uses Top_ISP_Shares.csv from data.gov.in.

import csv
import plotly as plt
import plotly.graph_objs as go

f = open(r'Top_ISP_Shares.csv')
buff_main = csv.DictReader(f)
#buff_main = csv.reader(f)

plot_data = []
isps = []
data = {}
years = [2009,2010,2011,2012,2013]

for row in buff_main:
    if not (('NA' in row.values()) or (0 in row.values())):
       isps.append(row['ISP'])
       share = []
       share.append(row['2009 - Share (%)'])
       share.append(row['2010 - Share (%)'])
       share.append(row['2011 - Share (%)'])
       share.append(row['2012 - Share (%)'])
       share.append(row['2013 - Share (%)'])
       data[row['ISP']] = share
        
#print(isps)
#print(data)


#print(data.keys())
for keys in data:
    plot_data.append(go.Scatter(
        x = years,
        y=data[keys],
        mode = 'lines+markers',
        name = keys,
        connectgaps=True
        ))
    
#print(plot_data)
layout = dict(title = 'Total market share of ISPs in India',
              xaxis = dict(
                  title = 'Year',
                  dtick=1,
                  showline=True,
                  showgrid=False,
                  showticklabels=True),
              yaxis = dict(title = 'Share in %',
                            showgrid=True,
                            zeroline=False,
                            showline=True,
                            showticklabels=True))

fig = dict(data=plot_data, layout=layout)

plt.offline.plot(fig, filename=r'ISP_Shares.html')
