import hashlib
import json
import datetime

current_tr = []
last_block = []

def hash(block):
    strs = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha512(strs).hexdigest()

def tranjection(self, sender, receiver, amount):
    try:
        self.current_tr.append(
            {
                'sender' : sender,
                'receiver' : receiver,
                'amount' : amount,
                'time' : datetime.datetime.now()
            }
        )
    except:
        print("Tranjection Error : 802\nplease Check Receiver Address Valid")
    finally:
        return last_block['index'] + 1