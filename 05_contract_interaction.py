from web3 import Web3

RPC_URL = 'http://ctf.mevsec.com:50033'

# connect to blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))

print(f'Connected: {web3.isConnected()}')

# connect to contract
TARGET_ADDRESS = '0x876807312079af775c49c916856A2D65f904e612'
TARGET_ABI = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_key",
                "type": "string"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "flag",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]


def get_contract_instance():
    target_address = web3.toChecksumAddress(TARGET_ADDRESS)
    return web3.eth.contract(address=target_address, abi=TARGET_ABI)


# get storage
target = get_contract_instance()


def get_storage_at_slot(slot):
    return web3.eth.get_storage_at(target.address, slot).decode()


print(web3.eth.accounts[0])
print(web3.eth.accounts[1])
web3.eth.default_account = web3.eth.accounts[1]

# get storage at slot 1
print('Storage at slot 0:')
print(get_storage_at_slot(0))
print('Storage at slot 1:')
print(get_storage_at_slot(1))
