import sys

DEFAUL_BLOCK_SIZE = 128
BYTE_SIZE=256

def main():
    filename = 'encrypted_file.txt'


    while True:
        print("--------------------------------------------------------------------")
        mode = input('input 1.encrypt or 2.decrypt:\n')

        if mode == '1':
            message = input("input encrypt message:")
            pubKeyFilename = "yewii-15180110005_publickey.txt"
            print('Encrypting and writing to %s...'%(filename))
            encryptedText = encryptAndWriteToFile(filename,pubKeyFilename,message)
            print('Encrypted text:')
            print(encryptedText)

        elif mode == '2':
            privKeyFilename = 'yewii-15180110005_privatekey.txt'
            print("reading from %s and decrypting..."%(filename))
            decryptedText = readFromFileAndDecrypt(filename,privKeyFilename)

            print('Decrypted text:%s'%(decryptedText))

        choose=input("Dou you want to quit:\n1.quit 2.continue\n")
        if choose == '1':
            break
        # else:
        #     break

def getBlocksFromtext(message,blockSize=DEFAUL_BLOCK_SIZE):
    messageBytes = message.encode('ascii')
    blockInts = []
    for blockStart in range(0,len(messageBytes),blockSize):
        blockInt = 0
        for i in range(blockStart,min(blockStart+blockSize,len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
            blockInts.append(blockInt)
    return blockInts

def getTextFromBlocks(blockInts,messageLength,blockSize = DEFAUL_BLOCK_SIZE):
    message=[]
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize -1 , -1 , -1):
            if len(message) + i<messageLength:
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0,chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)

def encryptMessage(message,key,blockSize=DEFAUL_BLOCK_SIZE):
    encryptedBlocks = []
    n,e = key

    for block in getBlocksFromtext(message,blockSize):
        encryptedBlocks.append(pow(block,e,n))
    return encryptedBlocks

def decryptMessage(encryptedBlocks,messageLength,key,blockSize=DEFAUL_BLOCK_SIZE):
    decryptedBlocks = []
    n,d=key

    for block in encryptedBlocks:
        decryptedBlocks.append(pow(block,d,n))

    return getTextFromBlocks(decryptedBlocks,messageLength,blockSize)

def readKeyFile(keyFilename):
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize,n,EorD = content.split(',')
    return (int(keySize),int(n),int(EorD))

def encryptAndWriteToFile(messageFilename,keyFilename,message,blockSize=DEFAUL_BLOCK_SIZE):
    keySize, n , e = readKeyFile(keyFilename)

    if keySize < blockSize * 8:
        sys.exit('ERROR')

    encryptedBlocks = encryptMessage(message , (n,e) , blockSize)

    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encrypteContent = ','.join(encryptedBlocks)

    encrypteContent = '%s_%s_%s'%(len(message),blockSize,encrypteContent)
    fo = open(messageFilename,'w')
    fo.write(encrypteContent)
    fo.close()

    return encrypteContent

def readFromFileAndDecrypt(messageFilename,keyFilename):
    keySize, n ,d =readKeyFile(keyFilename)
    fo = open(messageFilename)
    content = fo.read()

    messageLength,blockSize,encryptMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    if keySize < blockSize * 8:
        sys.exit('error')

    encryptedBlocks = []
    for block in encryptMessage.split(','):
        encryptedBlocks.append(int(block))

    return decryptMessage(encryptedBlocks,messageLength,(n,d),blockSize)

if __name__=='__main__':
    main()