---
layout: default
title: Navigacija
description: Navigacijska stranica za rezultate obrade
---

# Obrada rezultata

Ovo je navigacijska stranica za rezultate obrade dostavljenih podataka nakon pokusa
crnog starta i otočnog rada koji su provedeni na sve četiri proizvodne jedinice A, D, B i C u GHE Zakučac
03.12. i 04.12.2024. Hyperlinkovi vode na grafove prema podatcima koji su navedeni. 


<h1 style="text-align: center; font-family: Helvetica; color: red">03.12.2024. Crni start</h1>

<h2 style="text-align: center; font-family: Helvetica; color: red">Podatci: Končar KET - PROCIS</h2>

Za svaki pokus crnog starta grafički su prikazane sljedeće mjerne veličine:

<style scoped>
table {
  font-size: 13px;
}
</style>

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


<h1 style="text-align: center; font-family: Helvetica; color: blue">04.12.2024. Otočni rad</h1>

<h2 style="text-align: center; font-family: Helvetica; color: blue">Podatci: Končar KET - PROCIS</h2>

Za svaki pokus otočnog rada grafički su prikazane sljedeće mjerne veličine:
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
        <tr>
            <td style="text-align:left">Protok u tlačnom cjevovodu</td>
            <td style="text-align:center">Q</td>
            <td style="text-align:center">[m³/s]</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}


1. Otočni rad - proizvodna jedinica A - [rezultati]({{ site.baseurl }}/procis-or-gen-a/)
2. Otočni rad - proizvodna jedinica D - [rezultati]({{ site.baseurl }}/procis-or-gen-d/)
3. Otočni rad - proizvodna jedinica B - [rezultati]({{ site.baseurl }}/procis-or-gen-b/)
4. Otočni rad - proizvodna jedinica C - [rezultati]({{ site.baseurl }}/procis-or-gen-c/)

<h2 style="text-align: center; font-family: Helvetica; color: blue">Podatci: HOPS NM - konzum</h2>

Dostupne su mjerne veličine P, Q, I, U i položaj regulacijske sklopke. 
Ovisno o stanici mjerenja snage su ili na 110 kV ili na 35 kV naponskoj razini.

Dostavljeni su podatci mjerenja svih trafostanica koje su bile uključene u pokuse otočnog rada, vizualizacija je dana za sva četiri agregata.

<style scoped>
table {
  font-size: 16px;
}
</style>

{% capture raw_html %}
<table>
    <thead>
        <tr>
            <th style="text-align:center">TS HE Zakučac - TR1</th>
            <th style="text-align:center">TS Kaštela - TR2</th>
            <th style="text-align:center">TS Sinj - TR1 i TR2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-zakucac-or-gen-a/">GEN A - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-kastela-tr2-or-gen-a/">GEN A - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-sinj-or-gen-a/">GEN A - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-zakucac-or-gen-d/">GEN D - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-kastela-tr2-or-gen-d/">GEN D - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-sinj-or-gen-d/">GEN D - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-zakucac-or-gen-b/">GEN B - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-kastela-tr2-or-gen-b/">GEN B - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-sinj-or-gen-b/">GEN B - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-zakucac-or-gen-c/">GEN C - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-kastela-tr2-or-gen-c/">GEN C - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-sinj-or-gen-c/">GEN C - OR</a></td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th style="text-align:center">TS Dugopolje - TR1 i TR2</th>
            <th style="text-align:center">TS Meterize - TR1 i TR2</th>
            <th style="text-align:center">TS Vrboran - TR1 i TR2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-dugopolje-or-gen-a/">GEN A - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-meterize-or-gen-a/">GEN A - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-vrboran-or-gen-a/">GEN A - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-dugopolje-or-gen-d/">GEN D - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-meterize-or-gen-d/">GEN D - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-vrboran-or-gen-d/">GEN D - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-dugopolje-or-gen-b/">GEN B - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-meterize-or-gen-b/">GEN B - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-vrboran-or-gen-b/">GEN B - OR</a></td>
        </tr>
        <tr>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-dugopolje-or-gen-c/">GEN C - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-meterize-or-gen-c/">GEN C - OR</a></td>
            <td style="text-align:center"><a href="{{ site.baseurl }}/ts-vrboran-or-gen-c/">GEN C - OR</a></td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}

Kako bi se snaga proizvodnje pojedinih agregata usporedila s konzumom u otoku, 
dana je sumarna karakteristika radne i jalove snage konzuma u trafostanicama u otoku.
Grafovi prikazuju odvojeno radnu snagu i jalovu snagu za svaki pojedini agregat.

* **Sumarna karakteristika** - [rezultati]({{ site.baseurl }}/suma-konzum-or/)


<h2 style="text-align: center; font-family: Helvetica; color: blue">Podatci: HOPS NM - mjesta odvajanja</h2>

Mjesto odvajanja za sva četiri pokusa otočnog rada bio je DV 110 kV HE Zakučac - Meterize II.
Na mjestu odvajanja, s obje strane dalekovoda, mjerene su sljedeće veličine:

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
            <td style="text-align:left">Struja</td>
            <td style="text-align:center">I</td>
            <td style="text-align:center">[A]</td>
        </tr>
        <tr>
            <td style="text-align:left">Radna snaga</td>
            <td style="text-align:center">P</td>
            <td style="text-align:center">[MW]</td>
        </tr>
        <tr>
            <td style="text-align:left">Jalova snaga</td>
            <td style="text-align:center">Q</td>
            <td style="text-align:center">[Mvar]</td>
        </tr>
        <tr>
            <td style="text-align:left">Napon</td>
            <td style="text-align:center">U</td>
            <td style="text-align:center">[kV]</td>
        </tr>
    </tbody>
</table>
{% endcapture %}
{{ raw_html }}

Rezultati su prikazani odvojeno za sva četiri agregata:
* [GEN A - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-a/)
* [GEN D - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-d/)
* [GEN B - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-b/)
* [GEN C - MJESTO ODVAJANJA]({{ site.baseurl }}/mjesto-odvajanja-gen-c/)


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
