# NOIA-Stake-Rank

1). Go to https://etherscan.io/exportData?type=tokenholders&contract=0xa8c8cfb141a3bb59fea1e2ea6b79b5ecbcd7b6ca&decimal=18 and download the CSV of all token holders.

2). Open the file in excel and sort by balance and delete any entries with balances under the 20k minimum stake.

3). Place the file in the same directory as python file and run the file in IDLE. It will take 10-20 minutes to complete.

4). Data is then outputted into the output CSV file which can then be sorted in excel by rank.

NOTE: This project requires the requests and web3 python modules.

Pardon my coding skills -- I haven't touched python in 3 years...
