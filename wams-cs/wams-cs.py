# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:59:01 2024

@author: larab
"""

import plotly
import plotly.graph_objects as go
import plotly.io as pio
from datetime import timedelta
from datetime import datetime
from os import listdir
from os.path import isfile, join

import pandas as pd
import numpy as np

def naponi_graf(unit, df, pmu, annotations):
    # Debug: Check initial data
    # print(df.head())
    # print(df["PhasorDatetime"].head())

    # Ensure datetime is parsed correctly
    df["PhasorDatetime"] = pd.to_datetime(df["PhasorDatetime"], errors="coerce")
    if df["PhasorDatetime"].isnull().sum() > 0:
        print("Error: Invalid datetime values found.")
        return

    # Extract the data for each phase
    Uf_1 = df[[col for col in df.columns if "UPhase1abs" in col]]
    Uf_2 = df[[col for col in df.columns if "UPhase2abs" in col]]
    Uf_3 = df[[col for col in df.columns if "UPhase3abs" in col]]

    # Debug: Check selected columns
    # print("UPhase1abs columns:", Uf_1.columns)
    # print("UPhase2abs columns:", Uf_2.columns)
    # print("UPhase3abs columns:", Uf_3.columns)

    # Ensure no NaN or invalid data
    Uf_1 = Uf_1.dropna().astype(float)
    Uf_2 = Uf_2.dropna().astype(float)
    Uf_3 = Uf_3.dropna().astype(float)

    # Perform division to convert to kV if needed
    Uf1_values = Uf_1 / 1000
    Uf2_values = Uf_2 / 1000
    Uf3_values = Uf_3 / 1000

    # Debug: Check dimensions and data
    # print("PhasorDatetime shape:", df["PhasorDatetime"].shape)
    # print("Uf1_values shape:", Uf1_values.shape)
    # print("Uf2_values shape:", Uf2_values.shape)
    # print("Uf3_values shape:", Uf3_values.shape)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=Uf1_values.iloc[:, 0],  # Use the first column if multiple columns are selected
        mode="lines",
        name="U phase 1 [kV]",
        line=dict(color="red")
    ))

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=Uf2_values.iloc[:, 0],
        mode="lines",
        name="U phase 2 [kV]",
        line=dict(color="blue"),
    ))

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=Uf3_values.iloc[:, 0],
        mode="lines",
        name="U phase 3 [kV]",
        line=dict(color="green"),
    ))

    fig.add_vline(
        x=pd.to_datetime(annotations[1]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_vline(
        x=pd.to_datetime(annotations[3]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_vline(
        x=pd.to_datetime(annotations[5]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(annotations[1]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[0],
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
        x=pd.to_datetime(annotations[3]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[2],
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-60,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(annotations[5]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[4],
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )

    if unit == "B": 
        fig.add_vline(
            x=pd.to_datetime(annotations[7]).to_pydatetime(),
            line_width=1,
            line_dash="dash",
            line_color="#754FC5"
            )
        fig.add_annotation(
            x=pd.to_datetime(annotations[7]).to_pydatetime(),
            y=0.9,  # Set a relevant y-axis value
            xref="x",
            yref="paper",
            text=annotations[6],
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
        title=f"Fazni naponi tijekom CS agregata {unit} - mjerenje na PMU#{pmu}",
        template="plotly",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True, title="U [kV]")
    )
    return fig    
    
def struje_graf(unit, df, pmu, annotations):
    # Ensure datetime is parsed correctly
    df["PhasorDatetime"] = pd.to_datetime(df["PhasorDatetime"], errors="coerce")
    if df["PhasorDatetime"].isnull().sum() > 0:
        print("Error: Invalid datetime values found.")
        return

    # Debug: Print datetime details
    # print("PhasorDatetime sample:")
    # print(df["PhasorDatetime"].head())

    # Extract the data for each phase
    If_1 = df[[col for col in df.columns if "IPhase1abs" in col]]
    If_2 = df[[col for col in df.columns if "IPhase2abs" in col]]
    If_3 = df[[col for col in df.columns if "IPhase3abs" in col]]

    # Debug: Check selected columns
    # print("IPhase1abs columns:", If_1.columns)
    # print("IPhase2abs columns:", If_2.columns)
    # print("IPhase3abs columns:", If_3.columns)

    # Force all values to numeric and check for invalid data
    If_1 = If_1.apply(pd.to_numeric, errors="coerce")
    If_2 = If_2.apply(pd.to_numeric, errors="coerce")
    If_3 = If_3.apply(pd.to_numeric, errors="coerce")
    # print("NaN counts in If_1:", If_1.isnull().sum().sum())

    # Perform conversion to numeric if needed
    If1_values = If_1.iloc[:, 0]  # Select the first column if multiple
    If2_values = If_2.iloc[:, 0]
    If3_values = If_3.iloc[:, 0]

    # Debug: Inspect data ranges
    # print("Y-axis (If1_values):")
    # print(If1_values.describe())
    # print("Y-axis (If2_values):")
    # print(If2_values.describe())
    # print("Y-axis (If3_values):")
    # print(If3_values.describe())

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=If1_values,
        mode="lines",
        name="I phase 1 [A]",
        line=dict(color="red")
    ))

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=If2_values,
        mode="lines",
        name="I phase 2 [A]",
        line=dict(color="blue"),
    ))

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=If3_values,
        mode="lines",
        name="I phase 3 [A]",
        line=dict(color="green"),
    ))
    
    fig.add_vline(
        x=pd.to_datetime(annotations[1]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_vline(
        x=pd.to_datetime(annotations[3]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_vline(
        x=pd.to_datetime(annotations[5]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(annotations[1]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[0],
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
        x=pd.to_datetime(annotations[3]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[2],
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-60,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(annotations[5]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[4],
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    if unit == "B": 
        fig.add_vline(
            x=pd.to_datetime(annotations[7]).to_pydatetime(),
            line_width=1,
            line_dash="dash",
            line_color="#754FC5"
            )
        fig.add_annotation(
            x=pd.to_datetime(annotations[7]).to_pydatetime(),
            y=0.9,  # Set a relevant y-axis value
            xref="x",
            yref="paper",
            text=annotations[6],
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
        title=f"Struje tijekom CS agregata {unit} - mjerenje na PMU#{pmu}",
        template="plotly",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True, title="I [A]")
    )
    return fig    

def frekvencija_graf(unit, df, pmu, annotations):
    df["PhasorDatetime"] = pd.to_datetime(df["PhasorDatetime"], errors="coerce")
    if df["PhasorDatetime"].isnull().sum() > 0:
        print("Error: Invalid datetime values found.")
        return
    
    freq = df[[col for col in df.columns if "Freq" in col]]
    freq_values = freq.apply(pd.to_numeric, errors="coerce")
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=freq_values.iloc[:, 0],
        mode="lines",
        name="freq [Hz]",
        line=dict(color="blue"),
        ))

    fig.add_trace(go.Scatter(
        x=df["PhasorDatetime"],
        y=freq_values.iloc[:, 0]/50,
        mode="lines",
        name="freq [pu]",
        line=dict(color="red"),
        yaxis="y2",
        ))
    
    fig.add_vline(
        x=pd.to_datetime(annotations[1]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_vline(
        x=pd.to_datetime(annotations[3]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_vline(
        x=pd.to_datetime(annotations[5]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="#754FC5"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(annotations[1]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[0],
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
        x=pd.to_datetime(annotations[3]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[2],
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-60,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(annotations[5]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=annotations[4],
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="#754FC5", size=12),
        bordercolor="#754FC5",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    if unit == "B": 
        fig.add_vline(
            x=pd.to_datetime(annotations[7]).to_pydatetime(),
            line_width=1,
            line_dash="dash",
            line_color="#754FC5"
            )
        fig.add_annotation(
            x=pd.to_datetime(annotations[7]).to_pydatetime(),
            y=0.9,  # Set a relevant y-axis value
            xref="x",
            yref="paper",
            text=annotations[6],
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
        title=f"Frekvencija tijekom CS agregata {unit} - mjerenje na PMU#{pmu}",
        template="plotly",
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
                    side="right"),
        )
    return fig 

mypath = r"""D:\3_RADNO\_HOPS\2_ZAKUCAC_CS_OP\wams-cs"""
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in files:
    print(file)
    
savepath = r"""C:\Users\larab\Documents\GitHub\admilara.github.io\wams-cs"""

dfs = {}

pmus = ["PMU#324", "PMU#323", "PMU#318"]

for index, file in enumerate(files):
    wams_df = pd.read_excel(mypath + "\\" + file, header=0)
    wams_df["PhasorMs"] = wams_df["PhasorMs"].apply(lambda x: f"{x:03}")
    wams_df["PhasorDate"] = wams_df["PhasorDate"].astype(str)
    wams_df["PhasorDate"] = wams_df["PhasorDate"].str.split(" ").str[0]
    wams_df["PhasorDatetime"] = (wams_df["PhasorDate"] + ' ' + wams_df["PhasorTime"] + "." + wams_df["PhasorMs"].astype(str))
    wams_df['PhasorDatetime'] = pd.to_datetime(wams_df['PhasorDatetime'], format='%Y-%m-%d %H:%M:%S.%f')
    wams_df['PhasorDatetime'] = wams_df["PhasorDatetime"] + timedelta(hours=1)
    
    for pmu in pmus:
        #print("For petlja: ", pmu)
        if any(pmu in col for col in wams_df.columns):
            #print("If uvjet:", pmu)
            pmu_df = wams_df[["PhasorDatetime"] + [col for col in wams_df.columns if pmu in col]].copy()
            dfs[f"{index}_{pmu}"] = pmu_df
            

for key, value in dfs.items():
    agregat = key[0]
    print(agregat)
    pmu = key[-3:]
    print(pmu)
    if agregat == "0":
        unit="D"
        line_volt_txt = "Stavljanje DV 110 kV Zakučac - Meterize 3 pod napon"
        line_volt_dt_str = "2024-12-03 11:46:54"
        line_volt_dt = datetime.strptime(line_volt_dt_str, '%Y-%m-%d %H:%M:%S')
        
        switch_txt = "Uklop sabirničkog rastavljača u polju blok trafoa D"
        switch_dt_str = "2024-12-03 11:44:35"
        switch_dt = datetime.strptime(switch_dt_str, '%Y-%m-%d %H:%M:%S')
        
        off_txt = "Nalog za isključenje DV Zakučac - Meterize 3"
        off_dt_str = "2024-12-03 12:18:59"
        off_dt = datetime.strptime(off_dt_str, '%Y-%m-%d %H:%M:%S')
        annotations = [line_volt_txt, line_volt_dt, switch_txt, switch_dt, 
                       off_txt, off_dt]
    else:
        unit="B"
 
        line_volt_txt = "Stavljanje DV 220 kV Zakučac - Konjsko pod napon"
        line_volt_dt_str = "2024-12-03 14:09:31"
        line_volt_dt = datetime.strptime(line_volt_dt_str, '%Y-%m-%d %H:%M:%S')
        
        switch_txt = "Uklop sabirničkog rastavljača u polju blok trafoa B"
        switch_dt_str = "2024-12-03 14:07:30"
        switch_dt = datetime.strptime(switch_dt_str, '%Y-%m-%d %H:%M:%S')
        
        off_txt = "Nalog za isključenje DV Zakučac - Konjsko"
        off_dt_str = "2024-12-03 14:55:30"
        off_dt = datetime.strptime(off_dt_str, '%Y-%m-%d %H:%M:%S')  
        
        at3_txt = "Energizacija AT3"
        at3_dt_str = "2024-12-03 14:20:25.394"
        at3_dt = datetime.strptime(at3_dt_str, '%Y-%m-%d %H:%M:%S.%f')
        
        if pmu=="318":
            value['PhasorDatetime'] = value['PhasorDatetime'] - timedelta(seconds=7, milliseconds=86.0)
        
        annotations = [line_volt_txt, line_volt_dt, switch_txt, switch_dt, 
                       off_txt, off_dt, at3_txt, at3_dt]
    
    fig1 = naponi_graf(unit, value, pmu, annotations)
    fig2 = struje_graf(unit, value, pmu, annotations)     
    fig3 = frekvencija_graf(unit, value, pmu, annotations)
    
    html1 = pio.to_html(fig1, full_html=False, include_plotlyjs="cdn")
    html2 = pio.to_html(fig2, full_html=False, include_plotlyjs=False)
    html3 = pio.to_html(fig3, full_html=False, include_plotlyjs=False)
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Agregat {unit} - PMU #{pmu}</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h1>Crni start agregata {unit} - PMU#{pmu}</h1>
        <div>{html1}</div>
        <div>{html2}</div>
        <div>{html3}</div>
        </body>
    </html>
    """
    with open(f"{savepath}\\cs-agregata-{unit}-pmu-{pmu}.html", "w") as file:
        file.write(html_content)
    
    
    
    