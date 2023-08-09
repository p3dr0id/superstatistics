import time
import multiprocessing as mp
from scipy.stats import kurtosis
import numpy as np
import matplotlib.pyplot as plt

nprocs = mp.cpu_count()
pool = mp.Pool(processes=nprocs)
print(f'Number of CPU cores: {nprocs}')

# Load Soybean historical prices (macrotrends)
dados_soja = np.loadtxt('soybean-prices-historical-chart-data.csv',
                        delimiter=",",
                        dtype=str,
                        skiprows=1)

precos_soja = dados_soja[:, 1].astype(float)
retornos_soja = np.diff(np.log(precos_soja))

#plt.plot(retornos_soja)
#plt.savefig('retornos')
