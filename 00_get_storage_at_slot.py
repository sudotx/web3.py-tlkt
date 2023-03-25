# import Web3 library
from web3 import Web3

# URL for an Ethereum node, to connect to blockchain
RPC_URL = 'http://ctf.mevsec.com:50046'
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Check if the connection with the node is successful or not
print(f'Connected: {web3.isConnected()}')

# Set an address and abi of a smart contract that we'll use to interact with
target_address = web3.toChecksumAddress(
    '0x876807312079af775c49c916856A2D65f904e612')
target_abi = '[{"inputs":[{"internalType":"string","name":"_key","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"flag","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]'

# Create instance of contract factory attached with given address and ABI
target = web3.eth.contract(address=target_address, abi=target_abi)

# get data stored at a particular slot of the contract's storage


def get_storage_at_slot(slot):
    # use get_storage_at() method from web3.eth module to obtain value stored in specified slot
    padded_slot = slot.to_bytes(32, byteorder='big')
    storage_value = web3.eth.get_storage_at(target.address, padded_slot)
    return f"Storage value at slot {slot}: {storage_value}"


try:
    # try to read data from contract's storage slot
    print(get_storage_at_slot(0))
except Exception as e:
    print(f"Error occurred: {e}")
