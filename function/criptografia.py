import hashlib
import rsa
import pickle
import zipfile
from zipfile import ZipFile

# gerando as chaves
def generate_key():
    public_key,private_key = rsa.newkeys(1024)
    pickle.dump(public_key, open('files/public_key.pkl','wb'),protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(private_key, open('files/private_key.pkl','wb'),protocol=pickle.HIGHEST_PROTOCOL)

#Pegando a chave publica
def take_public_key():
    public_key = pickle.load(open('files/public_key.pkl','rb'))
    return public_key

def take_private_key():
    private_key = pickle.load(open('files/private_key.pkl','rb'))
    return private_key

def take_hash_encryption():
    hash_encryption = pickle.load(open('files/hash_encrypt.pkl','rb'))
    return hash_encryption
#Gerando o hash
def generate_hash(arquivo):
  hash = hashlib.new('ripemd160')
  hash.update(arquivo.encode('utf-8'))
  hash = hash.hexdigest()
  return hash

def compare_hashes(received_hash,generate_hash):
    if(received_hash==generate_hash):
        return True
    return False

def encryption_algorithm(hash,public_key):
    encryption = rsa.encrypt(hash.encode('utf-8'),public_key)
    return encryption

def dencryption_algorithm(hash_encrypt,private_key):
    dencryption = rsa.decrypt(hash_encrypt,private_key).decode()
    return dencryption

def compact_files():
    zipe_file = zipfile.ZipFile('files/documents.rar', 'w', zipfile.ZIP_DEFLATED)
    zipe_file.write('files/hash_encrypt.pkl')
    zipe_file.write('files/file.txt')
    zipe_file.close()

def descompact_files():
    zipe_file = ZipFile('files/documents.rar', 'r')
    zipe_file.extractall()
    zipe_file.close()