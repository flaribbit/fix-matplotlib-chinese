import matplotlib.pyplot as plt
# %config InlineBackend.figure_formats = ['svg']
plt.rcParams['font.size'] = 12
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.sans-serif'] = ['Times New Roman', 'Simsun']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

plt.title(r"中文English 中a英b混c排d $f(x)=\frac{1}{2}x^2$")
plt.show()
