import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('assignment1/excel_vnm.csv')
price = np.array(data['<CloseFixed>'])
T = 1
return_ = (price[T:] - price[:-T])/price[:-T]
vol = np.array(data['<Volume>']) 

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(price, 'r-')
ax2.plot(vol, 'b-')

ax1.set_xlabel('Time')
ax1.set_ylabel('Price data', color='r')
ax2.set_ylabel('Volume data', color='b')

plt.show()