plain_text = input("Enter the plain text: ")
# plain_text = "hello world"
k = int(input("Enter number of step: "))
# k=3
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

Ceaser_cipher = []
n = int(len(plain_text))

print(plain_text)
# # plain_text = plain_text.split()
# plain_text = list(plain_text)

# print(plain_text[6])
# print(plain_text)

def Encryption(plain_text):
    for i in range(n):
        char = plain_text[i]
        Ceaser_cipher = char[i+k]%26

def encrypt(text,s):
 result = ""
   # transverse the plain text
 for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
#check the above function
text = "CEASER CIPHER DEMO"
s = 4

print ("Plain Text : ", text)
