import hashlib
import json

def hash(block):
    strs = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha512(strs).hexdigest()
