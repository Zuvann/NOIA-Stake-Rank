# NOIA-Stake-Rank

1). Go to https://etherscan.io/exportData?type=tokenholders&contract=0xa8c8cfb141a3bb59fea1e2ea6b79b5ecbcd7b6ca&decimal=18 and download the CSV of all token holders.

2). Open the file in excel and sort by balance and delete any entries with balances under the 20k minimum stake.

3). Place file in same directory as python file and run the python file.

4). Data is then outputted into the output CSV file which can then be sorted in excel by rank.
