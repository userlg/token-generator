import bcrypt

import hashlib

import base64

def generate_token(word : str) -> str:
    
    salt = bcrypt.gensalt(15)

    word = word.encode('utf-8')

    word = base64.b64encode(hashlib.sha256(word).digest())

    word_hashed = bcrypt.hashpw(word,salt)

    return word_hashed

def check_word(word : str, token: str) -> bool:
    word = word.encode('utf-8')
    word = base64.b64encode(hashlib.sha256(word).digest())
    return bcrypt.checkpw(word,token)
 
