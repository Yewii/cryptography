#caesar hack

print('print the message you wang to decrypt:')
message=input()

LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translate=''

    for symbol in message:
        if symbol in LETTERS:
            num=LETTERS.find(symbol)
            num=num-key

            if num < 0:
                num=num+len(LETTERS)

            translate+=LETTERS[num]
        else:
            translate=translate+symbol
    print('key #%s: %s'%(key,translate))

