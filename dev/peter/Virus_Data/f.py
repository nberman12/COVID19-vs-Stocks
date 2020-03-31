from pprint import pprint
import time
import requests
import pandas as pd
from config import rapidapi_key
#from datetime import datetime
import matplotlib.pyplot as plt
import datetime
import math
import numpy as np
import scipy.stats as st


COVID 19 EFFECT ON STOCK MARKETS
#Read in Data

time_series_2019_ncov_Deaths =pd.read_csv("../../mvp/data/covid19_data/time_series_2019-ncov-Deaths.csv")
time_series_2019_ncov_Recovered = pd.read_csv("../../mvp/data/covid19_data/time_series_2019-ncov-Recovered.csv")
time_series_ncov_Confirmed = pd.read_csv("../../mvp/data/covid19_data/time_series-ncov-Confirmed.csv")
time_series_ncov_Deaths = pd.read_csv("../../mvp/data/covid19_data/time_series-ncov-Deaths.csv")
time_series_2019_ncov_Confirmed = pd.read_csv("../../mvp/data/covid19_data/time_series_2019-ncov-Confirmed.csv")
time_series_ncov_Recovered = pd.read_csv("../../mvp/data/covid19_data/time_series-ncov-Recovered.csv")

#Deaths
#US

us_cond=time_series_2019_ncov_Deaths['Country/Region']=='US'

us_deaths = time_series_2019_ncov_Deaths[us_cond]
us_deaths =us_deaths.drop(columns =['Lat','Long','Province/State'])
us_deaths = us_deaths.groupby('Country/Region').sum()

us_deaths =us_deaths.T
us_deaths.index = pd.to_datetime(us_deaths.index)
#us_deaths.plot(legend=False)

us_daily = [0]
us_daily_percent = [0]
for i in range(1,len(us_deaths['US'])):
    us_daily.append(us_deaths['US'][i]-us_deaths['US'][i-1])
    if us_deaths['US'][i-1]>0:
        us_daily_percent.append((us_deaths['US'][i]-us_deaths['US'][i-1])/us_deaths['US'][i-1])
    else:
        us_daily_percent.append(0)
us_daily_df = us_deaths[['US']]
us_daily_df['Daily']=us_daily
us_daily_df['Percent Change'] = us_daily_percent

#us_daily_df.plot(legend=False)
us_daily_df['Percent Change'].plot(legend=True)
plt.show()

#ITALY
italy_cond=time_series_2019_ncov_Deaths['Country/Region']=='Italy'

italy_deaths = time_series_2019_ncov_Deaths[italy_cond]
italy_deaths =italy_deaths.drop(columns =['Lat','Long','Province/State'])
italy_deaths = italy_deaths.groupby('Country/Region').sum()

italy_deaths =italy_deaths.T
italy_deaths.index = pd.to_datetime(italy_deaths.index)

italy_daily = [0]
italy_daily_percent = [0]
for i in range(1,len(italy_deaths['Italy'])):
    italy_daily.append(italy_deaths['Italy'][i]-italy_deaths['Italy'][i-1])
    
    if italy_deaths['Italy'][i-1]>0:
        italy_daily_percent.append((italy_deaths['Italy'][i]-italy_deaths['Italy'][i-1])/italy_deaths['Italy'][i-1])
    else:
        italy_daily_percent.append(0)    
    
italy_daily_df = italy_deaths[['Italy']]
italy_daily_df['Daily']=italy_daily
italy_daily_df['Percent Change'] = italy_daily_percent

#italy_daily_df.plot(legend=False)
italy_daily_df['Percent Change'].plot(legend=True)
plt.show()

#CHINA
china_cond=time_series_2019_ncov_Deaths['Country/Region']=='China'

china_deaths = time_series_2019_ncov_Deaths[china_cond]
china_deaths =china_deaths.drop(columns =['Lat','Long','Province/State'])
china_deaths = china_deaths.groupby('Country/Region').sum()

china_deaths =china_deaths.T
china_deaths.index = pd.to_datetime(china_deaths.index)
#china_deaths.plot(legend=False)

china_daily = [0]
china_daily_percent = [0]
for i in range(1,len(china_deaths['China'])):
    china_daily.append(china_deaths['China'][i]-china_deaths['China'][i-1])
    if china_deaths['China'][i-1]>0:
        china_daily_percent.append((china_deaths['China'][i]-china_deaths['China'][i-1])/china_deaths['China'][i-1])
    else:
        china_daily_percent.append(0)    
    
    
china_daily_df = china_deaths[['China']]
china_daily_df['Daily']=china_daily
china_daily_df['Percent Change'] = china_daily_percent

#china_daily_df.plot(legend=False)
china_daily_df['Percent Change'].plot(legend=True)

plt.show()

#NUMBER OF RECOVERED
#US
us_cond=time_series_2019_ncov_Recovered['Country/Region']=='US'

us_recovered = time_series_2019_ncov_Recovered[us_cond]
us_recovered =us_recovered.drop(columns =['Lat','Long','Province/State'])
us_recovered = us_recovered.groupby('Country/Region').sum()

us_recovered =us_recovered.T
us_recovered.index = pd.to_datetime(us_recovered.index)
#us_recovered.plot(legend=False)

us_daily = [0]
us_daily_percent = [0]
for i in range(1,len(us_recovered['US'])):
    
    us_daily.append(us_recovered['US'][i]-us_recovered['US'][i-1])
    if us_recovered['US'][i-1]>0:
        us_daily_percent.append((us_recovered['US'][i]-us_recovered['US'][i-1])/us_recovered['US'][i-1])
    else:
        us_daily_percent.append(0)
us_daily_df = us_recovered[['US']]
us_daily_df['Daily']=us_daily
us_daily_df['Percent Change'] = us_daily_percent

#us_daily_df.plot(legend=False)
us_daily_df['Percent Change'].plot(legend=True)
plt.show()

#ITALY
italy_cond=time_series_2019_ncov_Recovered['Country/Region']=='Italy'

italy_recovered = time_series_2019_ncov_Recovered[italy_cond]
italy_recovered =italy_recovered.drop(columns =['Lat','Long','Province/State'])
italy_recovered = italy_recovered.groupby('Country/Region').sum()

italy_recovered =italy_recovered.T
italy_recovered.index = pd.to_datetime(italy_recovered.index)
#italy_recovered.plot(legend=False)

italy_daily = [0]
italy_daily_percent = [0]
for i in range(1,len(italy_recovered['Italy'])):
    italy_daily.append(italy_recovered['Italy'][i]-italy_recovered['Italy'][i-1])
    if italy_recovered['Italy'][i-1]>0:
        italy_daily_percent.append((italy_recovered['Italy'][i]-italy_recovered['Italy'][i-1])/italy_recovered['Italy'][i-1])
    else:
        italy_daily_percent.append(0)
        
italy_daily_df = italy_recovered[['Italy']]
italy_daily_df['Daily']=italy_daily
italy_daily_df['Percent Change'] = italy_daily_percent

italy_daily_df.columns = ["Total Cases","Daily Cases", "Percent Change"]
#taly_daily_df.plot(legend=False)
italy_daily_df['Percent Change'].plot(legend=True)

plt.legend()
plt.show()

#CHINA
china_cond=time_series_2019_ncov_Recovered['Country/Region']=='China'

china_recovered = time_series_2019_ncov_Recovered[china_cond]
china_recovered =china_recovered.drop(columns =['Lat','Long','Province/State'])
china_recovered = china_recovered.groupby('Country/Region').sum()

china_recovered =china_recovered.T
china_recovered.index = pd.to_datetime(china_recovered.index)
#china_recovered.plot(legend=False)

china_daily = [0]
china_daily_percent = [0]
for i in range(1,len(china_recovered['China'])):
    china_daily.append(china_recovered['China'][i]-china_recovered['China'][i-1])
    if china_recovered['China'][i-1]>0:
        china_daily_percent.append((china_recovered['China'][i]-china_recovered['China'][i-1])/china_recovered['China'][i-1])
    else:
        china_daily_percent.append(0)
        
china_daily_df = china_recovered[['China']]
china_daily_df['Daily']=china_daily
china_daily_df['Percent Change'] = china_daily_percent

china_daily_df.columns=['Total Cases','Daily Cases','Percent Change']
#china_daily_df.plot(legend=False)
china_daily_df['Percent Change'].plot(legend=True)
plt.legend()
plt.show()

#Confirmed Cases
#US
us_cond=time_series_2019_ncov_Confirmed['Country/Region']=='US'

us_confirmed = time_series_2019_ncov_Confirmed[us_cond]
us_confirmed =us_confirmed.drop(columns =['Lat','Long','Province/State'])
us_confirmed = us_confirmed.groupby('Country/Region').sum()

us_confirmed =us_confirmed.T
us_confirmed.index = pd.to_datetime(us_confirmed.index)
#us_confirmed.plot(legend=True,label = "Total Cases")

us_daily = [0]
us_daily_percent = [0]
for i in range(1,len(us_confirmed['US'])):
    us_daily.append(us_confirmed['US'][i]-us_confirmed['US'][i-1])
    if us_confirmed['US'][i-1]>0:
        us_daily_percent.append((us_confirmed['US'][i]-us_confirmed['US'][i-1])/us_confirmed['US'][i-1])
    else:
        us_daily_percent.append(0)
us_daily_df = us_confirmed[['US']]
us_daily_df['Daily']=us_daily
us_daily_df['Percent Change'] = us_daily_percent

#us_daily_plot = us_daily_df['Daily']
#us_daily_plot.plot(legend=False,label = "Daily Cases")
us_daily_df['Percent Change'].plot(legend=True)
plt.legend()
plt.show()

### ITALY
italy_cond=time_series_2019_ncov_Confirmed['Country/Region']=='Italy'

italy_confirmed = time_series_2019_ncov_Confirmed[italy_cond]
italy_confirmed =italy_confirmed.drop(columns =['Lat','Long','Province/State'])
italy_confirmed = italy_confirmed.groupby('Country/Region').sum()

italy_confirmed =italy_confirmed.T
italy_confirmed.index = pd.to_datetime(italy_confirmed.index)
#italy_confirmed.plot(legend=False)

italy_daily = [0]
italy_daily_percent = [0]
for i in range(1,len(italy_confirmed['Italy'])):
    italy_daily.append(italy_confirmed['Italy'][i]-italy_confirmed['Italy'][i-1])
    if italy_confirmed['Italy'][i-1]>0:
        italy_daily_percent.append((italy_confirmed['Italy'][i]-italy_confirmed['Italy'][i-1])/italy_confirmed['Italy'][i-1])
    else:
        italy_daily_percent.append(0)
        
italy_daily_df = italy_confirmed[['Italy']]
italy_daily_df['Daily']=italy_daily
italy_daily_plot=italy_daily_df['Daily']
italy_daily_df['Percent Change'] = italy_daily_percent
italy_daily_df.columns = ["Total Cases","Daily Cases", "Percent Change"]
#italy_daily_plot.plot(legend=False, label = 'Daily Cases')
italy_daily_df['Percent Change'].plot(legend=True)
plt.legend()
plt.show()


### CHINA
china_cond=time_series_2019_ncov_Confirmed['Country/Region']=='China'

china_confirmed = time_series_2019_ncov_Confirmed[china_cond]
china_confirmed =china_confirmed.drop(columns =['Lat','Long','Province/State'])
china_confirmed = china_confirmed.groupby('Country/Region').sum()

china_confirmed =china_confirmed.T
china_confirmed.index = pd.to_datetime(china_confirmed.index)
#china_confirmed.plot(legend=False)

china_daily = [0]
china_daily_percent = [0]
for i in range(1,len(china_confirmed['China'])):
    china_daily.append(china_confirmed['China'][i]-china_confirmed['China'][i-1])
    if china_confirmed['China'][i-1]>0:
        china_daily_percent.append((china_confirmed['China'][i]-china_confirmed['China'][i-1])/china_confirmed['China'][i-1])
    else:
        china_daily_percent.append(0)
        
china_daily_df = china_confirmed[['China']]
china_daily_df['Daily']=china_daily
china_daily_df['Percent Change'] = china_daily_percent
china_daily_plot = china_daily_df['Daily']
#china_daily_plot.plot(legend=False)
china_daily_df['Percent Change'].plot(legend=True)
plt.show()



## STOCK MARKET
### DOW JONES INDEX
curr_time = int(time.time())

ticker_symbol = "^DJI"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"

querystring = {"region":"US","lang":"en","symbol":ticker_symbol,"from":'1575176400',"to":curr_time,"events":"div","events":"split","events":"earn","interval":"1d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response3 = requests.request("GET", url, headers=headers, params=querystring)

timestamp = response3.json()['chart']['result'][0]['timestamp']
year_close = response3.json()['chart']['result'][0]['indicators']['quote'][0]['close']
year_open =response3.json()['chart']['result'][0]['indicators']['quote'][0]['open']
year_volume =response3.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
year_adjclose =response3.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

djiDict = {"Timestamp":timestamp,
           "Open":year_open,
          "Close":year_close,
           "Volume":year_volume,
          "Adjclose":year_adjclose
          }
dji_df = pd.DataFrame(djiDict)
dji_df['Change %'] = (dji_df['Close']-dji_df['Open'])/dji_df['Open']

convert_date = []
convert_date = [datetime.datetime.utcfromtimestamp(dji_df['Timestamp'][x]).strftime('%Y-%m-%d') for x in range(0,len(dji_df['Timestamp']))]
dji_df['Date'] = convert_date

dji_df['Last Year'] =[datetime.datetime.strptime(dji_df['Date'][x],'%Y-%m-%d')-datetime.timedelta(365) for x in range(0,len(dji_df['Date']))]
dji_df.head()

### S&P 500
curr_time = int(time.time())
ticker_symbol = "^GSPC"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"

querystring = {"region":"US","lang":"en","symbol":ticker_symbol,"from":'1575176400',"to":curr_time,"events":"div","events":"split","events":"earn","interval":"1d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

timestamp = response.json()['chart']['result'][0]['timestamp']
year_close = response.json()['chart']['result'][0]['indicators']['quote'][0]['close']
year_open =response.json()['chart']['result'][0]['indicators']['quote'][0]['open']
year_volume =response.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
year_adjclose =response.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

smpDict = {"Timestamp":timestamp,
           "Open":year_open,
          "Close":year_close,
           "Volume":year_volume,
          "Adjclose":year_adjclose
          }
smp_df = pd.DataFrame(smpDict)
smp_df['Change %'] = (smp_df['Close']-smp_df['Open'])/smp_df['Open']

convert_date = []
convert_date = [datetime.datetime.utcfromtimestamp(smp_df['Timestamp'][x]).strftime('%Y-%m-%d') for x in range(0,len(smp_df['Timestamp']))]
smp_df['Date'] = convert_date


smp_df['Last Year'] =[datetime.datetime.strptime(smp_df['Date'][x],'%Y-%m-%d')-datetime.timedelta(365) for x in range(0,len(smp_df['Date']))]


### Shanghai Stock Exchange
curr_time = int(time.time())

ticker_symbol = "000001.SS"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"

querystring = {"region":"US","lang":"en","symbol":ticker_symbol,"from":'1575176400',"to":curr_time,"events":"div","events":"split","events":"earn","interval":"1d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response2 = requests.request("GET", url, headers=headers, params=querystring)

timestamp = response2.json()['chart']['result'][0]['timestamp']
year_close = response2.json()['chart']['result'][0]['indicators']['quote'][0]['close']
year_open =response2.json()['chart']['result'][0]['indicators']['quote'][0]['open']
year_volume =response2.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
year_adjclose =response2.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

sseDict = {"Timestamp":timestamp,
           "Open":year_open,
          "Close":year_close,
           "Volume":year_volume,
          "Adjclose":year_adjclose
          }
sse_df = pd.DataFrame(sseDict)

sse_df['Change %'] = (sse_df['Close']-sse_df['Open'])/sse_df['Open']

convert_date = []
convert_date = [datetime.datetime.utcfromtimestamp(sse_df['Timestamp'][x]).strftime('%Y-%m-%d') for x in range(0,len(sse_df['Timestamp']))]
sse_df['Date'] = convert_date

sse_df['Last Year'] =[datetime.datetime.strptime(sse_df['Date'][x],'%Y-%m-%d')-datetime.timedelta(365) for x in range(0,len(sse_df['Date']))]
sse_df.head()

### Italian Index
italy_market_df = pd.read_csv("italy_index/FTSE Italia All Share Historical Data.csv")
italy_market_df["Date"]=pd.to_datetime(italy_market_df["Date"])


fig,ax1 = plt.subplots()
ax1.plot(italy_market_df["Date"],italy_market_df["Price"])
plt.xlim(datetime.date(2020,1,22),datetime.date(2020,3,23))
plt.ylim(10000,35000)

ax2=ax1.twinx()

ax2.plot(italy_confirmed["Italy"],color = 'tab:red')

plt.show()


### France- CAC 40

curr_time = int(time.time())

ticker_symbol = "^FCHI"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"

querystring = {"region":"US","lang":"en","symbol":ticker_symbol,"from":'1575176400',"to":curr_time,"events":"div","events":"split","events":"earn","interval":"1d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response2 = requests.request("GET", url, headers=headers, params=querystring)

timestamp = response2.json()['chart']['result'][0]['timestamp']
year_close = response2.json()['chart']['result'][0]['indicators']['quote'][0]['close']
year_open =response2.json()['chart']['result'][0]['indicators']['quote'][0]['open']
year_volume =response2.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
year_adjclose =response2.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

fchiDict = {"Timestamp":timestamp,
           "Open":year_open,
          "Close":year_close,
           "Volume":year_volume,
          "Adjclose":year_adjclose
          }
fchi_df = pd.DataFrame(fchiDict)

fchi_df['Change %'] = (fchi_df['Close']-fchi_df['Open'])/fchi_df['Open']

convert_date = []
convert_date = [datetime.datetime.utcfromtimestamp(fchi_df['Timestamp'][x]).strftime('%Y-%m-%d') for x in range(0,len(fchi_df['Timestamp']))]
fchi_df['Date'] = convert_date

fchi_df['Last Year'] =[datetime.datetime.strptime(fchi_df['Date'][x],'%Y-%m-%d')-datetime.timedelta(365) for x in range(0,len(fchi_df['Date']))]
fchi_df.head()


### England- FTSE 100
curr_time = int(time.time())

ticker_symbol = "^FTSE"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"

querystring = {"region":"US","lang":"en","symbol":ticker_symbol,"from":'1575176400',"to":curr_time,"events":"div","events":"split","events":"earn","interval":"1d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response2 = requests.request("GET", url, headers=headers, params=querystring)

timestamp = response2.json()['chart']['result'][0]['timestamp']
year_close = response2.json()['chart']['result'][0]['indicators']['quote'][0]['close']
year_open =response2.json()['chart']['result'][0]['indicators']['quote'][0]['open']
year_volume =response2.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
year_adjclose =response2.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

ftseDict = {"Timestamp":timestamp,
           "Open":year_open,
          "Close":year_close,
           "Volume":year_volume,
          "Adjclose":year_adjclose
          }
ftse_df = pd.DataFrame(ftseDict)

ftse_df['Change %'] = (ftse_df['Close']-ftse_df['Open'])/ftse_df['Open']

convert_date = []
convert_date = [datetime.datetime.utcfromtimestamp(fchi_df['Timestamp'][x]).strftime('%Y-%m-%d') for x in range(0,len(ftse_df['Timestamp']))]
ftse_df['Date'] = convert_date

ftse_df['Last Year'] =[datetime.datetime.strptime(ftse_df['Date'][x],'%Y-%m-%d')-datetime.timedelta(365) for x in range(0,len(ftse_df['Date']))]
ftse_df.head()


### Germany- DAX

curr_time = int(time.time())

ticker_symbol = "DAX"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"

querystring = {"region":"US","lang":"en","symbol":ticker_symbol,"from":'1575176400',"to":curr_time,"events":"div","events":"split","events":"earn","interval":"1d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response2 = requests.request("GET", url, headers=headers, params=querystring)

timestamp = response2.json()['chart']['result'][0]['timestamp']
year_close = response2.json()['chart']['result'][0]['indicators']['quote'][0]['close']
year_open =response2.json()['chart']['result'][0]['indicators']['quote'][0]['open']
year_volume =response2.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
year_adjclose =response2.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

daxDict = {"Timestamp":timestamp,
           "Open":year_open,
          "Close":year_close,
           "Volume":year_volume,
          "Adjclose":year_adjclose
          }
dax_df = pd.DataFrame(daxDict)

dax_df['Change %'] = (dax_df['Close']-dax_df['Open'])/dax_df['Open']

convert_date = []
convert_date = [datetime.datetime.utcfromtimestamp(dax_df['Timestamp'][x]).strftime('%Y-%m-%d') for x in range(0,len(dax_df['Timestamp']))]
dax_df['Date'] = convert_date

dax_df['Last Year'] =[datetime.datetime.strptime(dax_df['Date'][x],'%Y-%m-%d')-datetime.timedelta(365) for x in range(0,len(dax_df['Date']))]
dax_df.head()

Switzerland- Swiss Market Index
curr_time = int(time.time())

ticker_symbol = "^SSMI"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"

querystring = {"region":"US","lang":"en","symbol":ticker_symbol,"from":'1575176400',"to":curr_time,"events":"div","events":"split","events":"earn","interval":"1d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response2 = requests.request("GET", url, headers=headers, params=querystring)

timestamp = response2.json()['chart']['result'][0]['timestamp']
year_close = response2.json()['chart']['result'][0]['indicators']['quote'][0]['close']
year_open =response2.json()['chart']['result'][0]['indicators']['quote'][0]['open']
year_volume =response2.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
year_adjclose =response2.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

ssmiDict = {"Timestamp":timestamp,
           "Open":year_open,
          "Close":year_close,
           "Volume":year_volume,
          "Adjclose":year_adjclose
          }
ssmi_df = pd.DataFrame(ssmiDict)

ssmi_df['Change %'] = (ssmi_df['Close']-ssmi_df['Open'])/ssmi_df['Open']

convert_date = []
convert_date = [datetime.datetime.utcfromtimestamp(ssmi_df['Timestamp'][x]).strftime('%Y-%m-%d') for x in range(0,len(ssmi_df['Timestamp']))]
ssmi_df['Date'] = convert_date

ssmi_df['Last Year'] =[datetime.datetime.strptime(ssmi_df['Date'][x],'%Y-%m-%d')-datetime.timedelta(365) for x in range(0,len(ssmi_df['Date']))]
ssmi_df.head()


### All World Index
curr_time = int(time.time())

ticker_symbol = "VWRD.L"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories"

querystring = {"region":"US","lang":"en","symbol":ticker_symbol,"from":'1575176400',"to":curr_time,"events":"div","events":"split","events":"earn","interval":"1d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response2 = requests.request("GET", url, headers=headers, params=querystring)

timestamp = response2.json()['chart']['result'][0]['timestamp']
year_close = response2.json()['chart']['result'][0]['indicators']['quote'][0]['close']
year_open =response2.json()['chart']['result'][0]['indicators']['quote'][0]['open']
year_volume =response2.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
year_adjclose =response2.json()['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

vwrldDict = {"Timestamp":timestamp,
           "Open":year_open,
          "Close":year_close,
           "Volume":year_volume,
          "Adjclose":year_adjclose
          }
vwrld_df = pd.DataFrame(vwrldDict)

vwrld_df['Change %'] = (vwrld_df['Close']-vwrld_df['Open'])/vwrld_df['Open']

convert_date = []
convert_date = [datetime.datetime.utcfromtimestamp(vwrld_df['Timestamp'][x]).strftime('%Y-%m-%d') for x in range(0,len(vwrld_df['Timestamp']))]
vwrld_df['Date'] = convert_date

vwrld_df['Last Year'] =[datetime.datetime.strptime(vwrld_df['Date'][x],'%Y-%m-%d')-datetime.timedelta(365) for x in range(0,len(vwrld_df['Date']))]
vwrld_df.head()



#DATETIME
dji_df["Date"] = pd.to_datetime(dji_df['Date'])
smp_df["Date"] = pd.to_datetime(smp_df['Date'])
sse_df["Date"] = pd.to_datetime(sse_df['Date'])
fchi_df["Date"] = pd.to_datetime(fchi_df['Date'])
ftse_df["Date"] = pd.to_datetime(ftse_df['Date'])
dax_df["Date"] = pd.to_datetime(dax_df['Date'])
ssmi_df["Date"] = pd.to_datetime(ssmi_df['Date'])
dax_df["Date"] = pd.to_datetime(dax_df['Date'])
vwrld_df["Date"] = pd.to_datetime(vwrld_df['Date'])

#GRAPH
fig,ax1 = plt.subplots()
ax1.plot(vwrld_df["Date"],vwrld_df["Close"])
plt.xlim(datetime.date(2020,1,22),datetime.date(2020,3,23))
#plt.ylim(10000,35000)

ax2=ax1.twinx()

ax2.plot(italy_confirmed["Italy"],color = 'tab:red')

plt.show()


#GRAPH
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('World Index Price')
ax1.plot(vwrld_df['Date'],vwrld_df['Close'], label = "World Index Price", color=color)
plt.xlim(datetime.date(2020,1,9),datetime.date(2020,3,26))

plt.legend(loc='center left')
plt.xticks(rotation=70)
ax2 = ax1.twinx()
color1 = 'tab:blue'
color2 = 'tab:green'
color3 = 'tab:orange'
ax2.set_ylabel('Daily % Change')
ax2.scatter(italy_deaths["Italy"].index,italy_deaths["Italy"].values,label='Italy % Change')
#ax2.scatter(us_daily_df.reset_index()['index'],us_daily_df.reset_index()['Percent Change'], label='US % Change')
#ax2.scatter(china_daily_df.reset_index()['index'],china_daily_df.reset_index()['Percent Change'],label='China % Change')

plt.legend(loc = 'best')
plt.show()

### REAL CHARTS
temp =time_series_2019_ncov_Deaths.groupby('Country/Region').sum()
temp_deaths =temp.drop(columns = ['Lat','Long'])
temp_deathsT = temp_deaths.T
temp_deathsT=temp_deathsT.reset_index()
temp_deathsT['index']=pd.to_datetime(temp_deathsT['index'])
temp_deathsT['Date']=temp_deathsT['index']
temp_deathsT.drop(columns=['index'])
smp_df['Date']=pd.to_datetime(smp_df['Date'])
a = pd.merge(temp_deathsT,smp_df,on='Date',how = 'inner')

country_list = []
corr_list = []
temp_deathsT = temp_deaths.T

chinese_death_correlation_fig = plt.figure()

x_values= a["China"]
y_values= a["Close"]
correlation = st.pearsonr(x_values,y_values)
correlation = round(st.pearsonr(x_values,y_values)[0],2)
print(f"The correlation coefficient between Chinese Deaths and is {correlation}")
plt.scatter(x_values,y_values)
plt.xlabel("Number of Deaths")
plt.ylabel("Stock Price")
plt.title("Chinese Deaths Vs. S&P 500 Stock Price")
plt.show()


### UNDER CHART
for name in temp_deathsT.columns:
    x_values = a[name]
    y_values = a['Close']
    correlation = st.pearsonr(x_values,y_values)
    plt.scatter(x_values,y_values)
    country_list.append(name)
    corr_list.append(round(correlation[0],2))
    
final_df = pd.DataFrame({'Country':country_list,
                        'Correlation':corr_list})

final_df=final_df[final_df['Correlation'].notna()]
final_df = final_df[final_df['Correlation']!="nan"]
f = final_df.sort_values('Correlation')
f
f =f.reset_index()
f.sort_values('Correlation',ascending = True)#,ascending = False

### CONFIRMED REAL
temp =time_series_2019_ncov_Confirmed.groupby('Country/Region').sum()
temp_confirm =temp.drop(columns = ['Lat','Long'])
temp_confirmT = temp_confirm.T
temp_confirmT=temp_confirmT.reset_index()
temp_confirmT['index']=pd.to_datetime(temp_confirmT['index'])
temp_confirmT['Date']=temp_confirmT['index']
temp_confirmT.drop(columns=['index'])
smp_df['Date']=pd.to_datetime(smp_df['Date'])
a = pd.merge(temp_confirmT,smp_df,on='Date',how = 'inner')

country_list = []
corr_list = []
temp_confirmT = temp_confirm.T


x_values= a["Italy"]
y_values= a["Close"]
correlation = st.pearsonr(x_values,y_values)
correlation = round(st.pearsonr(x_values,y_values)[0],2)
print(correlation)
plt.scatter(x_values,y_values)
plt.show()

for name in temp_deathsT.columns:
    x_values = a[name]
    y_values = a['Close']
    correlation = st.pearsonr(x_values,y_values)
    plt.scatter(x_values,y_values)
    country_list.append(name)
    corr_list.append(round(correlation[0],2))
    
final_df = pd.DataFrame({'Country':country_list,
                        'Correlation':corr_list})

final_df=final_df[final_df['Correlation'].notna()]
final_df = final_df[final_df['Correlation']!="nan"]
f = final_df.sort_values('Correlation')
f
f =f.reset_index()
f.sort_values('Correlation',ascending = True).head(10)#,ascending = False

### RECOVERED REAL
temp =time_series_2019_ncov_Recovered.groupby('Country/Region').sum()
temp_recovered =temp.drop(columns = ['Lat','Long'])
temp_recoveredT = temp_recovered.T
temp_recoveredT=temp_recoveredT.reset_index()
temp_recoveredT['index']=pd.to_datetime(temp_recoveredT['index'])
temp_recoveredT['Date']=temp_recoveredT['index']
temp_recoveredT.drop(columns=['index'])
smp_df['Date']=pd.to_datetime(smp_df['Date'])
a = pd.merge(temp_recoveredT,smp_df,on='Date',how = 'inner')

country_list = []
corr_list = []
temp_recoveredT = temp_recovered.T


x_values= a["China"]
y_values= a["Close"]
correlation = st.pearsonr(x_values,y_values)
correlation = round(st.pearsonr(x_values,y_values)[0],2)
print(correlation)
plt.scatter(x_values,y_values)
plt.show()

# for name in temp_deathsT.columns:
#     x_values = a[name]
#     y_values = a['Close']
#     correlation = st.pearsonr(x_values,y_values)
#     plt.scatter(x_values,y_values)
#     country_list.append(name)
#     corr_list.append(round(correlation[0],2))
    
# final_df = pd.DataFrame({'Country':country_list,
#                         'Correlation':corr_list})

# final_df=final_df[final_df['Correlation'].notna()]
# final_df = final_df[final_df['Correlation']!="nan"]
# f = final_df.sort_values('Correlation')
# f
#f =f.reset_index()
#f.sort_values('Correlation',ascending = True)#,ascending = False


f[f["Country"] == "US"]