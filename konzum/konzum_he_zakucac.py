# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:34:28 2024

@author: Lara Buljan
"""

import plotly
import plotly.graph_objects as go
import plotly.io as pio
#import plotly.dashboard_objs as dashboard_objs
import IPython.display
#from IPyhton.display import Image

from os import listdir
from os.path import isfile, join

import pandas as pd
import numpy as np

def graf(df, name, value_column, yaxis_name, colour, otocni_rad):
    fig = go.Figure()
    
    filtered_temp_df = df[
        (df[name]>=otocni_rad[0]) & 
        (df[name]<=otocni_rad[2])
        ]
    max_value = filtered_temp_df[value_column].max()
    max_index = filtered_temp_df[value_column].idxmax()
    min_value = filtered_temp_df[value_column].min()
    min_index = filtered_temp_df[value_column].idxmin()
    
    fig.add_trace(go.Scatter(
        x=df[name],
        y=df[value_column],
        mode="lines",
        name=name,
        line=dict(color=colour),
        showlegend=True
        ))
    
    fig.add_annotation(
        x=df[name].iloc[max_index], 
        y=max_value, 
        text=f"max: {max_value}",
        font=dict(family='Helvetica', size=14, color=colour),
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-30
        )
    
    fig.add_annotation(
        x=df[name].iloc[min_index], 
        y=min_value,
        text=f"min: {min_value}",
        font=dict(family='Helvetica', size=14, color=colour),
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=30
        )
    
    fig.add_vline(
        x=pd.to_datetime(otocni_rad[0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color=colour
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color=colour
        )
    
    fig.add_annotation(
        x=pd.to_datetime(otocni_rad[0]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {otocni_rad[1]}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color=colour, size=12),
        bordercolor=colour,
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(otocni_rad[2]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {otocni_rad[3]}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color=colour, size=12),
        bordercolor=colour,
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    
    fig.update_layout(
        title=name,
        xaxis_title="Vrijeme",
        yaxis_title=yaxis_name,
        legend_title="Legenda",
        template="plotly_white",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    return fig

   
konzum_path = "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\konzum\\HE_ZAK_TR1_20241204_0910-1710.csv"

zak_tr_df = pd.read_csv(konzum_path, delimiter=";")
zak_tr_df = zak_tr_df.dropna(axis=1, how="all")

column_names = zak_tr_df.columns

column_names = zak_tr_df.columns[::2]
values = zak_tr_df.columns[1::2]
units = ["I [A]", "P [MW]", "Q [Mvar]", "U [kV]", "položaj reg. sklopke", "U [kV]"]
colors = ["blue", "red", "blue", "green", "black", "green"]


# datetime conversion
for name in column_names:
    zak_tr_df[name] = pd.to_datetime(zak_tr_df[name], format="%d.%m.%Y. %H:%M:%S", dayfirst=True)

# float values 
for name in zak_tr_df.columns:
    first_value = zak_tr_df[name].iloc[0]  # Get the first value for type checking
    
    if isinstance(first_value, str):
        zak_tr_df[name] = zak_tr_df[name].str.replace(',', '.').astype(float)
    elif isinstance(first_value, (np.float64, float)):
        print(f"Column '{name}' is already of type float.")
    else:
        print(f"Column '{name}' is of unexpected type: {type(first_value)}")

split_dfs = []
intervals = [("2024-12-04 09:10:00", "2024-12-04 11:00:00"), 
             ("2024-12-04 11:00:00", "2024-12-04 13:00:00"),
             ("2024-12-04 14:15:00", "2024-12-04 15:30:00"),
             ("2024-12-04 16:15:00", "2024-12-04 17:10:00")]

otocni_rad = [("2024-12-04 09:12:58", "HE ZAK 110 METERIZE/2", "2024-12-04 10:20:29", "HE ZAK 110 SP W12"),
              ("2024-12-04 11:48:26", "HE ZAK 110 METERIZE/2", "2024-12-04 12:46:48", "HE ZAK 110 SP W12"),
              ("2024-12-04 14:24:28", "HE ZAK 110 METERIZE/2", "2024-12-04 15:25:27", "HE ZAK 110 SP W12"),
              ("2024-12-04 16:27:27", "HE ZAK 110 METERIZE/2", "2024-12-04 17:03:18", "HE ZAK 220 SP W12")]


column_mapping = {}
for time_col, value_col in zip(column_names, values):
    column_mapping[time_col] = value_col


# Loop through intervals and filter the DataFrame
for start, end in intervals:
    split_data = {}
    start_time = pd.to_datetime(start, format="%Y-%m-%d %H:%M:%S")
    end_time = pd.to_datetime(end, format="%Y-%m-%d %H:%M:%S")

    for time_col, value_col in column_mapping.items():
        mask = (zak_tr_df[time_col] >= start_time) & (zak_tr_df[time_col] <= end_time)
        split_data[time_col] = zak_tr_df[time_col][mask].reset_index(drop=True)
        split_data[value_col] = zak_tr_df[value_col][mask].reset_index(drop=True)
    split_dfs.append(pd.DataFrame(split_data))

# split_dfs - sadrzi cetiri dataframea, jedan za svaki otočni rad koji je testiran, po intervalima su to jedinice:
# A, B, C i D

# graphs and html

# OTOČNI RAD AGREGAT A
html_list = [f"html_{i}" for i in range(len(values))]

for i in range(len(values)):
    fig = graf(split_dfs[0], column_names[i], values[i], units[i], colors[i], otocni_rad[0])
    if i == 0:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs=False)

html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>konzum-zakucac-OR-A</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>HOPS NM - mjerenja konzuma - TP 110/35 kV HE Zakučac</h1>
    <h1>Otočni rad proizvodne jedinice A u HE Zakučac</h1>
    <h1>Promatrani interval: {intervals[0][0]} - {intervals[0][1]}</h1>
    <div>{html_list[0]}</div>
    <div>{html_list[1]}</div>
    <div>{html_list[2]}</div>
    <div>{html_list[3]}</div>
    <div>{html_list[4]}</div>
    <div>{html_list[5]}</div>
</body>
</html>
"""

# Save the HTML page
with open("TS_HE_zakucac_OR_GEN_A.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as TS_HE_zakucac_OR_GEN_A.html")

# OTOČNI RAD AGREGAT D
html_list = [f"html_{i}" for i in range(len(values))]

for i in range(len(values)):
    fig = graf(split_dfs[1], column_names[i], values[i], units[i], colors[i], otocni_rad[1])
    if i == 0:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs=False)

html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>konzum-zakucac-OR-D</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>HOPS NM - mjerenja konzuma - TP 110/35 kV HE Zakučac</h1>
    <h1>Otočni rad proizvodne jedinice D u HE Zakučac</h1>
    <h1>Promatrani interval: {intervals[1][0]} - {intervals[1][1]}</h1>
    <div>{html_list[0]}</div>
    <div>{html_list[1]}</div>
    <div>{html_list[2]}</div>
    <div>{html_list[3]}</div>
    <div>{html_list[4]}</div>
    <div>{html_list[5]}</div>
</body>
</html>
"""

# Save the HTML page
with open("TS_HE_zakucac_OR_GEN_D.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as TS_HE_zakucac_OR_GEN_D.html")

# OTOČNI RAD AGREGAT B
html_list = [f"html_{i}" for i in range(len(values))]

for i in range(len(values)):
    fig = graf(split_dfs[2], column_names[i], values[i], units[i], colors[i], otocni_rad[2])
    if i == 0:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs=False)

html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>konzum-zakucac-OR-B</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>HOPS NM - mjerenja konzuma - TP 110/35 kV HE Zakučac</h1>
    <h1>Otočni rad proizvodne jedinice B u HE Zakučac</h1>
    <h1>Promatrani interval: {intervals[2][0]} - {intervals[2][1]}</h1>
    <div>{html_list[0]}</div>
    <div>{html_list[1]}</div>
    <div>{html_list[2]}</div>
    <div>{html_list[3]}</div>
    <div>{html_list[4]}</div>
    <div>{html_list[5]}</div>
</body>
</html>
"""

# Save the HTML page
with open("TS_HE_zakucac_OR_GEN_B.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as TS_HE_zakucac_OR_GEN_B.html")

# OTOČNI RAD AGREGAT C
html_list = [f"html_{i}" for i in range(len(values))]

for i in range(len(values)):
    fig = graf(split_dfs[3], column_names[i], values[i], units[i], colors[i], otocni_rad[3])
    if i == 0:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs=False)

html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>konzum-zakucac-OR-C</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>HOPS NM - mjerenja konzuma - TP 110/35 kV HE Zakučac</h1>
    <h1>Otočni rad proizvodne jedinice C u HE Zakučac</h1>
    <h1>Promatrani interval: {intervals[3][0]} - {intervals[3][1]}</h1>
    <div>{html_list[0]}</div>
    <div>{html_list[1]}</div>
    <div>{html_list[2]}</div>
    <div>{html_list[3]}</div>
    <div>{html_list[4]}</div>
    <div>{html_list[5]}</div>
</body>
</html>
"""

# Save the HTML page
with open("TS_HE_zakucac_OR_GEN_C.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as TS_HE_zakucac_OR_GEN_C.html")