# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:13:21 2024

@author: larab
"""
import plotly
import plotly.graph_objects as go
import plotly.io as pio
from datetime import timedelta

from os import listdir
from os.path import isfile, join

import pandas as pd
import numpy as np

from scipy.interpolate import UnivariateSpline, interp1d


def napon_graf(df, unit, pmu, start, end, voltage):
    filtered_columns = [col for col in df.columns if "|UN| magn [pu]" in col]
    y_values = df[filtered_columns].values.flatten()
    y_values_kV = y_values*voltage
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=y_values,
        mode="lines",
        name="U [pu]",
        line=dict(color="red")
        ))

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=y_values_kV,
        mode="lines",
        name="U [kV]",
        line=dict(color="blue"),
        yaxis="y2"
        ))

    fig.add_vline(
        x=pd.to_datetime(start).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )

    fig.add_vline(
        x=pd.to_datetime(end).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(start).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {start}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(end).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {end}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
        
    fig.update_layout(
        title=f"Napon u p.u. i kV - mjerenje na {pmu}",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="U [pu]",
                   titlefont=dict(color="red"),
                   tickfont=dict(color="red")),
        yaxis2=dict(showgrid=True,
                    title="U [kV]",
                    titlefont=dict(color="blue"),
                    tickfont=dict(color="blue"),
                    overlaying="y",
                    side="right")
        )
    return fig

def struja_graf(df, unit, pmu, start, end):
    filtered_columns = [col for col in df.columns if "|IN| magn [A]" in col]
    y_values = df[filtered_columns].values.flatten()
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=y_values,
        mode="lines",
        name="I [A]",
        line=dict(color="red")
        ))

    fig.add_vline(
        x=pd.to_datetime(start).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )

    fig.add_vline(
        x=pd.to_datetime(end).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(start).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {start}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(end).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {end}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
        
    fig.update_layout(
        title=f"Struja u A - mjerenje na {pmu}",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="I [A]",
                   titlefont=dict(color="red"),
                   tickfont=dict(color="red"))
        )
    return fig

def frekvencija_graf(df, unit, pmu, start, end):
    filtered_columns = [col for col in df.columns if "f(PMU) [Hz]" in col]
    y_values = df[filtered_columns].values.flatten()
    y_values_pu = y_values/50
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=y_values,
        mode="lines",
        name="f [Hz]",
        line=dict(color="red")
        ))

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=y_values_pu,
        mode="lines",
        name="f [pu]",
        line=dict(color="blue"),
        yaxis="y2"
        ))

    fig.add_vline(
        x=pd.to_datetime(start).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )

    fig.add_vline(
        x=pd.to_datetime(end).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(start).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {start}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(end).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {end}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
        
    fig.update_layout(
        title=f"Frekvencija u p.u. i Hz - mjerenje na {pmu}",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="f [Hz]",
                   titlefont=dict(color="red"),
                   tickfont=dict(color="red")),
        yaxis2=dict(showgrid=True,
                    title="f [pu]",
                    titlefont=dict(color="blue"),
                    tickfont=dict(color="blue"),
                    overlaying="y",
                    side="right")
        )
    return fig

def radna_jalova_graf(df, unit, pmu, start, end):
    filtered_columns = [col for col in df.columns if "P [W]" in col]
    y_values = df[filtered_columns].values.flatten()
    y_values_MW = y_values/1000000
    
    filtered_columns = [col for col in df.columns if "Q [VAr]" in col]
    y_values = df[filtered_columns].values.flatten()
    y_values_MVAr = y_values/1000000
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=y_values_MW,
        mode="lines",
        name="P [MW]",
        line=dict(color="red")
        ))

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=y_values_MVAr,
        mode="lines",
        name="Q [MVAr]",
        line=dict(color="blue"),
        yaxis="y2"
        ))

    fig.add_vline(
        x=pd.to_datetime(start).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )

    fig.add_vline(
        x=pd.to_datetime(end).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(start).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {start}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(end).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {end}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
        
    fig.update_layout(
        title=f"Radna [MW] i jalova [MVAr] snaga - mjerenje na {pmu}",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="P [MW]",
                   titlefont=dict(color="red"),
                   tickfont=dict(color="red")),
        yaxis2=dict(showgrid=True,
                    title="Q [MVAr]",
                    titlefont=dict(color="blue"),
                    tickfont=dict(color="blue"),
                    overlaying="y",
                    side="right")
        )
    return fig


mypath = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\wams-or"""
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

savepath = r"""C:\Users\larab\Documents\GitHub\admilara.github.io\wams-or"""

dfs = []

fdict = {"24-12-04-0812_to_24-12-04-0921_v2.1.2975.csv": {"search_strings": ["Phasor", "PMU#318"],
                                                          "start": "2024-12-04 09:12:58",
                                                          "end": "2024-12-04 10:20:29",
                                                          "unit": "A",
                                                          "PMUS": 1},
         "24-12-04-1048_to_24-12-04-1147_v2.1.2975.csv": {"search_strings": ["Phasor", "PMU#318", "PMU#323"],
                                                          "start": "2024-12-04 11:48:26",
                                                          "end": "2024-12-04 12:46:48",
                                                          "unit": "D",
                                                          "PMUS": 2},
         "24-12-04-1324_to_24-12-04-1426_v2.1.2975.csv": {"search_strings": ["Phasor", "PMU#318", "PMU#324"],
                                                          "start": "2024-12-04 14:24:28",
                                                          "end": "2024-12-04 17:03:18",
                                                          "unit": "B",
                                                          "PMUS": 2},
         "24-12-04-1527_to_24-12-04-1603_v2.1.2975.csv": {"search_strings": ["Phasor", "PMU#318"], 
                                                          "start": "2024-12-04 16:27:27", 
                                                          "end": "2024-12-04 17:03:18",
                                                          "unit": "C",
                                                          "PMUS": 1}}


# =============================================================================
#                       DATAFRAMES FROM CSV FILES
# =============================================================================

col_strings = ["Phasor", "|UN| magn [pu]", "|IN| magn [A]", "f(PMU) [Hz]", "P [W]", "Q [VAr]"]
# col_strings = [string.encode("utf-8") for string in strings]

for file in files:
    print(file)
    print("\n")
    wams_df = pd.read_csv(mypath + "\\" + file, header=0, delimiter=",")
    wams_df["PhasorMs"] = wams_df["PhasorMs"].apply(lambda x: f"{x:03}")
    wams_df["PhasorDatetime"] = (wams_df["PhasorDate"] + ' ' + wams_df["PhasorTime"] + "." + wams_df["PhasorMs"].astype(str))
    wams_df['PhasorDatetime'] = pd.to_datetime(wams_df['PhasorDatetime'], format='%Y-%m-%d %H:%M:%S.%f')
    wams_df['PhasorDatetime'] = wams_df["PhasorDatetime"] + timedelta(hours=1)
    
    search_strings = fdict[file]["search_strings"]
    
    filtered_wams_df = wams_df[[col for col in wams_df.columns if any(s in col for s in search_strings)]]
    filtered_wams_df = filtered_wams_df[[col for col in filtered_wams_df.columns if any(s in col for s in col_strings)]]
    fdict[file]["df"] = filtered_wams_df
    

for key, value in fdict.items():
    for i in range(value["PMUS"]) :
        # ako je i=1 onda se radi o mjerenjima s dva PMU-a (dakle agregati D i B)
        # ako je i=0 onda je PMU 318 u VP Konjsko (za sve agregate)
        filtered_columns = [col for col in value["df"].columns if value["search_strings"][i+1] in col]
        filtered_df = value["df"][filtered_columns].copy()
        filtered_df.loc[:, "PhasorDatetime"] = value["df"]["PhasorDatetime"]
        
        fig1 = radna_jalova_graf(filtered_df, value["unit"], value["search_strings"][i+1], value["start"], value["end"])
        fig2 = frekvencija_graf(filtered_df, value["unit"], value["search_strings"][i+1], value["start"], value["end"])
        if value["search_strings"][i+1] == "PMU#324":
            fig3 = napon_graf(filtered_df, value["unit"], value["search_strings"][i+1], value["start"], value["end"], 220)
        else:
            fig3 = napon_graf(filtered_df, value["unit"], value["search_strings"][i+1], value["start"], value["end"], 110)
        fig4 = struja_graf(filtered_df, value["unit"], value["search_strings"][i+1], value["start"], value["end"])            
        
        html1 = pio.to_html(fig1, full_html=False, include_plotlyjs="cdn")
        html2 = pio.to_html(fig2, full_html=False, include_plotlyjs="cdn")
        html3 = pio.to_html(fig3, full_html=False, include_plotlyjs="cdn")
        html4 = pio.to_html(fig4, full_html=False, include_plotlyjs="cdn")
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Agregat {value['unit']} - {value['search_strings'][i+1]}</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
            <h1>Otočni rad agregata {value['unit']} - {value['search_strings'][i+1]}</h1>
            <div>{html1}</div>
            <div>{html2}</div>
            <div>{html3}</div>
            <div>{html4}</div>
            </body>
        </html>
        """
        with open(f"{savepath}\\or-agregata-{value['unit'].lower()}-{value['search_strings'][i+1].lower()}.html", "w") as file:
            file.write(html_content)
    
    
    
        
    
    


