import json, requests
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))

# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/BitcoinPriceOracle.json'

deployed_contract_address = '0xb904A7D08a6C3Ba86Fa4860e86F698aC6fdf3396'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)


# call the CoinDesk api to access latest info ot bitcoin price in USD
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
curr_priceUSD = response['bpi']['USD']['rate']


# calling the contract function
message = contract.functions.currPriceUSD().call()

print(f"Last updated bitcoin price is {message} USD")

# execute updateCurrPrice function
tx_hash = contract.functions.updateCurrPrice(str(curr_priceUSD)).transact()

# waits for the specified transaction (tx_hash) to be confirmed
# (included in a mined block)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print(f'tx_hash: {tx_hash.hex()}')


