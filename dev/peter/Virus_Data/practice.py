
#curr_time = int(time.time())
#prior_year = curr_time-(60*60*24*365)
prior_year = 1543622400  # unix for December 01,2018
ticker_symbol = "000001.SS"
import requests 
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

querystring = {"symbol":ticker_symbol}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "b477e42517mshf0183273bba2e47p1544cbjsnc7d400ac9422"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

r = response

print(r)
