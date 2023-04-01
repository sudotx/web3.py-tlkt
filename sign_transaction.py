from web3 import Web3

# Load account addresses and private keys from env variables
FIRST_ACCOUNT = '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266'
FIRST_ACCOUNT_PRIV = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'
SECOND_ACCOUNT = '0x70997970C51812dc3A010C7d01b50e0d17dc79C8'

# RPC URL for local development node
RPC_URL = 'http://127.0.0.1:8545'


# connect to blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))


# Build transaction object, to send 1 ether from 1 user to  a sender
try:
    # Sign and send transaction
    tx_hash = web3.eth.send_transaction({
        'from': FIRST_ACCOUNT,
        'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(FIRST_ACCOUNT)),
        'to': SECOND_ACCOUNT,
        'value': web3.to_wei(1, 'ether'),
        'gas': 7000,
        'gasPrice': web3.eth.gas_price
    })

    # Wait for confirmation
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(
        f"Transaction successful! Tx hash: {tx_receipt['transactionHash'].hex()}")
    print(web3.eth.get_transaction(tx_receipt['transactionHash']))
except Exception as e:
    print(f"Error occurred: {e}")
