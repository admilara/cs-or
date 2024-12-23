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

from os import listdir
from os.path import isfile, join

import pandas as pd


def graf_radna_jalova(df, unit):
    fig = go.Figure()

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

    fig.update_layout(
        title=f"Radna i jalova snaga generatora {unit}",
        xaxis_title="Vrijeme",
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
    return fig


def graf_naponi_gen(df, unit):
    fig = go.Figure()

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

    fig.update_layout(
        title=f"Naponi generatora {unit}",
        xaxis_title="Timestamp",
        yaxis_title="Ug [V]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    return fig


def graf_struje_gen(df, unit):
    fig = go.Figure()

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

    fig.update_layout(
        title=f"Struje generatora {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="Ig [V]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    
    return fig


def graf_uzbuda(df, unit):
    fig = go.Figure()

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

    fig.update_layout(
        title=f"Napon i struja uzbude generatora {unit}",
        xaxis_title="Vrijeme",
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
    return fig


def graf_brzine(df, unit):
    fig = go.Figure()
        
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
    
    fig.update_layout(
        title=f"Frekvencija, brzina vrtnje i zadana brzina vrtnje jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="f, n, nset [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    
    return fig

def graf_frekvencija(df, unit):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"{unit}_FREKVENCIJA_GENERATORA"],
        mode="lines",
        name=f"FREKVENCIJA GENERATORA {unit} [Hz]",
        line=dict(color="purple")
        ))
    
    fig.update_layout(
        title=f"Frekvencija jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="f [Hz]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)        
        )
    return fig

def graf_otvor_pk(df, unit):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_OTVOR_PK"],
        mode="lines",
        name=f"OTVOR PRIVODNOG KOLA {unit} [%]",
        line=dict(color="blue"),
        yaxis="y2"
        ))
    
    fig.update_layout(
        title=f"Otvor privodnog kola jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="y [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    return fig

def graf_otvor_pk(df, unit):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Vrijeme"],
        y=df[f"PB_{unit}_TR_OTVOR_PK"],
        mode="lines",
        name=f"OTVOR PRIVODNOG KOLA {unit} [%]",
        line=dict(color="blue")
        ))
    
    fig.update_layout(
        title=f"Otvor privodnog kola jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="y [%]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
        )
    return fig

def graf_tlak(df, unit):
    fig = go.Figure()
    
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
    
    fig.update_layout(
        title=f"Tlakovi za vrijeme CS jedinice {unit}",
        xaxis_title="Vrijeme",
        yaxis_title="p [bar]",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)        
        )
    return fig

def graf_protok(df, unit):
    fig = go.Figure()
    
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
    
    fig.update_layout(
        title=f"Protok u tlačnom cjevovodu i otvor privodnog kola {unit}",
        xaxis_title="Vrijeme",
        template="plotly_white",
        legend_title="Legenda",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True,
                   title="protok [m<sup>3</sup>/s]",
                   titlefont=dict(color="red"),
                   tickfont=dict(color="red"),
                   side="left"),
        yaxis2=dict(showgrid=True,
                    title="y [%]",
                    titlefont=dict(color="blue"),
                    tickfont=dict(color="blue"),
                    overlaying="y",
                    side="right")
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