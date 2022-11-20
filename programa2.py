from function.open_txt import open_txt 
from function.criptografia import *
import rsa
import pickle

def main():
  file = open_txt('files/file.txt')
  public_key = take_public_key()
  hash = generate_hash(file)
  hash_encrypt = encryption_algorithm(hash, public_key)
  pickle.dump(hash_encrypt, open('files/hash_encrypt.pkl','wb'),protocol=pickle.HIGHEST_PROTOCOL)
  compact_files()
  print('Hash: ',hash)

if __name__== "__main__":
  main()