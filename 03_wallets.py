from web3 import Web3

RPC_URL = 'https://mainnet.infura.io/v3/e5b18908f978432c87e7c1dbd2027517'

# connect to blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))

print(f'Connected: {web3.isConnected()}')

# connect to wallet
target_address = web3.toChecksumAddress(
    '0x514910771AF9Ca656af840dff83E8264EcF986CA')

# get eth balance of account
print(web3.fromWei(web3.eth.get_balance(target_address), 'ether'))

# get bytecode if account is a CA
print(web3.toHex(web3.eth.get_code(target_address)))
