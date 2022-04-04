import csv
import requests
from web3 import Web3


url = 'https://dashboard-api-prod.syntropystack.com/api/v1/get-stake/'
f = open('export-0x8A27Fa791316A17C5b39FE6a319f6D72ce50241F.csv')
csv_f = csv.reader(f)
next(csv_f)
field_names= ['block','current_stake','current_total','total_interest','current_position','stake_in_contract','stake_whitelisted','validator_status','validator_text','kyc_completed','email_verified']
seen = []


with open('output-validator.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for row in csv_f:
        if row[4] in seen:
            continue
        seen.append(row[4])
        try:
            address=Web3.toChecksumAddress(row[4])
            r = requests.get(url+address)
            data=r.json()
            data["data"]["block"] = address
            data["data"].pop('claim_proof')
            data["data"]["current_stake"] = int(data["data"]["current_stake"].translate({ord('n'): None}))/(10**18)
            data["data"]["current_total"] = int(data["data"]["current_total"].translate({ord('n'): None}))/(10**18)
            data["data"]["total_interest"] = int(data["data"]["total_interest"].translate({ord('n'): None}))/(10**18)
            writer.writerow(data["data"])
        except:
            pass
            
csvfile.close()
print('Done validators')


url = 'https://dashboard-api-prod.syntropystack.com/api/v1/get-stake-nominator/'
f = open('export-0xD0aE7da0EcE12811ce13297257d7fc42848E107E.csv')
csv_f = csv.reader(f)
next(csv_f)
field_names= ['address','current_stake','current_total','total_interest','kyc_required','kyc_completed']
seen = []

with open('output-nominator.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=field_names)
    writer.writeheader()
    for row in csv_f:
        if row[4] in seen:
            continue
        seen.append(row[4])
        try:
            address=Web3.toChecksumAddress(row[4])
            r = requests.get(url+address)
            data=r.json()
            data["data"]["address"] = address
            data["data"].pop('claim_proof')
            data["data"]["current_stake"] = int(data["data"]["current_stake"].translate({ord('n'): None}))/(10**18)
            data["data"]["current_total"] = int(data["data"]["current_total"].translate({ord('n'): None}))/(10**18)
            data["data"]["total_interest"] = int(data["data"]["total_interest"].translate({ord('n'): None}))/(10**18)
            writer.writerow(data["data"])
        except:
            pass
            
csvfile.close()
print('Done nominators')
