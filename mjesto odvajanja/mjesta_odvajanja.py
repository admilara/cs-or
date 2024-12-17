# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:32:09 2024

@author: larab
"""

import plotly
import plotly.graph_objects as go
import plotly.io as pio
 

from os import listdir
from os.path import isfile, join

import pandas as pd
import numpy as np

intervals = [("2024-12-04 09:10:00", "2024-12-04 11:00:00"), 
             ("2024-12-04 11:00:00", "2024-12-04 13:00:00"),
             ("2024-12-04 14:15:00", "2024-12-04 15:30:00"),
             ("2024-12-04 16:15:00", "2024-12-04 17:10:00")]

otocni_rad = [("2024-12-04 09:12:58", "HE ZAK 110 METERIZE/2", "2024-12-04 10:20:29", "HE ZAK 110 SP W12"),
              ("2024-12-04 11:48:26", "HE ZAK 110 METERIZE/2", "2024-12-04 12:46:48", "HE ZAK 110 SP W12"),
              ("2024-12-04 14:24:28", "HE ZAK 110 METERIZE/2", "2024-12-04 15:25:27", "HE ZAK 110 SP W12"),
              ("2024-12-04 16:27:27", "HE ZAK 110 METERIZE/2", "2024-12-04 17:03:18", "HE ZAK 110 SP W12")]

file_name = "110_ZAK-MET_2_20241204_0910-1710.csv"
path = "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\mjesta odvajanja i sinkronizacije\\"

full_path = path + file_name

full_df = pd.read_csv(full_path, delimiter=";")
full_df = full_df.dropna(axis=1, how="all")

for column in full_df.columns:
    if "Unnamed:" in column:
        first_value = full_df[column].iloc[0]
        if isinstance(first_value, str):
            full_df[column] = full_df[column].str.replace(",", ".").astype(float)
        elif isinstance(first_value, (np.float, float)):
            continue
        else:
            continue
    else:
        full_df[column] = pd.to_datetime(full_df[column], format="%d.%m.%Y. %H:%M:%S", dayfirst=True)


split_dfs = []

column_mapping = {}
for time_col, value_col in zip(full_df.columns[::2], full_df.columns[1::2]):
    column_mapping[time_col] = value_col

# Loop through intervals and filter the DataFrame
for start, end in intervals:
    split_data = {}
    start_time = pd.to_datetime(start, format="%Y-%m-%d %H:%M:%S")
    end_time = pd.to_datetime(end, format="%Y-%m-%d %H:%M:%S")

    for time_col, value_col in column_mapping.items():
        mask = (full_df[time_col] >= start_time) & (full_df[time_col] <= end_time)
        split_data[time_col] = full_df[time_col][mask].reset_index(drop=True)
        split_data[value_col] = full_df[value_col][mask].reset_index(drop=True)
    split_dfs.append(pd.DataFrame(split_data))

yaxis_names = ["STRUJA - I[A]", "RADNA SNAGA - P[MW]", "JALOVA SNAGA Q[Mvar]", "NAPON - U[kV]"]
agregati = ["A", "D", "B", "C"]
fig_list = []
html_list = []

for i, df in enumerate(split_dfs):  # Loop over each split_df
    print(f"Agregat: {agregati[i]}")
    
    # Generate 4 graphs for the current split_df
    for j in range(4):  # Corresponds to each measurement type in yaxis_names
        fig = go.Figure()
        
        # Get the columns for timestamps and values
        # Columns are paired: (timestamp, value) for both sides of the line
        timestamp_side1 = df.columns[j * 2]         # 0, 2, 4, 6 (timestamps on side 1)
        value_side1 = df.columns[j * 2 + 1]        # 1, 3, 5, 7 (values on side 1)
        timestamp_side2 = df.columns[j * 2 + 8]    # 8, 10, 12, 14 (timestamps on side 2)
        value_side2 = df.columns[j * 2 + 9]        # 9, 11, 13, 15 (values on side 2)
        
        # Add traces for both sides of the line
        fig.add_trace(go.Scatter(
            x=df[timestamp_side1],
            y=df[value_side1],
            mode="lines",
            name=f"{timestamp_side1}",
            showlegend=True
        ))
        fig.add_trace(go.Scatter(
            x=df[timestamp_side2],
            y=df[value_side2],
            mode="lines",
            name=f"{timestamp_side2}",
            showlegend=True
        ))
        
        # Update the layout with dynamic titles
        fig.update_layout(
            title=f"OR proizvodne jedinice {agregati[i]}: {yaxis_names[j]} - veličine: {timestamp_side1} | {timestamp_side2}",
            xaxis_title="Vrijeme",
            yaxis_title=yaxis_names[j],
            legend_title="Legenda",
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True)
        )
        
        # Append the figure to the list
        fig_list.append(fig)
        
        # Generate HTML for the figure
        if i == 0 and j == 0:  # Include Plotly.js only once
            html = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
        else:
            html = pio.to_html(fig, full_html=False, include_plotlyjs=False)
        html_list.append(html)

        # Debug output
        print(f"Generated graph {j + 1} for Agregat {agregati[i]} with y-axis: {yaxis_names[j]}")
        
html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>suma-konzum</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Mjerene veličine na mjestu odvajanja - DV 110 kV HE Zakučac - Meterize II</h1>
    <p>Za svaku mjerenu veličinu [I, P, Q, U] graf prikazuje mjerene veličine s obje strane dalekovoda.</p>
    <p>Mjerenja su prikazana odvojeno po agregatima, u redoslijedu prema pokusu otočnog rada. </p>
    <h1>Agregat A</h1>
    <div>{html_list[0]}</div>
    <div>{html_list[1]}</div>
    <div>{html_list[2]}</div>
    <div>{html_list[3]}</div>
    <h1>Agregat D</h1>
    <div>{html_list[4]}</div>
    <div>{html_list[5]}</div>
    <div>{html_list[6]}</div>
    <div>{html_list[7]}</div>
    <h1>Agregat B</h1>
    <div>{html_list[8]}</div>
    <div>{html_list[9]}</div>
    <div>{html_list[10]}</div>
    <div>{html_list[11]}</div>
    <h1>Agregat C</h1>
    <div>{html_list[12]}</div>
    <div>{html_list[13]}</div>
    <div>{html_list[14]}</div>
    <div>{html_list[15]}</div>
</body>
</html>
"""

# Save the HTML page
with open("mjesto-odvajanja-test.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as mjesto-odvajanja-test.html")
