from web3 import Web3

# Load account addresses and private keys from env variables
FIRST_ACCOUNT = '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266'
FIRST_ACCOUNT_PRIV = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'
SECOND_ACCOUNT = '0x70997970C51812dc3A010C7d01b50e0d17dc79C8'

# RPC URL for local development node
RPC_URL = 'http://127.0.0.1:8545'


# connect to blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))


# Estimate gas required for the transaction

def get_contract_instance(address, target_abi):
    target_address = web3.to_checksum_address(address)
    return web3.eth.contract(address=target_address, abi=target_abi)


target = get_contract_instance('0x5FbDB2315678afecb367f032d93F642f64180aa3',
                               '[{"inputs": [{"internalType": "string","name": "_key","type": "string"}],"stateMutability": "nonpayable","type": "constructor"},{"inputs": [],"name": "flag","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}]')

deposit_eth = target.functions.deposit().build_transaction({
    'value': web3.to_wei(1, 'ether'),
    'chainId': 1337,
    'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(FIRST_ACCOUNT)),
    'gas': 7000,
    'gasPrice': web3.eth.gas_price,
})

# withdraw eth from contract
withdraw_eth = target.functions.withdraw(100).build_transaction({
    'chainId': 1337,
    'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(FIRST_ACCOUNT)),
    'gas': 7000,
    'gasPrice': web3.eth.gas_price,
})


try:
    # Sign and send transaction
    tx_hash = web3.eth.send_transaction(
        {'to': '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266', 'data': deposit_eth})

    # Wait for confirmation
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(
        f"Transaction successful! Tx hash: {tx_receipt['transactionHash'].hex()}")
    print(web3.eth.get_transaction(tx_receipt['transactionHash']))
except Exception as e:
    print(f"Error occurred: {e}")
