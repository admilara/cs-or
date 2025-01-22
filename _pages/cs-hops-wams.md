---
layout: default
title: CRNI START - REZULTATI HOPS WAMS
description: Kratki pregled podataka iz WAMS-a za pokuse crnog starta u HE Zakučac
---
<style scoped>
table {
  font-size: 13px;
}
</style>
<h1 style="text-align: center; font-family: Helvetica; color: red">03.12.2024. Crni start</h1>

<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: HOPS - WAMS</h2>

Od strane HOPS MC Split dostavljeni su podatci o mjerenim veličinama iz tri PMU-a za pokuse 
crnog starta agregata D i agregata B. Za PMU #324 i #318 vremenska sinkronizacija nije pouzdana.
Vizualizacija je prilagođena te su uzeta u obzir vremenska odstupanja zapisa za nesinkronizirane PMU-ove.

* **PMU #318** = HE ZAK VP 220 KONJ
* **PMU #323** = HE ZAK 110 GEN 4 (D)
* **PMU #324** = HE ZAK 220 GEN 2 (B)

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center">Agregat D</th>
            <th style="text-align:center">Agregat B</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/cs-agregata-d-pmu-323/">PMU#318</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/cs-agregata-b-pmu-324/">PMU#324</a></td>
        </tr>
        <tr>
            <td style="text-align:center"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/cs-agregata-b-pmu-318/">PMU#318</a></td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}

Tijekom crnog starta agregata B dodatno je proveden pokus mogućnosti energizacije mrežnog transformatora
AT3 u TS Konjsko, što je vidljivo na vizualizacijama za PMU #323 i #318.


