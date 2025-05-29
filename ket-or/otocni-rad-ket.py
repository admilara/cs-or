# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:41:59 2024

@author: larab
"""

import plotly
import plotly.graph_objects as go
import plotly.io as pio
#import plotly.dashboard_objs as dashboard_objs
import IPython.display
#from IPyhton.display import Image
import re
from os import listdir
from os.path import isfile, join
from datetime import timedelta
import pandas as pd

otocni_rad = {"A": ("2024-12-04 09:12:58", "HE ZAK 110 METERIZE/2", "2024-12-04 10:20:29", "HE ZAK 110 SP W12"),
              "D": ("2024-12-04 11:48:26", "HE ZAK 110 METERIZE/2", "2024-12-04 12:46:48", "HE ZAK 110 SP W12"),
              "B": ("2024-12-04 14:24:28", "HE ZAK 110 METERIZE/2", "2024-12-04 15:25:27", "HE ZAK 110 SP W12"),
              "C": ("2024-12-04 16:27:27", "HE ZAK 110 METERIZE/2", "2024-12-04 17:03:18", "HE ZAK 220 SP W12")}

def graf_radna_jalova(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_RADNA_SNAGA_GENERATORA"],
        mode="lines",
        name=f"RADNA SNAGA GENERATORA {unit} [MW]",
        line=dict(color="red")
        ))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_JALOVA_SNAGA_GENERATORA"],
        mode="lines",
        name=f"JALOVA SNAGA GENERATORA {unit} [Mvar]",
        line=dict(color="blue"),
        yaxis="y2"
        ))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {otocni_rad[unit][1]}",
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
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {otocni_rad[unit][3]}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="magenta", size=12),
        bordercolor="magenta",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
        
    fig.update_layout(
        title=f"Radna i jalova snaga generatora {unit}",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="Pg [MW]",
                   titlefont=dict(color="red"),
                   tickfont=dict(color="red")),
        yaxis2=dict(showgrid=True,
                    title="Qg [Mvar]",
                    titlefont=dict(color="blue"),
                    tickfont=dict(color="blue"),
                    overlaying="y",
                    side="right")
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        legend=dict(
            orientation="h",      
            yanchor="bottom",
            y=-0.3,               
            xanchor="center",
            x=0.5                 
            ),
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True)
    )
    
    return fig


def graf_naponi_gen(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_NAPON_GENERATORA_UL1L2"],
        mode="lines",
        name=f"NAPON GENERATORA {unit} - UL1L2 [V]",
        line=dict(color="blue")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_NAPON_GENERATORA_UL2L3"],
        mode="lines",
        name=f"NAPON GENERATORA {unit} - UL2L3 [V]",
        line=dict(color="red")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_NAPON_GENERATORA_UL3L1"],
        mode="lines",
        name=f"NAPON GENERATORA {unit} - UL3L1 [V]",
        line=dict(color="green")))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.update_layout(
        title=f"Naponi generatora {unit}",
        yaxis_title="Ug [V]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        legend=dict(
            orientation="h",      
            yanchor="bottom",
            y=-0.3,               
            xanchor="center",
            x=0.5                 
            ),
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True, range=[14000,17500])
    )
    
    return fig


def graf_struje_gen(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_STRUJA_GENERATORA_IL1"],
        mode="lines",
        name=f"STRUJA GENERATORA {unit} - IL1 [A]",
        line=dict(color="blue")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_STRUJA_GENERATORA_IL2"],
        mode="lines",
        name=f"STRUJA GENERATORA {unit} - IL2 [A]",
        line=dict(color="red")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_STRUJA_GENERATORA_IL3"],
        mode="lines",
        name=f"STRUJA GENERATORA {unit} - IL3 [A]",
        line=dict(color="green")))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.update_layout(
        title=f"Struje generatora {unit}",
        yaxis_title="Ig [V]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0.85,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        legend=dict(
            orientation="h",      
            yanchor="bottom",
            y=-0.3,               
            xanchor="center",
            x=0.5                 
            ),
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True)
    )
    
    return fig


def graf_uzbuda(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_NAPON_UZBUDE"],
        mode="lines",
        name=f"NAPON UZBUDE GENERATORA {unit} [V]",
        line=dict(color="blue")))

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_STRUJA_UZBUDE"],
        mode="lines",
        name=f"STRUJA UZBUDE GENERATORA {unit} [A]",
        line=dict(color="red"),
        yaxis="y2"))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.update_layout(
        title=f"Napon i struja uzbude generatora {unit}",
        yaxis_title="Napon i struja uzbude",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="Uf [V]",
                   titlefont=dict(color="blue"),
                   tickfont=dict(color="blue")),
        yaxis2=dict(showgrid=True,
                    title="If [A]",
                    titlefont=dict(color="red"),
                    tickfont=dict(color="red"),
                    overlaying="y",
                    side="right")
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0.85,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        legend=dict(
            orientation="h",      
            yanchor="bottom",
            y=-0.3,               
            xanchor="center",
            x=0.5                 
            ),
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True)
    )
    
    return fig


def graf_brzine(df, unit):
    fig = go.Figure()
    
    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_FREKVENCIJA_GENERATORA"]/50*100,
        mode="lines",
        name=f"FREKVENCIJA GENERATORA {unit} [%]",
        line=dict(color="blue")
        ))
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_ZADANA_BRZ"],
        mode="lines",
        name=f"ZADANA BRZINA VRNJE GENERATORA {unit} [%]",
        line=dict(color="black")
        ))
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_BRZINA_VRTNJE"],
        mode="lines",
        name=f"BRZINA VRTINJE GENERATORA {unit} [%]",
        line=dict(color="green")
        ))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    fig.update_layout(
        title=f"Frekvencija, brzina vrtnje i zadana brzina vrtnje jedinice {unit}",
        yaxis_title="f, n, nset [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0.85,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    y1_data = df[f"{unit}_FREKVENCIJA_GENERATORA"]/50*100
    y1_min = y1_data.min()
    y1_max = y1_data.max()
    
    y2_data = df[f"PB_{unit}_TR_ZADANA_BRZ"]
    y2_min = y2_data.min()
    y2_max = y2_data.max()

    y3_data = df[f"PB_{unit}_TR_BRZINA_VRTNJE"]
    y3_min = y3_data.min()
    y3_max = y3_data.max()

    y_min = min([y1_min, y2_min, y3_min])
    y_max = max([y1_max, y2_max, y3_max])
    
    padding = (y_max - y_min) * 0.5
    y_range = [y_min - padding, y_max + padding]

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        legend=dict(
            orientation="h",      
            yanchor="bottom",
            y=-0.3,               
            xanchor="center",
            x=0.5                 
            ),
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True, range=[80,110])
    )
    return fig

def graf_frekvencija(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)
    
    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    fig.add_annotation(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"ODVAJANJE: {otocni_rad[unit][1]}",
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
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        y=0.9,  # Set a relevant y-axis value
        xref="x",
        yref="paper",
        text=f"RESINKRONIZACIJA: {otocni_rad[unit][3]}",
        showarrow=True,
        arrowhead=2,
        ax=20,  # Arrow shift in x direction
        ay=-40,  # Arrow shift in y direction
        font=dict(color="magenta", size=12),
        bordercolor="magenta",
        borderwidth=1,
        bgcolor="rgba(255,255,255,0.7)"
        )
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_FREKVENCIJA_GENERATORA"],
        mode="lines",
        name=f"FREKVENCIJA GENERATORA {unit} [Hz]",
        line=dict(color="purple")
        ))
    
    fig.update_layout(
        title=f"Frekvencija jedinice {unit}",
        yaxis_title="f [Hz]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)        
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0.85,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True, range=[40,60])
    )
    
    return fig

def graf_otvor_pk(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_OTVOR_PK"],
        mode="lines",
        name=f"OTVOR PRIVODNOG KOLA {unit} [%]",
        line=dict(color="blue"),
        yaxis="y2"
        ))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    fig.update_layout(
        title=f"Otvor privodnog kola jedinice {unit}",
        yaxis_title="y [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   range=[20,70])
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0.85,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    fig.update_layout(
        title=f"Frekvencija jedinice {unit}",
        yaxis_title="f [Hz]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True)
    )
    
    return fig

def graf_otvor_pk(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)

    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_OTVOR_PK"],
        mode="lines",
        name=f"OTVOR PRIVODNOG KOLA {unit} [%]",
        line=dict(color="blue")
        ))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    y_data = df[f"PB_{unit}_TR_OTVOR_PK"]
    y_min = y_data.min()
    y_max = y_data.max()

    padding = (y_max - y_min) * 0.5
    y_range = [y_min - padding, y_max + padding]
    
    fig.update_layout(
        title=f"Otvor privodnog kola jedinice {unit}",
        yaxis_title="y [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   range=y_range)
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0.85,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True)
    )
    
    return fig

def graf_tlak(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_TLAK_U_SPIRALI_TURBINE"],
        mode="lines",
        name=f"TLAK U SPIRALI TURBINE JEDINICE {unit} [bar]",
        line=dict(color="blue")
        ))
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_TLAK_U_TLACNOM_CJEVOVODU"],
        mode="lines",
        name=f"{unit} TLAK U TLACNOM CJEVOVODU [bar]",
        line=dict(color="red")
        ))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    fig.update_layout(
        title=f"Tlakovi za vrijeme OR jedinice {unit}",
        yaxis_title="p [bar]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)        
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0.85,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    y1_data = df[f"{unit}_TLAK_U_SPIRALI_TURBINE"]
    y1_min = y1_data.min()
    y1_max = y1_data.max()
    
    y2_data = df[f"{unit}_TLAK_U_TLACNOM_CJEVOVODU"]
    y2_min = y2_data.min()
    y2_max = y2_data.max()

    y_min = min([y1_min, y2_min])
    y_max = max([y1_max, y2_max])
    
    padding = (y_max - y_min) * 0.5
    y_range = [y_min - padding, y_max + padding]

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        legend=dict(
            orientation="h",      
            yanchor="bottom",
            y=-0.3,               
            xanchor="center",
            x=0.5                 
            ),
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True, range=y_range)
    )
    
    return fig

def graf_protok(df, unit):
    fig = go.Figure()

    start_time = pd.to_datetime(otocni_rad[unit][0]) - timedelta(minutes=10)
    end_time = pd.to_datetime(otocni_rad[unit][2]) + timedelta(minutes=5)
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"ZK_Agr_{unit}_Protok_tl_cjevovod"],
        mode="lines",
        name=f"PROTOK TLAČNOG CJEVOVODA {unit} [m<sup>3</sup>/s]",
        line=dict(color="red")
        ))
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_OTVOR_PK"],
        mode="lines",
        name=f"OTVOR PRIVODNOG KOLA {unit} [%]",
        line=dict(color="blue"),
        yaxis="y2"
        ))

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][0]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )

    fig.add_vline(
        x=pd.to_datetime(otocni_rad[unit][2]).to_pydatetime(),
        line_width=1,
        line_dash="dash",
        line_color="magenta"
        )
    
    y1_data = df[f"ZK_Agr_{unit}_Protok_tl_cjevovod"]
    y1_min = y1_data.min()
    y1_max = y1_data.max()

    padding1 = (y1_max - y1_min) * 0.5
    y1_range = [y1_min - padding1, y1_max + padding1]
    
    y2_data = df[f"PB_{unit}_TR_OTVOR_PK"]
    y2_min = y2_data.min()
    y2_max = y2_data.max()

    padding2 = (y2_max - y2_min) * 0.5
    y2_range = [y2_min - padding2, y2_max + padding2]

    
    fig.update_layout(
        title=f"Protok u tlačnom cjevovodu i otvor privodnog kola {unit}",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="protok [m<sup>3</sup>/s]",
                   titlefont=dict(color="red"),
                   tickfont=dict(color="red"),
                   side="left", 
                   range=y1_range),
        yaxis2=dict(showgrid=True,
                    title="y [%]",
                    titlefont=dict(color="blue"),
                    tickfont=dict(color="blue"),
                    overlaying="y",
                    side="right",
                    range=y2_range)
        )
    
    relevant_pss = pss_df[
        (pss_df["generator"] == unit) &
        (pss_df["datetime"] >= start_time) &
        (pss_df["datetime"] <= end_time)
    ]

    # Add annotations for each PSS ON/OFF event
    for _, row in relevant_pss.iterrows():
        fig.add_vline(
            x=row["datetime"],
            line_width=1,
            line_dash="dot",
            line_color="blue" if row["status"] == "PSS ON" else "red"
        )
        fig.add_annotation(
            x=row["datetime"],
            y=0.85,
            xref="x",
            yref="paper",
            text=row["status"],
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30,
            font=dict(color="blue" if row["status"] == "PSS ON" else "red", size=11),
            bordercolor="black",
            borderwidth=1,
            bgcolor="rgba(255,255,255,0.8)"
        )

    fig.update_layout(
        template="plotly_white",
        legend_title="Legenda",
        legend=dict(
            orientation="h",      
            yanchor="bottom",
            y=-0.3,               
            xanchor="center",
            x=0.5                 
            ),
        xaxis=dict(showgrid=True, range=[start_time, end_time]),
        yaxis=dict(showgrid=True)
    )
    
    return fig


mypath = "D:\\3_RADNO\\_HOPS\\2_ZAKUCAC_CS_OP\\KET"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in files:
    print(file)
    print("\n")

dfs = []

crni_start_A_df = pd.read_excel(mypath+'\\'+files[6], header=1)
crni_start_A_df = crni_start_A_df.drop(0)
crni_start_A_df["Vrijeme"] = pd.to_datetime(crni_start_A_df["Vrijeme"], format="%d-%m-%Y %H:%M:%S", dayfirst=True)
dfs.append(crni_start_A_df)

crni_start_B_df = pd.read_excel(mypath+'\\'+files[7], header=1)
crni_start_B_df["Vrijeme"] = pd.to_datetime(crni_start_B_df["Vrijeme"], format="%d-%m-%Y %H:%M:%S", dayfirst=True)
dfs.append(crni_start_B_df)

crni_start_C_df = pd.read_excel(mypath+'\\'+files[8], header=1)
crni_start_C_df["Vrijeme"] = pd.to_datetime(crni_start_C_df["Vrijeme"], format="%d-%m-%Y %H:%M:%S", dayfirst=True)
dfs.append(crni_start_C_df)

crni_start_D_df = pd.read_excel(mypath+'\\'+files[9], header=1)
crni_start_D_df["Vrijeme"] = pd.to_datetime(crni_start_D_df["Vrijeme"], format="%d-%m-%Y %H:%M:%S", dayfirst=True)
dfs.append(crni_start_D_df)

units=["A", "B", "C", "D"]

# =============================================================================
#                   PSS ANNOTATIONS - PRORADE
# =============================================================================

pss_path = "C:/Users/larab/Documents/GitHub/cs-or/cs-or/ket-or/pss-on-off.txt"

# Load and parse the file
with open(pss_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Extract and structure the data
parsed_data = []
for line in lines:
    parts = line.strip().split('\t')
    if len(parts) == 3:
        timestamp, generator, message = parts
        status = "PSS ON" if "Uključen" in message and "NESTANAK" not in message else "PSS OFF"
        parsed_data.append({
            "datetime": pd.to_datetime(timestamp, format="%d-%m-%Y %H:%M:%S:%f"),
            "generator": generator,
            "status": status
        })


pss_df = pd.DataFrame(parsed_data)

# Convert datetime to pandas datetime
pss_df['datetime'] = pd.to_datetime(pss_df['datetime'], format="%Y-%m-%d %H:%M:%S:%f")


# =============================================================================
#                       SLIKE
# =============================================================================

for unit, df in zip(units, dfs):
    # GENERATOR A - RADNA I JALOVA SNAGA
    fig = graf_radna_jalova(df, unit)

    #GENERATOR A - NAPONI
    fig2 = graf_naponi_gen(df, unit)

    #GENERATOR A - STRUJE
    fig3 = graf_struje_gen(df, unit)

    #GENERATOR A - UZBUDA
    fig4 = graf_uzbuda(df, unit)

    #GENERATOR A - ZADANA BRZINA, BRZINA VRTNJE, FREKVENCIJA 
    fig5 = graf_brzine(df, unit)

    #GENERATOR A - OTVOR PRIVODNOG KOLA
    fig6 = graf_otvor_pk(df, unit)

    #GENERATOR A - FREKVENCIJA
    fig7 = graf_frekvencija(df, unit)

    #GENERATOR A - TLAK U SPIRALI I CJEVOVODU
    fig8 = graf_tlak(df, unit)

    #GENERATOR A - PROTOK I OTVOR PK
    fig9 = graf_protok(df, unit)

    html1 = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    html2 = pio.to_html(fig2, full_html=False, include_plotlyjs=False)
    html3 = pio.to_html(fig3, full_html=False, include_plotlyjs=False)
    html4 = pio.to_html(fig4, full_html=False, include_plotlyjs=False)
    html5 = pio.to_html(fig5, full_html=False, include_plotlyjs=False)
    html6 = pio.to_html(fig6, full_html=False, include_plotlyjs=False)
    html7 = pio.to_html(fig7, full_html=False, include_plotlyjs=False)
    html8 = pio.to_html(fig8, full_html=False, include_plotlyjs=False)
    html9 = pio.to_html(fig9, full_html=False, include_plotlyjs=False)

    html_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>gen-{unit}-otocni-rad</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h2>Vizualizacija podataka - PROCIS - Otočni rad</h2>
        <div>{html1}</div>
        <div>{html2}</div>
        <div>{html3}</div>
        <div>{html4}</div>
        <div>{html5}</div>
        <div>{html6}</div>
        <div>{html7}</div>
        <div>{html8}</div>
        <div>{html9}</div>
    </body>
    </html>
    """
    
    # Save the HTML page
    with open(f"procis-or-gen-{unit}.html", "w") as f:
        f.write(html_page)
    
    print(f"Dashboard saved as procis-or-gen-{unit}.html")