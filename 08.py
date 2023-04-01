from web3 import Web3

RPC_URL = 'https://rpc.ankr.com/eth'  # connected to anvil


# connect to blockchain

web3 = Web3(Web3.HTTPProvider(RPC_URL))

print(f'Connected: {web3.is_connected()}')

# get Chain id
print(f'Chain ID: {web3.eth.chain_id}')


block = web3.eth.get_block('latest')  # every 15 seconds
# print(block)

# get block number


def get_block_number():
    block = web3.eth.get_block('latest')
    print(block['number'])

# get block hash


def get_block_hash():
    block = web3.eth.get_block('latest')
    print(block['hash'])


def get_transactions_in_block():
    block = web3.eth.get_block('latest')
    for transactions in block['transactions']:
        # get transaction hash
        value = web3.to_hex(transactions)
        # get transaction details for hash
        # print(web3.eth.getTransaction(transactions))

        # get transaction count in block
        # print(web3.eth.get_block_transaction_count(block.))


get_transactions_in_block()


def look_for_approve_func():
    for transactions in block.transactions:
        # get transaction hash
        # print(web3.toHex(transactions))
        # get transaction details for hash
        value = web3.eth.get_transaction(transactions)
        # this is the approve function signature
        # if '095ea7b3' in web3.toHex(value['input']), this will return true
        if '095ea7b3' in web3.to_hex(transactions):
            print(
                f'found an approve transaction: {web3.eth.get_transaction(value["hash"])}')
