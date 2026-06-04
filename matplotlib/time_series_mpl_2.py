import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn-v0_8')

data = pd.read_csv('data3.csv')
price_date = data['Date']
price_close = data['Close']

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()
