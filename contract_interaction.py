from web3 import Web3

RPC_URL = 'http://ctf.mevsec.com:50033'

# connect to blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))

print(f'Connected: {web3.is_connected()}')

# get contract


def get_contract_instance(address, target_abi):
    target_address = web3.to_checksum_address(address)
    return web3.eth.contract(address=target_address, abi=target_abi)


def get_contract_code_tohex(target_address):
    return (web3.to_hex(web3.eth.get_code(target_address)))


def get_storage_at_slot(address, abi, slot):
    target = get_contract_instance(address, abi)
    return web3.eth.get_storage_at(target.address, slot).decode()


print(web3.eth.accounts[0])
# print(web3.eth.accounts[1])
# web3.eth.default_account = web3.eth.accounts[1]


# get storage at slot 1
print('Storage at slot 0:')
print(get_storage_at_slot('0x876807312079af775c49c916856A2D65f904e612',
      '[{"inputs": [{"internalType": "string","name": "_key","type": "string"}],"stateMutability": "nonpayable","type": "constructor"},{"inputs": [],"name": "flag","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}]', 0))
print('Storage at slot 1:')
print(get_storage_at_slot('0x876807312079af775c49c916856A2D65f904e612',
      '[{"inputs": [{"internalType": "string","name": "_key","type": "string"}],"stateMutability": "nonpayable","type": "constructor"},{"inputs": [],"name": "flag","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}]', 1))


# this function interacts with a smart contract deployed on the blockchain network


def interact_with_contract_function(address, abi):
    # get contract instance
    target_contract = get_contract_instance(address, abi)
    # specify contract function and arguments here

    # interact with contract function
    txn_hash = target_contract.functions.test("test").transact()

    # wait for transaction to be mined
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)

    # return transaction hash
    return txn_receipt['transactionHash']

# interact with contract function


interact_with_contract_function('0x876807312079af775c49c916856A2D65f904e612',
                                '[{"inputs": [{"internalType": "string","name": "_key","type": "string"}],"stateMutability": "nonpayable","type": "constructor"},{"inputs": [],"name": "flag","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}]')
