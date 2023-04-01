from web3 import Web3

RPC_URL = 'https://rpc.ankr.com/eth'  # connected to anvil


# connect to blockchain

web3 = Web3(Web3.HTTPProvider(RPC_URL))


print(f'Connected: {web3.is_connected()}')  # proof of life


# connect to contract
router_address = web3.to_checksum_address(
    '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f')
router_abi = '[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'


router = web3.eth.contract(address=router_address, abi=router_abi)

# total number of allPairs of UniswapV2Factory
# answer to question 1
print(f'Number of pairs: {router.functions.allPairsLength().call()}')

token0 = web3.to_checksum_address('0x6B175474E89094C44Da98b954EedeAC495271d0F')
token1 = web3.to_checksum_address('0x6B175474E89094C44Da98b954EedeAC495271d0F')


print(router.functions.getPair(token0, token1).call())

print()


print(f'Address of the first pair: {router.functions.allPairs(0).call()}')
print(f'Address of the second pair: {router.functions.allPairs(1).call()}')
print(f'Address of the third pair: {router.functions.allPairs(2).call()}')


# get the address of the first n pair_s


# def get_n_pair_address_s(n):
#     pair_address_s = []
#     for i in range(n):
#         pair_address_s.append(target.functions.allPairs(i).call())
#         # get pair names

#     print(pair_address_s)


# get_n_pair_address_s(4)
