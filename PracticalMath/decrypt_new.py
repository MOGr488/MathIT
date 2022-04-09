import math
head="Decryption using affine transformation"
print(head)
print("-"*len(head))
#define the sybol set size as 128
symbol_set=128

#define multiplicative inverse function under given modulo value
def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    
K1=int(input("Enter the key1 value: "))
while(True):
    
    if(math.gcd(K1, symbol_set)==1):  # check for relatively prime  
        break
    else:
       print("Enter key_A such that the symbol set and your key are relatively prime")
       K1=int(input("Enter the key1 value: ")) 

KI=modInverse(K1, symbol_set)

K2=int(input("Enter the key2 value: "))
input_String=input("Enter a word to decrypt: ")
   
#define decrypt character and string functions
def decryptChar(char):
      
      return chr(KI * (ord(char) - K2) % symbol_set)
   
def decrypt(string):
    return   "".join(map(decryptChar, string))


print(f"Decrypted text is: {decrypt(input_String)} for the given encrypted text {input_String} ")
