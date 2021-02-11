#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone

from Random import Random as rand


N = 10000
lam=2
date =  str(datetime.now().astimezone())[0:19].replace(' ','_')
samples = []

x = rand()

for i in range(N):
    samples.append(x.Poisson(lam=lam))


fig, ax = plt.subplots(figsize=(11,8.5))

ax.hist(samples,histtype='stepfilled',hatch='//',fill=False,label=f"Lambda = {lam}")

ax.set_xlabel("Value", fontsize=22)
ax.set_ylabel("Frequency", fontsize =22)
ax.set_title(f"Poisson Distribution for {N} Samples", fontsize = 26)

ax.legend(fontsize=22)

plt.tight_layout()


plt.savefig(f"./poisson_lam{lam}_{date}.pdf", orientation='landscape', format='pdf')
