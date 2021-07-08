import csv
import requests
from ast import literal_eval
from web3 import Web3


url = 'https://dashboard-api-prod.syntropystack.com/api/v1/get-stake/'
f = open('export-tokenholders-for-contract-0xa8c8CfB141A3bB59FEA1E2ea6B79b5ECBCD7b6ca.csv')
csv_f = csv.reader(f)
next(csv_f)
field_names= ['sum_earned','annual_yield','current_stake','current_total','total_interest','current_position']

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for row in csv_f:
        try:
            address=Web3.toChecksumAddress(row[0])
            r = requests.get(url+address)
            get_stake = literal_eval(r.text)
            get_stake["data"]["sum_earned"] = address
            writer.writerow(get_stake["data"])
        except:
            pass
            
csvfile.close()
print('Done')
