---
layout: default
title: OTOČNI RAD - REZULTATI HOPS WAMS
description: Kratki pregled podataka iz WAMS-a za pokuse otočnog rada u HE Zakučac
---

<h1 style="text-align: center; font-family: Helvetica; color: blue">04.12.2024. Otočni rad</h1>

<h2 style="text-align: center; font-family: Helvetica; color: blue">Podatci: HOPS WAMS</h2>

Od strane HOPS-a dostavljeni su i podatci za četiri PMU-a za četiri promatrana perioda - po 
jedan za svaki obavljeni pokus otočnog rada. Vizualizacije su dostupne na hyperlinkovima ispod.
* 24-12-04-0812_to_24-12-04-0921_v2.1.2975.csv - otočni rad agregata A
* 24-12-04-1048_to_24-12-04-1147_v2.1.2975.csv - otočni rad agregata D
* 24-12-04-1324_to_24-12-04-1426_v2.1.2975.csv - otočni rad agregata B
* 24-12-04-1527_to_24-12-04-1603_v2.1.2975.csv - otočni rad agregata C

Četiri dostupna PMU-a su:
* **PMU #14** = RHE VEL VP 400 KONJ
* **PMU #318** = HE ZAK VP 220 KONJ
* **PMU #323** = HE ZAK 110 GEN 4 (D)
* **PMU #324** = HE ZAK 220 GEN 2 (B)

Za sva četiri agregata promatran je PMU #318, koji se nalazi u VP 220 kV Konjsko - Zakučac.
Od generatora u HE Zakučac, PMU je ugrađen na generatore B (220 kV) i D (110 kV) te je za otočni rad
ta dva agregata dostupna i vizualizacija njihovih pripadajućih PMU-ova.

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:left">Agregat</th>
            <th style="text-align:center">Rezultati</th>
            <th style="text-align:left">Agregat</th>
            <th style="text-align:center">Rezultati</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left">Agregat A</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/or-agregata-a-pmu-318/">A - PMU#318</a></td>
            <td style="text-align:left">Agregat C</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/or-agregata-c-pmu-318/">C - PMU#318</a></td>
        </tr>
        <tr>
            <td style="text-align:left">Agregat D</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/or-agregata-d-pmu-318/">D - PMU#318</a></td>
            <td style="text-align:left">Agregat B</td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/or-agregata-b-pmu-318/">B - PMU#318</a></td>
        </tr>
        <tr>
            <td style="text-align:left"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/or-agregata-d-pmu-323/">D - PMU#323</a></td>
            <td style="text-align:left"></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/or-agregata-b-pmu-324/">B - PMU#324</a></td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}