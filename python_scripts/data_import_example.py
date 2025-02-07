print('Hello world from the Python script!!!')

import requests
import pandas as pd

# Make the API request
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/DEMO_R_D3DENS?lang=EN&time=2022"
response = requests.get(url)

print('Response status code:')
print(response.status_code)

# read the request response into JSON
response_json = response.json()
print(list(response_json.keys()))

# ID and value
id_value_df = pd.DataFrame(response_json['value'].items(), columns=['id', 'value'])
print(id_value_df.head())

# status data
status_df =  pd.DataFrame(response_json['status'].items(), columns=['id', 'status'])
print(status_df.head())

# code
code_df = pd.DataFrame(response_json['dimension']['geo']['category']['index'].items(), columns=['code', 'id'])
print(code_df.head())

# label
label_df = pd.DataFrame(response_json['dimension']['geo']['category']['label'].items(), columns=['code', 'label'])
print(label_df.head())

print('Data pulled successfully!')
