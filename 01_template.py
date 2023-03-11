from web3 import Web3

INFURA = 'https://goerli.infura.io/v3/e5b18908f978432c87e7c1dbd2027517'

# connect to blockchain
web3 = Web3(Web3.HTTPProvider(INFURA))

print(f'Connected: {web3.isConnected()}')

# connect to contract
target_address = web3.toChecksumAddress("")
target_abi = ""

target = web3.eth.contract(address=target_address, abi=target_abi)


