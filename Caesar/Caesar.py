#Caesar Cipher


key=2

#select encrypt or decrypy
print('choose encrypt or decrypy')
mode=input()

#ciphertext
print('print ciphertext or express')
message=input()


LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated=''

message = message.upper()

for symbol in message:
    if symbol in message:
        num = LETTERS.find(symbol)
        if mode == "encrypt":
            num = num +key
        elif mode == "decrypy":
            num = num -key

        if num >= len(LETTERS):
            num = num-len(LETTERS)
        elif num < 0:
            num = num+len(LETTERS)

        translated = translated +LETTERS[num]

    else:
        translated = translated + symbol

print(translated)