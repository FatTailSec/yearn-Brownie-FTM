# yearn-Brownie-FTM
Easily gets relevant infomration from yern vaults on the FTM network

This repository allows for the user to quickly grab on chain data relating to the price per share as well as other yearn vault information. 

How to use:

1) Install dependencies 
```
pip install -r requirements.txt || pip3 install -r requirements.txt
```

2) Point the fork to the block number you wish to gather data at. 
In the `hardhat.congif.js` file on line 9 is where the blockNumber can be found and changed 

3) Run the following command and a csv of all Yearn vaults with sufficient value will be queried and saves as a `.csv` file
```
brownie run scripts/yearn-ftm.py --network hardhat
```
