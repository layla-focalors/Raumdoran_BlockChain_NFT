import datetime
import hashlib
import random

class POW_Chain(object):
    def __init__ (self):
        self.chain = []
        self.current_transaction = []
        self.nodes = set()
        self.new_block(previous_hash=1, proof=100)
        
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
    
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = str(last_proof + proof).encode()
        guess_hash = hashlib.sha512(guess).hexdigest()
        return guess_hash[:4] == '0000'
    
    def pow(self, last_proof):
        proof = random.randint(-1000000, 1000000)
        while self.valid_proof(last_proof, proof) is False:
            proof = random.randint(-1000000, 1000000)
        return proof

class MainNet(object):
    def __init__ (self):
        self.chain = []
        self.current_transaction = []
        self.account = []
        
    def add_account(self, name, email):
        try:
            self.account.append({
                'accountID' : len(self.account) + 1,
                'name' : name,
                'email' : email,
                'NFT_Block_ID' : []
            })
            print("new Account Added")
        except:
            print("Error 703 : failed Create Accounts")
            
    def add_nft_account(self, accountID, nft_block_id, nft_block_id_url):
        #     print("Error : URL codination is not allowed")
        #     return 0
        block = {
            'BlockID' : len(self.chain) + 1,
            'time' : datetime.datetime.now().timestamp(),
            'transactions' : self.current_transaction,
            'nft_url' : nft_block_id_url
        }
        self.current_transaction = []
        print("LOG : New NFT ADDED for Account")
        self.chain.append(block)
            
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
    