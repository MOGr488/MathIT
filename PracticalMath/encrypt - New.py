import math
head="Encryption using affine transformation"
print(head)
print("-"*len(head))
#define the symbol set size as 128
symbol_set=128

K1=int(input("Enter the key1 value: "))

while(True):
    
    if(math.gcd(K1, symbol_set)==1):   
        break
    else:
        print("Enter key1 such that the symbol set and your key are relatively prime!!!")
        K1=int(input("Enter the key1 value: ")) 

K2=int(input("Enter the key2 value: "))

input_String=input("Enter a word to encrypt: ")

#define encrypt character and string function
def encryptChar(char):
     
      return chr((K1 * ord(char) + K2) % symbol_set)
		
def encrypt(string):
              
        return   "".join(map(encryptChar, string))
  
print(f"Cipher text is: {encrypt(input_String)} for the given plain text {input_String} ")
 