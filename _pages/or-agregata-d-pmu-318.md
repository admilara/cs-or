---
layout: default
title: WAMS rezultati - PMU#318 - AGREGAT D
---

## WAMS - PMU #318 - Agregat D

#### Otočni rad

Na grafovima ispod prikazana su mjerenja s PMU-a **#318** koji se nalazi u **VP 220 kV Konjsko - Zakučac** za period unutar
kojeg je proveden pokus otočnog rada agregata D u GHE Zakučac.

Sve veličine su preuzete iz dostavljenog csv-a `24-12-04-1048_to_24-12-04-1147_v2.1.2975.csv`.

Vrijeme detekcije OR preuzeto je iz Liste KDR za Regiju Split, koja je dostavljena od strane MC Split.
Prema informacijama HOPS MC Split, GPS nije pouzdan - odstupanje iznosi 7 sekundi, što je vidljivo iz grafova i zabilježenog
vremena prema listi KRD.

<style scoped>
table {
  font-size: 13px;
}
</style>

| Agregat | Vrijeme detekcije OR |  Lokacija             | Vrijeme sinkronizacije | Lokacija          |
| :------ | :------------------: | :------------------:  | :---------------------:|:-----------------:|
|Agregat D| 2024-12-04 11:48:26  | HE ZAK 110 METERIZE/2 | 2024-12-04 12:46:48    | HE ZAK 110 SP W12 |

Iz dostavljene csv datoteke preuzete su veličine:
* PMU#318 &#124;IN&#124; magn [A]
* PMU#318 &#124;UN&#124; magn [pu]
* PMU#318 f(PMU) [Hz]
* PMU#318 P [W]
* PMU#318 Q [VAr]

<div class="wide-graph">
    <iframe src="{{ site.baseurl }}/wams-or/or-agregata-d-pmu-318.html" width="100%" height="800px" frameborder="0"></iframe>
</div>