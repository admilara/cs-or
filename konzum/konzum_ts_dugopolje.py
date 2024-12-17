# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:49:39 2024

@author: Lara Buljan
"""
import plotly
import plotly.graph_objects as go
import plotly.io as pio
 

from os import listdir
from os.path import isfile, join

import pandas as pd
import numpy as np


def graf(df, name, name_tr2, value_column, value_column_tr2, yaxis_name, 
         colour, colour_tr2, otocni_rad):
       
    fig = go.Figure()   
    
    fig.add_trace(go.Scatter(
        x=df[name],
        y=df[value_column],
        mode="lines",
        name=name,
        line=dict(color=colour),
        showlegend=True,
        legendgroup="TR1",
        legendgrouptitle_text="TR1"
        ))
    
    fig.add_trace(go.Scatter(
        x=df[name_tr2],
        y=df[value_column_tr2],
        mode="lines",
        name=name_tr2,
        line=dict(color=colour_tr2),
        showlegend=True,
        legendgroup="TR2",
        legendgrouptitle_text="TR2"
        ))
    
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
    
    if "STRUJA" in name:
        temp1 = df[[name, value_column]]
        temp2 = df[[name_tr2, value_column_tr2]]
        temp1 = temp1.rename(columns = {name: "Timestamp", value_column: "TP1"})
        temp2 = temp2.rename(columns = {name_tr2: "Timestamp", value_column_tr2: "TP2"})

        suma = pd.merge(temp1, temp2, on="Timestamp", how="outer")
        suma = suma.dropna(subset=["TP1", "TP2"], how="all")

        suma["TP1"] = suma["TP1"].ffill()
        suma["TP2"] = suma["TP2"].ffill()

        fig.add_trace(go.Scatter(
            x=suma["Timestamp"],
            y=suma["TP1"] + suma["TP2"],
            mode="lines",
            name="SUMA STRUJA U TP1 I TP2 DUGOPOLJE",
            line=dict(color="magenta"),
            showlegend=True,
            legendgroup="SUMA",
            legendgrouptitle_text="SUMA"
            ))
        
    if "RADNA" in name:
        temp1 = df[[name, value_column]]
        temp2 = df[[name_tr2, value_column_tr2]]
        temp1 = temp1.rename(columns = {name: "Timestamp", value_column: "TP1"})
        temp2 = temp2.rename(columns = {name_tr2: "Timestamp", value_column_tr2: "TP2"})

        suma = pd.merge(temp1, temp2, on="Timestamp", how="outer")
        suma = suma.dropna(subset=["TP1", "TP2"], how="all")

        suma["TP1"] = suma["TP1"].ffill()
        suma["TP2"] = suma["TP2"].ffill()        
        
        fig.add_trace(go.Scatter(
            x=suma["Timestamp"],
            y=suma["TP1"] + suma["TP2"],
            mode="lines",
            name="SUMA RADNIH SNAGA U TP1 I TP2 DUGOPOLJE",
            line=dict(color="magenta"),
            showlegend=True,
            legendgroup="SUMA",
            legendgrouptitle_text="SUMA"
            ))
        
    if "JALOVA" in name:
        temp1 = df[[name, value_column]]
        temp2 = df[[name_tr2, value_column_tr2]]
        temp1 = temp1.rename(columns = {name: "Timestamp", value_column: "TP1"})
        temp2 = temp2.rename(columns = {name_tr2: "Timestamp", value_column_tr2: "TP2"})

        suma = pd.merge(temp1, temp2, on="Timestamp", how="outer")
        suma = suma.dropna(subset=["TP1", "TP2"], how="all")

        suma["TP1"] = suma["TP1"].ffill()
        suma["TP2"] = suma["TP2"].ffill()
        
        fig.add_trace(go.Scatter(
            x=suma["Timestamp"],
            y=suma["TP1"] + suma["TP2"],
            mode="lines",
            name="SUMA JALOVIH SNAGA U TP1 I TP2 DUGOPOLJE",
            line=dict(color="magenta"),
            showlegend=True,
            legendgroup="SUMA",
            legendgrouptitle_text="SUMA"
            ))
    
    
    fig.update_layout(
        title=name + " i " + name_tr2,
        xaxis_title="Vrijeme",
        yaxis_title=yaxis_name,
        legend_title="Legenda",
        template="plotly_white",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)       
        )
    return fig

   
konzum_path = "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\konzum\\TS_DUG_TR1_TR2_20241204_0910-1710.csv"

konzum_df = pd.read_csv(konzum_path, delimiter=";")
konzum_df = konzum_df.dropna(axis=1, how="all")

column_names = konzum_df.columns

column_names = konzum_df.columns[::2]
values = konzum_df.columns[1::2]
units = ["I [A]", "P [MW]", "Q [Mvar]", "U [kV]", "položaj reg. sklopke", "U [kV]"]
colors = ["blue", "blue", "blue", "green", "black", "green"]
colors2 = ["red", "red", "red", "orange", "blue", "orange"]

# datetime conversion
for name in column_names:
    konzum_df[name] = pd.to_datetime(konzum_df[name], format="%d.%m.%Y. %H:%M:%S", dayfirst=True)

# float values 
for name in konzum_df.columns:
    first_value = konzum_df[name].iloc[0]  # Get the first value for type checking
    
    if isinstance(first_value, str):
        konzum_df[name] = konzum_df[name].str.replace(',', '.').astype(float)
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
        mask = (konzum_df[time_col] >= start_time) & (konzum_df[time_col] <= end_time)
        split_data[time_col] = konzum_df[time_col][mask].reset_index(drop=True)
        split_data[value_col] = konzum_df[value_col][mask].reset_index(drop=True)
    split_dfs.append(pd.DataFrame(split_data))


# split_dfs - sadrzi cetiri dataframea, jedan za svaki otočni rad koji je testiran, po intervalima su to jedinice:
# A, B, C i D

# graphs and html

# OTOČNI RAD AGREGAT A
html_list = [f"html_{i}" for i in range(len(values))]

for i in range(int(len(column_names)/2)):
    fig = graf(split_dfs[0], column_names[i], column_names[i+6], values[i], 
               values[i+6], units[i], colors[i], colors2[i], otocni_rad[0])
    if i == 0:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs=False)



html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>konzum-dugopolje-OR-A</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>HOPS NM - mjerenja konzuma - TS 110/20 kV Dugopolje</h1>
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
with open("TS_Dugopolje_OR_GEN_A.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as TS_Dugopolje_OR_GEN_A.html")


# OTOČNI RAD AGREGAT D
html_list = [f"html_{i}" for i in range(len(values))]

for i in range(int(len(column_names)/2)):
    fig = graf(split_dfs[1], column_names[i], column_names[i+6], values[i], 
               values[i+6], units[i], colors[i], colors2[i], otocni_rad[1])
    if i == 0:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs=False)



html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>konzum-dugopolje-OR-D</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>HOPS NM - mjerenja konzuma - TS 110/20 kV Dugopolje</h1>
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
with open("TS_Dugopolje_OR_GEN_D.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as TS_Dugopolje_OR_gen_D.html")


# OTOČNI RAD AGREGAT B
html_list = [f"html_{i}" for i in range(len(values))]

for i in range(int(len(column_names)/2)):
    fig = graf(split_dfs[2], column_names[i], column_names[i+6], values[i], 
               values[i+6], units[i], colors[i], colors2[i], otocni_rad[2])
    if i == 0:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs=False)



html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>konzum-dugopolje-OR-B</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>HOPS NM - mjerenja konzuma - TS 110/20 kV Dugopolje</h1>
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
with open("TS_Dugopolje_OR_GEN_B.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as TS_Dugopolje_OR_gen_B.html")



# OTOČNI RAD AGREGAT C
html_list = [f"html_{i}" for i in range(len(values))]

for i in range(int(len(column_names)/2)):
    fig = graf(split_dfs[3], column_names[i], column_names[i+6], values[i], 
               values[i+6], units[i], colors[i], colors2[i], otocni_rad[3])
    if i == 0:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html_list[i] = pio.to_html(fig, full_html=False, include_plotlyjs=False)



html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>konzum-dugopolje-OR-C</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>HOPS NM - mjerenja konzuma - TS 110/20 kV Dugopolje</h1>
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
with open("TS_Dugopolje_OR_GEN_C.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as TS_Dugopolje_OR_gen_C.html")