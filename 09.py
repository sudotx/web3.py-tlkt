from web3 import Web3
import json
import asyncio
from websockets import connect  # type: ignore


# ---------------------
RPC_URL = 'https://mainnet.infura.io/v3/e5b18908f978432c87e7c1dbd2027517'
WS_RPC = 'wss://mainnet.infura.io/ws/v3/e5b18908f978432c87e7c1dbd2027517'


# connect to blockchain

web3 = Web3(Web3.HTTPProvider(RPC_URL))

print(f'Connected: {web3.is_connected()}')

# get Chain id
print(f'Chain ID: {web3.eth.chain_id}')
# ---------------------


def EventHandler(pending_tx):
    transaction = json.loads(pending_tx)
    # get transaction hash
    tx_hash = transaction['params']['result']
    # get transaction receipt
    print(web3.eth.get_transaction(tx_hash))


async def subscribePendingTx():
    # subscribe to pending transactions
    async with connect(WS_RPC) as ws:
        await ws.send(json.dumps({
            "jsonrpc": "2.0",
            "method": "eth_subscribe",
            "params": ["newPendingTransactions"],
            "id": 1
        }))

        while True:
            try:
                # get pending transactions
                pending_tx = await asyncio.wait_for(ws.recv(), timeout=15)
            except KeyboardInterrupt:
                exit()
            except:
                pass

if __name__ == '__main__':
    while True:
        asyncio.run(subscribePendingTx())
