import pyperclip

def main():
    print('input your message')
    message=input()
    key=8

    ciphertext = encryptMessage(key,message)

    print(ciphertext+'|')

    pyperclip.copy(ciphertext)

def encryptMessage(key,message):
    ciphertext=['']*key

    for col in range(key):
        pointer = col
        while pointer < len(message):
             ciphertext[col]+=message[pointer]

             pointer+=key

    return''.join(ciphertext)


if __name__ == "__main__":
    main()