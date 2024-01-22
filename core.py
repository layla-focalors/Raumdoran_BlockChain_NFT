import datetime

class Blockchain(object):
    def __init__ (self):
        self.chain = []
        self.current_transaction = []
        
    def tranjection(self, sender, receiver, amount):
        try:
            self.current_transaction.append(
                {
                    'sender' : sender,
                    'receiver' : receiver,
                    'amount' : amount,
                    'time' : datetime.datetime.now().timestamp()
                }
            )
        except:
            print("Tranjection Error : 802\nplease Check Receiver Address Valid")
        finally:
            return self.last_block['index'] + 1
    
    def new_block(self, proof, previous_hash = None):
        block = {
            'BlockID' : len(self.chain) +  1,
            'time' : datetime.datetime.now().timestamp(),
            'transactions' : self.current_transaction,
        }
        
        self.current_transaction = []
        print("LOG : NEW BLOCK APPEND FOR CHAIN")
        self.chain.append(block)
        return block
    
    def new_nft(self, nft_url, proof, previous_hash = None):
        # if(nft_url != ' ' and nft_url != ''):
        #     print("Error : URL codination is not allowed")
        #     return 0
        block = {
            'BlockID' : len(self.chain) + 1,
            'time' : datetime.datetime.now().timestamp(),
            'transactions' : self.current_transaction,
            'nft_url' : nft_url
        }
        self.current_transaction = []
        print("LOG : New NFT ADDED")
        self.chain.append(block)
    @property
    def last_block(self):
        return self.chain[-1]
    