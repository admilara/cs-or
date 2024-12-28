---
layout: default
title: WAMS rezultati - PMU#323 - AGREGAT D
---

## WAMS - PMU #323 - Agregat D

#### Otočni rad

Na grafovima ispod prikazana su mjerenja s PMU-a **#323** koji se nalazi na **GEN D (110 kV) u HE Zakučac** za period unutar
kojeg je proveden pokus otočnog rada agregata D u GHE Zakučac.

Sve veličine su preuzete iz dostavljenog csv-a `24-12-04-1048_to_24-12-04-1147_v2.1.2975.csv`.

Vrijeme detekcije OR preuzeto je iz Liste KDR za Regiju Split, koja je dostavljena od strane MC Split.
Prema informacijama HOPS MC Split, GPS nije pouzdan te su moguća vremenska odstupanja od stvarnog događaja.

<style scoped>
table {
  font-size: 13px;
}
</style>

| Agregat | Vrijeme detekcije OR |  Lokacija             | Vrijeme sinkronizacije | Lokacija          |
| :------ | :------------------: | :------------------:  | :---------------------:|:-----------------:|
|Agregat D| 2024-12-04 11:48:26  | HE ZAK 110 METERIZE/2 | 2024-12-04 12:46:48    | HE ZAK 110 SP W12 |

Iz dostavljene csv datoteke preuzete su veličine:
* PMU#323 |IN| magn [A]
* PMU#323 |UN| magn [pu]
* PMU#323 f(PMU) [Hz]
* PMU#323 P [W]
* PMU#323 Q [VAr]

<div class="wide-graph">
    <iframe src="{{ site.baseurl }}/wams-or/or-agregata-d-pmu#323.html" width="100%" height="800px" frameborder="0"></iframe>
</div>