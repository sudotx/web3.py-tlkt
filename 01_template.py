from web3 import Web3

RPC_URL = 'http://127.0.0.1:8545'  # connected to anvil


# connect to blockchain

web3 = Web3(Web3.HTTPProvider(RPC_URL))

print(f'Connected: {web3.is_connected()}')  # proof of life

# get Chain id
print(f'Chain ID: {web3.eth.chain_id}')


# connect to contract
# target_address = web3.toChecksumAddress("")
# target_abi = ""

# target = web3.eth.contract(address=target_address, abi=target_abi)
