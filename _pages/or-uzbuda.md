---
layout: default
title: OTOČNI RAD - REZULTATI INEM - UZBUDA
description: Kratki pregled podataka Končar INEM-a za pokuse otočnog rada u HE Zakučac
---

<style scoped>
table {
  font-size: 13px;
}
</style>

<h1 style="text-align: center; font-family: Helvetica; color: red">04.12.2024. Otočni rad</h1>
<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: Končar INEM</h2>

Za pokuse otočnog rada agregata A, D, B i C u HE Zakučac dostupni su i zapisi iz sustava uzbude,
dostavljeni u obliku RecEx i Watch log datoteka. Trajanje RecEx datoteka iznosi **2 minute, 13 sekundi i 56 milisekundi**.
Watch logovi različite su duljine te su one navedene u tablici ispod. 

Veličine u zapisima se razlikuju od datoteke do datoteke - popis oznaka, mjernih jedinica i baznih vrijednosti veličina koje se mogu naći u datotekama nalazi se ispod tablice. 

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica">Zapis</th>
            <th style="text-align:center; font-family: Helvetica">Agregat A</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa [min]</th>
            <th style="text-align:center; font-family: Helvetica">Napomena</th>                        
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1a-006/">RecEx_ZAKUCA1A_006</a></td>
            <td style="text-align:center">02:13.056</td>
            <td style="text-align:center">Zapis odvajanja u otok. Vremensko odstupanje originalnog zapisa od utvrđenog trenutka odvajanja 58 minuta i 21.681 sekundi.</td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1a-031/">Watch_ZAKUCA1A_031</a></td>
            <td style="text-align:center">01:49.757</td>
            <td style="text-align:center">Sinkronizacija na mrežu. Odstupanje zapisa 19.407 sekundi.</td>                      
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
            <th style="text-align:center; font-family: Helvetica">Agregat D</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa [min]</th>
            <th style="text-align:center; font-family: Helvetica">Napomena</th>                        
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1d-002/">RecEx_ZAKUCA1D_002</a></td>
            <td style="text-align:center">02:13.056</td>
            <td style="text-align:center">Zapis odvajanja u otok. Vremensko odstupanje zapisa od utvrđenog trenutka odvajanja 15 minuta i 17.654 sekunde.</td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1d-022/">Watch_ZAKUCA1D_022</a></td>            
            <td style="text-align:center">04:30.850</td> 
            <td style="text-align:center">Sinkronizacija na mrežu. Odstupanje zapisa: 20.400 sekunde.</td>         
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}



{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center; font-family: Helvetica; color: white">Zapis</th>
            <th style="text-align:center; font-family: Helvetica; color: white">Agregat B</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa [min]</th>
            <th style="text-align:center; font-family: Helvetica; color: white">Agregat C</th>
            <th style="text-align:center; font-family: Helvetica">Trajanje zapisa [min]</th>            
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">RECEX LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/recex-zakuca1b-002/">RecEx_ZAKUCA1B_002</a></td>
            <td style="text-align:center">02:13.056</td>
            <td style="text-align:center">-</td>
            <td style="text-align:center">-</td>
        </tr>
        <tr>
            <td style="text-align:center">WATCH LOG</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1b-031/">Watch_ZAKUCA1B_031</a></td>            
            <td style="text-align:center">03:49.270</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1c-013/">Watch_ZAKUCA1C_013</a></td>            
            <td style="text-align:center">02:14.407</td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center">-</td>            
            <td style="text-align:center">-</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/watch-zakuca1c-022/">Watch_ZAKUCA1C_022</a></td>            
            <td style="text-align:center">00:46.877</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}






