from function.open_txt import open_txt 
from function.criptografia import take_public_key,generate_hash
def main():
  arquivo = open_txt('arquivo.txt')
  public_key = take_public_key()
  hash = generate_hash(arquivo)
  print('Hash: ',hash)
  print('Public Key: ',public_key)

if __name__== "__main__":
  main()