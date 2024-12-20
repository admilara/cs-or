# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:18:35 2024

@author: Lara Buljan
"""
import plotly
import plotly.graph_objects as go
import plotly.io as pio
 

from os import listdir
from os.path import isfile, join

import pandas as pd
import numpy as np

from scipy.interpolate import UnivariateSpline, interp1d


    
def spline_interpolate(column, timestamps):
    
    valid_x = timestamps[column.notna()]
    valid_y = column[column.notna()]
    
    spline = UnivariateSpline(valid_x, valid_y, k=1, s=0)

    return spline(timestamps)

# def spline_interpolate(column, timestamps):
    
#     valid_x = timestamps[column.notna()]
#     valid_y = column[column.notna()]
    
#     spline = UnivariateSpline(valid_x, valid_y, k=3, s=0)

#     return spline(timestamps)


konzum = {
    "zakucac": {"path": "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\konzum\\HE_ZAK_TR1_20241204_0910-1710.csv",
                "radna": [],
                "jalova": [],
                "radna_values": [],
                "jalova_values": []},
    "kastela": {"path": "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\konzum\\TS_KAST_TR2_20241204_0910-1710.csv",
                "radna": [],
                "jalova": [],
                "radna_values": [],
                "jalova_values": []},
    "dugopolje": {"path": "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\konzum\\TS_DUG_TR1_TR2_20241204_0910-1710.csv",
                  "radna": [],
                  "jalova": [],
                  "radna_values": [],
                  "jalova_values": []},
    "sinj": {"path": "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\konzum\\TS_SINJ_TR1_TR2_20241204_0910-1710.csv",
             "radna": [],
             "jalova": [],
             "radna_values": [],
             "jalova_values": []},
    "meterize": {"path": "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\konzum\\TS_MET_TR1_TR2_20241204_0910-1710.csv",
                 "radna": [],
                 "jalova": [],
                 "radna_values": [],
                 "jalova_values": []},
    "vrboran": {"path": "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\HOPS\\mjerenja\\konzum\\TS_VRB_TR1_TR2_20241204_0910-1710.csv",
                "radna": [],
                "jalova": [],
                "radna_values": [],
                "jalova_values": []}
    }

for key, value in konzum.items():
    path = value.get("path")
    value["df"] = pd.read_csv(path, delimiter=";")
    value["df"] = value["df"].dropna(axis=1, how="all")
    
    radna_columns = [col for col in value["df"].columns if "RADNA" in col]
    radna_indices = [i for i, col in enumerate(value["df"].columns) if "RADNA" in col.upper()]
    
    for index in radna_indices:
        konzum[key]["radna"].append(konzum[key]["df"].columns[index])
        if index+1 < len(konzum[key]["df"].columns):
            konzum[key]["radna_values"].append(konzum[key]["df"].columns[index+1])
    
    jalova_columns = [col for col in konzum[key]["df"].columns if "JALOVA" in col]
    jalova_indices = [i for i, col in enumerate(konzum[key]["df"].columns) if "JALOVA" in col.upper()]

    #print(jalova_columns)
    #print(jalova_indices)
    
    for index in jalova_indices:
        konzum[key]["jalova"].append(konzum[key]["df"].columns[index])
        if index+1 < len(konzum[key]["df"].columns):
            konzum[key]["jalova_values"].append(konzum[key]["df"].columns[index+1])



intervals = [("2024-12-04 09:10:00", "2024-12-04 11:00:00"), 
             ("2024-12-04 11:00:00", "2024-12-04 13:00:00"),
             ("2024-12-04 14:15:00", "2024-12-04 15:30:00"),
             ("2024-12-04 16:15:00", "2024-12-04 17:10:00")]

otocni_rad = [("2024-12-04 09:12:58", "HE ZAK 110 METERIZE/2", "2024-12-04 10:20:29", "HE ZAK 110 SP W12"),
              ("2024-12-04 11:48:26", "HE ZAK 110 METERIZE/2", "2024-12-04 12:46:48", "HE ZAK 110 SP W12"),
              ("2024-12-04 14:24:28", "HE ZAK 110 METERIZE/2", "2024-12-04 15:25:27", "HE ZAK 110 SP W12"),
              ("2024-12-04 16:27:27", "HE ZAK 110 METERIZE/2", "2024-12-04 17:03:18", "HE ZAK 220 SP W12")]

for key, value in konzum.items():
    df = value.get("df")
    
    column_names = df.columns[::2]
    values = df.columns[1::2]
    
    for name in column_names:
        df[name] = pd.to_datetime(df[name], format="%d.%m.%Y. %H:%M:%S", dayfirst=True)
    
    for name in df.columns:
        first_value = df[name].iloc[0]
        if isinstance(first_value, str):
            df[name]= df[name].str.replace(",", ".").astype(float)
        elif isinstance(first_value, (np.float64, float)):
            continue
            #print(f"Column '{name}' is already of type float.")
        else:
            continue
            #print(f"Column '{name}' is of unexpected type: {type(first_value)}")
    
    konzum[key]["df"] = df



for key, value in konzum.items():
    df = value.get("df")
    split_dfs = []
    column_mapping = {}
    for time_col, value_col in zip(df.columns[::2], df.columns[1::2]):
        column_mapping[time_col] = value_col

    # Loop through intervals and filter the DataFrame
    for start, end in intervals:
        split_data = {}
        start_time = pd.to_datetime(start, format="%Y-%m-%d %H:%M:%S")
        end_time = pd.to_datetime(end, format="%Y-%m-%d %H:%M:%S")

        for time_col, value_col in column_mapping.items():
            mask = (df[time_col] >= start_time) & (df[time_col] <= end_time)
            split_data[time_col] = df[time_col][mask].reset_index(drop=True)
            split_data[value_col] = df[value_col][mask].reset_index(drop=True)
        split_dfs.append(pd.DataFrame(split_data))
    konzum[key]["split_dfs"] = split_dfs
    
    
for key, value in konzum.items():
    radna_stupci = []
    for i in range(len(value["radna"])):
        radna_stupci.append(value["radna"][i])
        radna_stupci.append(value["radna_values"][i])
    filtered_radna_df = value["df"][radna_stupci]
    value["filtered_radna_df"] = filtered_radna_df 
    
    jalova_stupci = []
    for i in range(len(value["jalova"])):
        jalova_stupci.append(value["jalova"][i])
        jalova_stupci.append(value["jalova_values"][i])
    filtered_jalova_df = value["df"][jalova_stupci]
    value["filtered_jalova_df"] = filtered_jalova_df

for key, value in konzum.items():
    df = value["filtered_radna_df"]
    if len(df.columns)>2:
        print(df[[value["radna"][0], value["radna_values"][0]]])
        
        melted_1 = df[[value["radna"][0], value["radna_values"][0]]].rename(
                    columns={value["radna"][0]: "timestamp", value["radna_values"][0]: "value0"})
        melted_2 = df[[value["radna"][1], value["radna_values"][1]]].rename(
                    columns={value["radna"][1]: "timestamp", value["radna_values"][1]: "value1"})
        merged_df = pd.merge(melted_1, melted_2, on='timestamp', how='outer')
        merged_df.sort_values(by='timestamp', inplace=True)
        
        merged_df = merged_df.dropna(subset=["value0", "value1"], how="all")

        merged_df["value0"] = merged_df["value0"].ffill()
        merged_df["value1"] = merged_df["value1"].ffill()
        value["filtered_radna_df"] = merged_df
    else:
        df = df.rename(columns={value["radna"][0]: "timestamp", value["radna_values"][0]: "value0"})
        value["filtered_radna_df"] = df
    
    df = value["filtered_jalova_df"]
    if len(df.columns)>2:
        print(df[[value["jalova"][0], value["jalova_values"][0]]])
        
        melted_1 = df[[value["jalova"][0], value["jalova_values"][0]]].rename(
                    columns={value["jalova"][0]: "timestamp", value["jalova_values"][0]: "value0"})
        melted_2 = df[[value["jalova"][1], value["jalova_values"][1]]].rename(
                    columns={value["jalova"][1]: "timestamp", value["jalova_values"][1]: "value1"})
        merged_df = pd.merge(melted_1, melted_2, on='timestamp', how='outer')
        merged_df.sort_values(by='timestamp', inplace=True)
        
        merged_df = merged_df.dropna(subset=["value0", "value1"], how="all")

        merged_df["value0"] = merged_df["value0"].ffill()
        merged_df["value1"] = merged_df["value1"].ffill()
        value["filtered_jalova_df"] = merged_df
    else:
        df = df.rename(columns={value["jalova"][0]: "timestamp", value["jalova_values"][0]: "value0"})
        value["filtered_jalova_df"] = df


#RADNA SNAGA

final_radna_df = pd.DataFrame()
for i, (key, value) in enumerate(konzum.items()):
    print("final_radna_df columns:", final_radna_df.columns)
    print(f"value['filtered_radna_df'] columns ({key}):", value["filtered_radna_df"].columns)
    if "vrboran" in key.lower():
        value["filtered_radna_df"]["value0"] = value["filtered_radna_df"]["value0"]*-1
        value["filtered_radna_df"]["value1"] = value["filtered_radna_df"]["value1"]*-1

    value["filtered_radna_df"] = value["filtered_radna_df"].rename(
        columns=lambda col: f"{col}_{i}" if col != "timestamp" else col)

    if final_radna_df.empty:
        print("Is final_radna_df empty?", final_radna_df.empty)
        print(f"Is value['filtered_radna_df'] empty ({key})?", value["filtered_radna_df"].empty)
        final_radna_df = value["filtered_radna_df"]
    else:
        # Ensure "timestamp" exists before merging
        if "timestamp" in value["filtered_radna_df"].columns:
            print(value["filtered_radna_df"].columns)
            final_radna_df = pd.merge(final_radna_df, value["filtered_radna_df"], left_on="timestamp", right_on="timestamp", how="outer")

final_radna_df["time_seconds"] = (final_radna_df["timestamp"] - final_radna_df["timestamp"].min()).dt.total_seconds()
final_radna_df.iloc[:, 1:] = final_radna_df.iloc[:, 1:].apply(lambda col: spline_interpolate(col, final_radna_df["time_seconds"]), axis=0)
#final_radna_df = final_radna_df.interpolate(method="linear", axis=1)

final_radna_df["suma"] = final_radna_df.drop(columns=["timestamp", "time_seconds"]).sum(axis=1)
final_radna_df["suma"] = final_radna_df["suma"]*-1


# JALOVA SNAGA

final_jalova_df = pd.DataFrame()
for i, (key, value) in enumerate(konzum.items()):
    print("final_jalova_df columns:", final_jalova_df.columns)
    print(f"value['filtered_jalova_df'] columns ({key}):", value["filtered_jalova_df"].columns)
    if "vrboran" in key.lower():
        value["filtered_jalova_df"]["value0"] = value["filtered_jalova_df"]["value0"]*-1
        value["filtered_jalova_df"]["value1"] = value["filtered_jalova_df"]["value1"]*-1
    
    value["filtered_jalova_df"] = value["filtered_jalova_df"].rename(
        columns=lambda col: f"{col}_{i}" if col != "timestamp" else col)

    if final_jalova_df.empty:
        print("Is final_jalova_df empty?", final_jalova_df.empty)
        print(f"Is value['filtered_jalova_df'] empty ({key})?", value["filtered_jalova_df"].empty)
        final_jalova_df = value["filtered_jalova_df"]
    else:
        # Ensure "timestamp" exists before merging
        if "timestamp" in value["filtered_jalova_df"].columns:
            final_jalova_df = pd.merge(final_jalova_df, value["filtered_jalova_df"], left_on="timestamp", right_on="timestamp", how="outer")

final_jalova_df["time_seconds"] = (final_jalova_df["timestamp"] - final_jalova_df["timestamp"].min()).dt.total_seconds()
final_jalova_df.iloc[:, 1:] = final_jalova_df.iloc[:, 1:].apply(lambda col: spline_interpolate(col, final_jalova_df["time_seconds"]), axis=0)
#final_jalova_df = final_jalova_df.interpolate(method="linear", axis=1)

final_jalova_df["suma"] = final_jalova_df.drop(columns=["timestamp", "time_seconds"]).sum(axis=1)
final_jalova_df["suma"] = final_jalova_df["suma"]*-1


# SPLIT SUM
split_final_radna_dfs = []
for start, end in intervals:
#    print(start, end, intervals)
    split_final_radna = pd.DataFrame()
    start_time = pd.to_datetime(start, format="%Y-%m-%d %H:%M:%S")
    end_time = pd.to_datetime(end, format="%Y-%m-%d %H:%M:%S")

    mask = (final_radna_df["timestamp"] >= start_time) & (final_radna_df["timestamp"] <= end_time)
    split_final_radna["timestamp"] = final_radna_df["timestamp"][mask].reset_index(drop=True)
    split_final_radna["suma"] = final_radna_df["suma"][mask].reset_index(drop=True)
    split_final_radna_dfs.append(split_final_radna)

split_final_jalova_dfs = []
for start, end in intervals:
    split_final_jalova = pd.DataFrame()
    start_time = pd.to_datetime(start, format="%Y-%m-%d %H:%M:%S")
    end_time = pd.to_datetime(end, format="%Y-%m-%d %H:%M:%S")

    mask = (final_jalova_df["timestamp"] >= start_time) & (final_jalova_df["timestamp"] <= end_time)
    split_final_jalova["timestamp"] = final_jalova_df["timestamp"][mask].reset_index(drop=True)
    split_final_jalova["suma"] = final_jalova_df["suma"][mask].reset_index(drop=True)
    split_final_jalova_dfs.append(split_final_jalova)


#FIGURES - RADNA SNAGA
fig_list = []
html_list = []
agregati = ["A", "D", "B", "C"]
for i in range(4):    
    interval_index = i
    fig = go.Figure()
    for key, value in konzum.items():
        for j in range(len(value["radna"])):
            fig.add_trace(go.Scatter(
                x = value["split_dfs"][interval_index][value["radna"][j]],            
                y = value["split_dfs"][interval_index][value["radna_values"][j]],
                mode = "lines",
                name = value["radna"][j],
                showlegend=True
        ))
    fig.add_vline(
        x=pd.to_datetime(otocni_rad[i][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[i][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    filtered_temp_df = split_final_radna_dfs[i][
        (split_final_radna_dfs[i]["timestamp"]>=otocni_rad[i][0]) & 
        (split_final_radna_dfs[i]["timestamp"]<=otocni_rad[i][2])
        ]
    max_value_p = round(filtered_temp_df["suma"].max(), 2)
    max_index_p = round(filtered_temp_df["suma"].idxmax(), 2)
    min_value_p = round(filtered_temp_df["suma"].min(), 2)
    min_index_p = round(filtered_temp_df["suma"].idxmin(), 2)
    # print(max_value_p)
    # print(max_index_p)
    # print(min_value_p)
    # print(min_index_p)    
    
    fig.add_annotation(
        x=split_final_radna_dfs[i]["timestamp"].iloc[max_index_p], 
        y=max_value_p, 
        text=f"max: {max_value_p}",
        font=dict(family='Helvetica', size=14, color="magenta"),
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-30
        )
    
    fig.add_annotation(
        x=split_final_radna_dfs[i]["timestamp"].iloc[min_index_p], 
        y=min_value_p,
        text=f"min: {min_value_p}",
        font=dict(family='Helvetica', size=14, color="magenta"),
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=30
        )
    
    fig.add_trace(go.Scatter(
        x=split_final_radna_dfs[i]["timestamp"],
        y=split_final_radna_dfs[i]["suma"],
        mode="lines",
        name="Suma radnih snaga po TS u otoku",
        showlegend=True,
        line=dict(color="magenta")
        ))
    
    fig.add_annotation(
        x=pd.to_datetime(otocni_rad[i][0]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {otocni_rad[i][1]}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="magenta", size=12),
        bordercolor="magenta",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(otocni_rad[i][2]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {otocni_rad[i][3]}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="magenta", size=12),
        bordercolor="magenta",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    name = f"Otočni rad agregata {agregati[i]} - suma konzuma po trafostanicama u otoku"
    yaxis_name = "Radna snaga P[MW]"
    fig.update_layout(
        title=name,
        xaxis_title="Vrijeme",
        yaxis_title=yaxis_name,
        legend_title="Legenda",
        #template="plotly_white",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True) )
    
    fig_list.append(fig)
    if i == 0:
        html = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html = pio.to_html(fig, full_html=False, include_plotlyjs=False)
    html_list.append(html)

agregati = ["A", "D", "B", "C"]
for i in range(4):    
    interval_index = i
    fig = go.Figure()
    for key, value in konzum.items():
        for j in range(len(value["jalova"])):
            fig.add_trace(go.Scatter(
                x = value["split_dfs"][interval_index][value["jalova"][j]],            
                y = value["split_dfs"][interval_index][value["jalova_values"][j]],
                mode = "lines",
                name = value["jalova"][j],
                showlegend=True
        ))
    fig.add_vline(
        x=pd.to_datetime(otocni_rad[i][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[i][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    filtered_temp_df = split_final_jalova_dfs[i][
        (split_final_jalova_dfs[i]["timestamp"]>=otocni_rad[i][0]) & 
        (split_final_jalova_dfs[i]["timestamp"]<=otocni_rad[i][2])
        ]
    max_value_q = round(filtered_temp_df["suma"].max(), 2)
    max_index_q = round(filtered_temp_df["suma"].idxmax(), 2)
    min_value_q = round(filtered_temp_df["suma"].min(), 2)
    min_index_q = round(filtered_temp_df["suma"].idxmin(), 2)
    # print(max_value_p)
    # print(max_index_p)
    # print(min_value_p)
    # print(min_index_p)    
    
    fig.add_annotation(
        x=split_final_jalova_dfs[i]["timestamp"].iloc[max_index_q], 
        y=max_value_q, 
        text=f"max: {max_value_q}",
        font=dict(family='Helvetica', size=14, color="magenta"),
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-30
        )
    
    fig.add_annotation(
        x=split_final_jalova_dfs[i]["timestamp"].iloc[min_index_q], 
        y=min_value_q,
        text=f"min: {min_value_q}",
        font=dict(family='Helvetica', size=14, color="magenta"),
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=30
        )
    
    fig.add_trace(go.Scatter(
        x=split_final_jalova_dfs[i]["timestamp"],
        y=split_final_jalova_dfs[i]["suma"],
        mode="lines",
        name="Suma jalovih snaga po TS u otoku",
        showlegend=True,
        line=dict(color="magenta")
        ))
    
    fig.add_annotation(
        x=pd.to_datetime(otocni_rad[i][0]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {otocni_rad[i][1]}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="magenta", size=12),
        bordercolor="magenta",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(otocni_rad[i][2]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {otocni_rad[i][3]}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="magenta", size=12),
        bordercolor="magenta",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    name = f"Otočni rad agregata {agregati[i]} - suma konzuma po trafostanicama u otoku"
    yaxis_name = "Jalova snaga Q[Mvar]"
    fig.update_layout(
        title=name,
        xaxis_title="Vrijeme",
        yaxis_title=yaxis_name,
        legend_title="Legenda",
        #template="plotly-white",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True) )
    
    fig_list.append(fig)
    html = pio.to_html(fig, full_html=False, include_plotlyjs=False)
    html_list.append(html)


html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>suma-konzum</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h2>Suma radnih snaga</h2>
    <div>{html_list[0]}</div>
    <div>{html_list[1]}</div>
    <div>{html_list[2]}</div>
    <div>{html_list[3]}</div>
    
    <h2>Suma jalovih snaga</h2>
    <div>{html_list[4]}</div>
    <div>{html_list[5]}</div>
    <div>{html_list[6]}</div>
    <div>{html_list[7]}</div>
    
</body>
</html>
"""

# Save the HTML page
with open("suma-konzum-or.html", "w") as f:
    f.write(html_page)

print("Dashboard saved as suma-konzum-or.html")
    

    




