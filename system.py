import core

testnet = core.Blockchain()
testnet.new_block(proof = '1')
testnet.new_block(proof = '1')
testnet.new_block(proof = '1')
testnet.new_block(proof = '1')

datid = 'owkodkod'
testnet.new_nft(proof='1', nft_url='https://www.valid.nft.raumdoran.com/f{datid}')
print(testnet.chain)