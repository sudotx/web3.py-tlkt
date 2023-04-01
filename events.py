from web3 import Web3
import asyncio
import json

RPC_URL = 'http://127.0.0.1:8545'  # connected to anvil


# connect to blockchain

web3 = Web3(Web3.HTTPProvider(RPC_URL))

print(f'Connected: {web3.is_connected()}')

# get Chain id
print(f'Chain ID: {web3.eth.chain_id}')


# connect to contract
target_address = web3.to_checksum_address("")
target_abi = ""

target = web3.eth.contract(address=target_address, abi=target_abi)


def EventHandler(event):
    event = Web3.to_json(event)
    event = json.loads(event)
    print(event["args"]["sender"], event["args"]
          ["value"], event["args"]["message"])


async def EventLogLoop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            EventHandler(event)
        await asyncio.sleep(poll_interval)


def main():
    event_filter = target.events.Transfer._get_event_filter_params(
        fromBlock="latest")
    asyncio.run(EventLogLoop(event_filter, 2))

    if __name__ == "_main_":
        main()
