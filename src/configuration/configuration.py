import os

# CSV data saving path
url = "https://www.boc.lk/rates-tariff"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:127.0) Gecko/20100101 Firefox/127.0"

OUTPUT_HTML = os.path.join("data", "html", "BOC_Exchange_Rates.html")
OUTPUT_CSV = os.path.join("data", "csv", "BOC_Exchange_Rates.csv")
Basefile_name="BOC_Bank_Exchange_Rates"

# SQL connection string
# CONNECTION_STRING = 'mssql://BGL-DTS33\\MSSQLSERVER1/mydb?driver=ODBC+DRIVER+17+FOR+SQL+SERVER'
# Commercial bank exchange rate url
container_name_for_reference_backups = 'bank-exchange-rates-reference-backups'
backup_base_filename = 'BOC'
backup_pairs_to_keep = 28