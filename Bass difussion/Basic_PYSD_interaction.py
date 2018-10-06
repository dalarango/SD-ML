import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pysd 
from Utilities.Toolkit import analytics

# Reading the bass dffusion model

bass = pysd.read_vensim('Bass_dif.mdl')
an = analytics()



# Testing model behavior

run_1 = an.runner(bass, 'run_1')
an.plotter(run_1, ['Customer', 'Potential adopters'])


# Changing constants 

## Emphasizing word to mouth via adoption fraction and neglecting advertisement

run_2 = an.runner(bass,'run_2', params={'Advertising effectiveness': 0.05, 'Adoption fraction': 0.020})
an.plotter(run_2, ['Customer', 'Potential adopters'])


### Comparing the two strategies

plt.figure(figsize=(12,8))
run_1['Customer'].plot(label='Default')
run_2['Customer'].plot(label='Emphasis on word_of_mouth')
plt.legend()

an.compare(runs=[run_1, run_2], param='Customer')

## Sinosoidal random variations to introduce basic seasonality in advertisement


bass.components.advertising_effectiveness = seasonal

run_3 = an.runner(bass, 'run_3')
an.plotter(run_3, ['Customer', 'Potential adopters'])


