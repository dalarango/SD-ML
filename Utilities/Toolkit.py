import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pysd



class analytics:

    def runner(self, model, run_name, params=None):
        run = pd.DataFrame(model.run(params=params))
        run.name = run_name
        return run

    def plotter(self, run, params):
        plt.figure(figsize=(12,8))
        for j in range(len(params)):
            run[params[j]].plot(label=str(params[j]))
        plt.legend()
        return plt.plot()

    def compare(self, runs, param):
        plt.figure(figsize=(12,8))
        for r in range(len(runs)):
            runs[r][param].plot(label=runs[r].name)
        plt.legend()
        return plt.plot()

    def seasonal(self):
    	mark_eff = np.sin(np.random.normal(loc=0.05, scale=0.15))
    	#base_eff = bass.components.advertising_effectiveness()
    	return mark_eff


