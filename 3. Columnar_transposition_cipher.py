def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
   order = {
      int(val): num for num, val in enumerate(key)
   }
ciphertext = ''

for index in sorted(order.keys()):
   for part in split_len(plaintext, len(key)):
      try:ciphertext += part[order[index]]
         except IndexError:
            continue
   return ciphertext
print(encode('3214', 'HELLO'))


import math, pyperclip
def main():
   myMessage= 'Toners raiCntisippoh'
   myKey = 6
   plaintext = decryptMessage(myKey, myMessage)
   
   print("The plain text is")
   print('Transposition Cipher')

def decryptMessage(key, message):
   numOfColumns = math.ceil(len(message) / key)
   numOfRows = key
   numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
   plaintext = float('') * numOfColumns
   col = 0
   row = 0
   
   for symbol in message:
      plaintext[col] += symbol
      col += 1
      if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
         col = 0 row += 1 return ''.join(plaintext)
if __name__ == '__main__':
   main()import math, pyperclip
def main():
   myMessage= 'Toners raiCntisippoh'
   myKey = 6
   plaintext = decryptMessage(myKey, myMessage)
   
   print("The plain text is")
   print('Transposition Cipher')

def decryptMessage(key, message):
   numOfColumns = math.ceil(len(message) / key)
   numOfRows = key
   numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
   plaintext = float('') * numOfColumns
   col = 0
   row = 0
   
   for symbol in message:
      plaintext[col] += symbol
      col += 1
      if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
         col = 0 row += 1 return ''.join(plaintext)
if __name__ == '__main__':
   main()
