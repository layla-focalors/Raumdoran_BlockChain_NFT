import core
import socket
import uuid
import datetime
import reqeusts

testnet = core.Blockchain()
testnet.new_block(proof = '1')
testnet.new_block(proof = '1')
testnet.new_block(proof = '1')
testnet.new_block(proof = '1')

datid = 'owkodkod'
testnet.new_nft(proof='1', nft_url='https://www.valid.nft.raumdoran.com/f{datid}')
print(testnet.chain)

mainNet = core.MainNet()
mainNet.new_block(proof = '1')

def printchain():
    print(mainNet.chain)
    return mainNet.chain

def service():
    print('Host IP : ' + socket.gethostbyname(socket.getfqdn()))
    print('Session Start ID : ' + str(uuid.uuid4()))
    print('Start Time : ' + str(datetime.datetime.now()))
    print(printchain)
    
    while True:
        # mode : transaction
        datas = {
            'validID' : ''
        }
        validID = requests.post(url, data=datas)
        mainNet.new_nft(proof = '1', nft_url='https://nft.raumdoran.com/' + validID)
        

if(__name__ == '__main__'):
    service()