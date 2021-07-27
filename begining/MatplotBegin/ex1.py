import matplotlib.pyplot as plt # престалвение pylab как plt
import numpy as np

np.random.seed(444)

fig, _ = plt.subplots()
print(type(fig)) # <class 'matplotlib.figure.Figure'>

one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
print(type(one_tick)) # <class 'matplotlib.axis.YTick'>



