import time
from scipy.stats import kurtosis
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt

nprocs = mp.cpu_count()
pool = mp.Pool(processes=nprocs)
print(f'Number of CPU cores: {nprocs}')

# Load Soybean historical prices (macrotrends)
dados_soja = np.loadtxt('soybean-prices-historical-chart-data.csv', 
                        delimiter=",", 
                        dtype=str, 
                        skiprows=1)

print(dados_soja)

