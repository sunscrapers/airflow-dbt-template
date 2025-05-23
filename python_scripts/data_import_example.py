import requests
import pandas as pd
import postgres_utils
import os

# Make the API request
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/DEMO_R_D3DENS?lang=EN&time=2022"
response = requests.get(url)

print("Response status code:")
print(response.status_code)

# read the request response into JSON
response_json = response.json()
print(list(response_json.keys()))

# ID and value
id_value_df = pd.DataFrame(response_json["value"].items(), columns=["id", "value"])
print(id_value_df.head())

# status data
status_df = pd.DataFrame(response_json["status"].items(), columns=["id", "status"])
print(status_df.head())

# code
code_df = pd.DataFrame(
    response_json["dimension"]["geo"]["category"]["index"].items(),
    columns=["code", "id"],
)
print(code_df.head())

# label
label_df = pd.DataFrame(
    response_json["dimension"]["geo"]["category"]["label"].items(),
    columns=["code", "label"],
)
print(label_df.head())

print("Data pulled successfully!")

# Print all environment variables
print("All environment variables:")
print(dict(os.environ))

# Create a data table in PostgreSQL
postgres_utils.write_df_to_postgres(
    table_name="raw.eurostat_d3dens_id_value", df=id_value_df
)

postgres_utils.write_df_to_postgres(
    table_name="raw.eurostat_d3dens_id_status", df=status_df
)

postgres_utils.write_df_to_postgres(
    table_name="raw.eurostat_d3dens_id_code", df=code_df
)

postgres_utils.write_df_to_postgres(
    table_name="raw.eurostat_d3dens_code_label", df=label_df
)
