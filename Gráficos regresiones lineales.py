# Gráficos regresiones lineales

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

# Sample data
data = {
    'x': [2.3625, 1.89, 1.575, 0.945, 0.63, 0.315, 0.252], 
    'y': [94.184030, 78.886997, 64.934463, 41.844804, 28.743727, 14.523220, 11.536080]
}

# Concentración NOR Uv --> [6.30, 4.725, 3.15, 1.575, 0.945, 0.63, 0.315]
# Concentración SMX Uv --> [5.00, 3.75, 2.50, 1.25, 0.75, 0.50, 0.25]
# Concentración NOR FLU --> [2.3625, 1.89, 1.575, 0.945, 0.63, 0.315, 0.252]

df = pd.DataFrame(data)

# Regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df['x'], df['y'])

# Uso de Latex para el gráfico, ver la renderización
plt.rcParams['text.usetex'] = True

# Plot
sns.regplot(x='x', y='y', data=df, ci=None, line_kws={'color':'blue', 'linewidth':1.8}, scatter_kws={'color':'blue', "s":30})
plt.xlabel(r'Concentración ($\mu g/ml$)', fontsize=12, fontweight="bold")
plt.ylabel(r'Intensidad de Fluorescencia', fontsize=12, fontweight="bold")
#plt.xlabel('Concentración (µg/ml)', fontname = "DejaVu Sans")  'Concentración ($\mu g/ml$)
#plt.ylabel('Absorbancia', fontname = "DejaVu Sans")
#plt.title(f'Curva de Calibración NOR', fontname="Arial", fontsize=14, fontweight="bold")
sign = '-' if intercept < 0 else '+'
plt.text(0.8, 80, r'$y = %.3fx\ %s\ %.3f$' % (slope, sign, abs(intercept)) + '\n$R^2= %.4f$' % r_value**2, 
         fontsize=11, color='black')
#plt.text(1.5, 0.6, f'y = {slope:.3f}x {sign} {abs(intercept):.3f}\n$R^2$= {r_value**2:.4f}', 
         #fontname='DejaVu Sans', fontsize=10, color='black') #bbox=dict(facecolor='white', alpha=0.5))

plt.xticks(np.arange(0, 3.5, 0.5))  
plt.yticks(np.round(np.arange(0, 120, 20), 4))

sns.despine()

plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
#plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

plt.show()