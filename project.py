from flask import Flask
import json
from web3 import Web3
import requests

#######################################################################################
url = 'https://dashboard-api-prod.syntropystack.com/api/v1/get-stake/'
seen_validators = []
output_validators=[]
a=requests.get('https://api.etherscan.io/api?module=account&action=txlist&address=0x8A27Fa791316A17C5b39FE6a319f6D72ce50241F&sort=asc&apikey=9VHFZI6B4YDK81PH2P2JSWGIZQDMIYRMA9')
input_data=a.json()
print('Starting')
for i in range(0,len(input_data["result"])-1):
    if input_data["result"][i]["from"] in seen_validators:
        continue
    seen_validators.append(input_data["result"][i]["from"])
    try:
        address=Web3.toChecksumAddress(input_data["result"][i]["from"])
        r = requests.get(url+address)
        data=r.json()
        data["data"]["block"] = address
        data["data"].pop('claim_proof')
        data["data"]["current_stake"] = round(int(data["data"]["current_stake"].translate({ord('n'): None}))/(10**18))
        data["data"]["current_total"] = round(int(data["data"]["current_total"].translate({ord('n'): None}))/(10**18))
        data["data"]["total_interest"] = round(int(data["data"]["total_interest"].translate({ord('n'): None}))/(10**18))
        if data["data"]["current_position"] != -1:
            output_validators.append(data["data"])
    except:
        pass
output_validators = [{"current_position": di["current_position"], **di} for di in output_validators]
output_validators = sorted(output_validators, key=lambda d: d['current_position'])
json_dump_validators = json.dumps(output_validators)
#######################################################################################


######################################################################################
url = 'https://dashboard-api-prod.syntropystack.com/api/v1/get-stake-nominator/'
seen_nominators = []
output_nominators=[]
a=requests.get('https://api.etherscan.io/api?module=account&action=txlist&address=0xD0aE7da0EcE12811ce13297257d7fc42848E107E&sort=asc&apikey=9VHFZI6B4YDK81PH2P2JSWGIZQDMIYRMA9')
input_data=a.json()
for i in range(0,len(input_data["result"])-1):
    if input_data["result"][i]["from"] in seen_nominators:
        continue
    seen_nominators.append(input_data["result"][i]["from"])
    try:
        address=Web3.toChecksumAddress(input_data["result"][i]["from"])
        r = requests.get(url+address)
        data=r.json()
        data["data"]["address"] = address
        data["data"].pop('claim_proof')
        data["data"]["current_stake"] = round(int(data["data"]["current_stake"].translate({ord('n'): None}))/(10**18))
        data["data"]["current_total"] = round(int(data["data"]["current_total"].translate({ord('n'): None}))/(10**18))
        data["data"]["total_interest"] = round(int(data["data"]["total_interest"].translate({ord('n'): None}))/(10**18))
        output_nominators.append(data["data"])
    except:
        pass
output_nominators = sorted(output_nominators, key=lambda d: d['current_stake'], reverse=True)
json_dump_nominators = json.dumps(output_nominators)
#######################################################################################



app = Flask(__name__)

@app.route('/validator-ranks/', methods = ['GET', 'POST'])
def handle_request():
    return json_dump_validators

@app.route('/nominator-ranks/', methods = ['GET', 'POST'])
def handle_request2():
    return json_dump_nominators
