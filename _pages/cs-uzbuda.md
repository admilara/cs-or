---
layout: default
title: CRNI START - REZULTATI INEM - UZBUDA
description: Kratki pregled podataka Končar INEM-a za pokuse crnog starta u HE Zakučac
---
<style scoped>
table {
  font-size: 13px;
}
</style>
<h1 style="text-align: center; font-family: Helvetica; color: red">03.12.2024. Crni start</h1>
<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: Končar INEM</h2>

Za pokuse crnog starta agregata A, D, B i C u HE Zakučac dostupni su i zapisi iz sustava uzbude,
dostavljeni u obliku RecEx i Watch log datoteka. Trajanje svih RecEx datoteka iznosi **2 minute, 13 sekundi i 56 milisekundi**.
Watch logovi različite su duljine te su one navedene u tablici ispod. 

Veličine u zapisima se razlikuju od datoteke do datoteke - popis oznaka, mjernih jedinica i baznih vrijednosti veličina koje se mogu naći u datotekama nalazi se ispod tablice. 

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica">Zapis</th>
            <th style="text-align:center; font-family: Helvetica">Agregat A</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>
            <th style="text-align:center; font-family: Helvetica">Agregat D</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>>            
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1a-003/">RecEx_ZAKUCA1A_003</a></td>
            <td style="text-align:center">0:02:13.056</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1d-001/">RecEx_ZAKUCA1D_001</a></td>
            <td style="text-align:center">0:02:13.056</td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1a-006/">Watch_ZAKUCA1A_006</a></td>
            <td style="text-align:center">00:02:45.652</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1d-006/">Watch_ZAKUCA1D_006</a></td>            
            <td style="text-align:center">00:03:50.937</td>            
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1a-007/">Watch_ZAKUCA1A_007</a></td>
            <td style="text-align:center">00:03:54.593</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1d-007/">Watch_ZAKUCA1D_007</a></td>            
            <td style="text-align:center">00:03:31.879</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1a-008/">Watch_ZAKUCA1A_008</a></td>
            <td style="text-align:center">00:03:03.001</td>
            <td style="text-align:center">-</td>
            <td style="text-align:center">-</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica">Zapis</th>
            <th style="text-align:center; font-family: Helvetica">Agregat B</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>
            <th style="text-align:center; font-family: Helvetica">Agregat C</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa</th>            
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1b-001/">RecEx_ZAKUCA1B_001</a></td>
            <td style="text-align:center">0:02:13.056</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1c-034/">RecEx_ZAKUCA1C_034</a></td>
            <td style="text-align:center">0:02:13.056</td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1b-001/">Watch_ZAKUCA1B_001</a></td>            
            <td style="text-align:center">00:04:25.700</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1c-007/">Watch_ZAKUCA1C_007</a></td>            
            <td style="text-align:center">00:03:29.419</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1b-012/">Watch_ZAKUCA1B_012</a></td>            
            <td style="text-align:center">00:03:47.137</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1c-008/">Watch_ZAKUCA1C_008</a></td>            
            <td style="text-align:center">00:03:31.128</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1b-013/">Watch_ZAKUCA1B_013</a></td>            
            <td style="text-align:center">00:07:07.524</td>
            <td style="text-align:center">-</td>
            <td style="text-align:center">-</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}



