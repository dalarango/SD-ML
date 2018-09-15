import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pysd 

# Reading the bass dffusion model

bass = pysd.read_vensim('Bass_dif.mdl')

# Testing model behavior

run_1 = pd.DataFrame(bass.run())

plt.figure(figsize=(12,8))
run_1['Customer'].plot()
run_1['Potential adopters'].plot()

# Changing constants 

## Emphasizing word to mouth via adoption fraction and neglecting advertisement

run_2 = pd.DataFrame(bass.run(params={'Advertising effectiveness': 0.05, 'Adoption fraction': 0.020}))

plt.figure(figsize=(12,8))
run_2['Customer'].plot(label='Customers')
run_2['Potential adopters'].plot(label='Potential adopters')
plt.legend()

### Comparing the two strategies

plt.figure(figsize=(12,8))
run_1['Customer'].plot(label='Default')
run_2['Customer'].plot(label='Emphasis on word_of_mouth')
plt.legend()

## Sinosoidal random variations to introduce basic seasonality in advertisement



def seasonal ():
    mark_eff = np.sin(np.random.normal(loc=0.05, scale=0.15))
    #base_eff = bass.components.advertising_effectiveness()
    return mark_eff


bass.components.advertising_effectiveness = seasonal

run_3 =bass.run()

run_3['Customer'].plot(label='Customers')
run_3['Potential adopters'].plot(label='Potential customers')
plt.legend()

