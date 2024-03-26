from mnemonic import Mnemonic
import eth_account,time
from eth_account import Account

def generate_mnemonic():
    mnemo = Mnemonic("english")
    mnemonic = mnemo.generate()
    return mnemonic  #随机生成助记词

    
eth_account.Account.enable_unaudited_hdwallet_features()    
wd=input('input the tail number：')
s=time.time()
i=0

while True:
    mnemonic = generate_mnemonic()
    private_key = Account.from_mnemonic(mnemonic)._private_key
    address = Account.from_key(private_key).address

    if address[-len(wd):] == wd:
        print('adress: '+address)
        print('mnemonic: '+mnemonic)
        print(i)
        break
    else:
        print(address)
    i+=1
    
    
r=time.time()-s
print('time: '+str(r))
print('speed: '+str(int(i/r))+'/s') 