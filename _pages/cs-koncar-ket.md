---
layout: default
title: CRNI START - REZULTATI KONČAR PROCIS
description: Kratki pregled podataka Končar KET-a za pokuse crnog starta u HE Zakučac
---


<h1 style="text-align: center; font-family: Helvetica; color: red">03.12.2024. Crni start</h1>
<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: Končar KET - PROCIS</h2>

Za svaki pokus crnog starta grafički su prikazane sljedeće mjerne veličine:

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:left"></th>
            <th style="text-align:center">Oznaka</th>
            <th style="text-align:center">Mjerna jedinica</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left">Radna snaga generatora</td>
            <td style="text-align:center">P</td>
            <td style="text-align:center">[MW]</td>
        </tr>
        <tr>
            <td style="text-align:left">Jalova snaga generatora</td>
            <td style="text-align:center">Q</td>
            <td style="text-align:center">[Mvar]</td>
        </tr>
        <tr>
            <td style="text-align:left">Naponi generatora</td>
            <td style="text-align:center">UL1L2, UL2L3, UL3L1</td>
            <td style="text-align:center">[V]</td>
        </tr>
        <tr>
            <td style="text-align:left">Struje generatora</td>
            <td style="text-align:center">IL1, IL2, IL3</td>
            <td style="text-align:center">[A]</td>
        </tr>
        <tr>
            <td style="text-align:left">Napon uzbude</td>
            <td style="text-align:center">Uf</td>
            <td style="text-align:center">[V]</td>
        </tr>
        <tr>
            <td style="text-align:left">Struja uzbude</td>
            <td style="text-align:center">If</td>
            <td style="text-align:center">[A]</td>
        </tr>
        <tr>
            <td style="text-align:left">Brzina vrtnje, zadana brzina vrtnje, frekvencija</td>
            <td style="text-align:center"></td>
            <td style="text-align:center">[%]</td>
        </tr>
        <tr>
            <td style="text-align:left">Frekvencija</td>
            <td style="text-align:center">f</td>
            <td style="text-align:center">[Hz]</td>
        </tr>
        <tr>
            <td style="text-align:left">Otvor privodnog kola</td>
            <td style="text-align:center">y</td>
            <td style="text-align:center">[%]</td>
        </tr>
        <tr>
            <td style="text-align:left">Tlak u spirali turbine i tlak u tlačnom cjevovodu</td>
            <td style="text-align:center">p</td>
            <td style="text-align:center">[bar]</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}


1. Crni start - proizvodna jedinica A - [rezultati]({{ site.baseurl }}/procis-cs-gen-a/)
2. Crni start - proizvodna jedinica D - [rezultati]({{ site.baseurl }}/procis-cs-gen-d/)
3. Crni start - proizvodna jedinica B - [rezultati]({{ site.baseurl }}/procis-cs-gen-b/)
4. Crni start - proizvodna jedinica C - [rezultati]({{ site.baseurl }}/procis-cs-gen-c/)
