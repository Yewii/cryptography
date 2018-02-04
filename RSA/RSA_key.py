
import os
import random
import sys

import rabinMiller, cryptomath


def main():
    # create a public keypair with 1024 bits key
    print('Making key files...')
    makeKeyFiles('yewii-15180110005',1024)
    print('key files made...')

def gengeratekey(keySize):
    # Create a pibilc/private key pair with keys that are keySize bits in size

    print('Generating p prime...')
    p = rabinMiller.generateLargePrime(keySize)
    print('Generating q prime...')
    q = rabinMiller.generateLargePrime(keySize)
    n = p*q

    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(2**(keySize - 1),2**(keySize))
        if cryptomath.gcd(e, (p-1)*(q-1)) == 1:
            break

    print('Calculating d that mod inverse of e...')
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

    publicKey=(n,e)
    privateKey=(n,d)

    print('public key:',publicKey)
    print('private key',privateKey)

    return(publicKey,privateKey)

def makeKeyFiles(name,keySize):
    #Creates two files "x_publicKey.txt' and 'x_privateKey' with the n,e and d,e integers written in them,delimited by a comma
    if os.path.exists('%s_publicKey.txt'%(name)) or os.path.exists('%s_privateKey.txt'%(name)):
        sys.exit('Warning:The file %s_publicKey.txt or %s_privateKey.txt already exits!Use a different name or delete these files and re-run this program'%(name,name))

    publicKey,privateKey = gengeratekey(keySize)

    print()
    print('The public key is a %s and %s digit nmber.' % (len(str(publicKey[0])),len(str(privateKey[1]))))
    print('Writing public key to file %s_publicKey.txt'%(name))
    fo = open('%s_publickey.txt'%(name),'w')
    fo.write('%s,%s,%s'%(keySize,publicKey[0],publicKey[1]))
    fo.close

    print()
    print('The private key is a %s and %s digit nmber' % (len(str(publicKey[0])), len(str(privateKey[1]))))
    print('Writing public key to file %s_privateKey.txt' % (name))
    fo = open('%s_privatekey.txt' % (name),'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close

if __name__=='__main__':
    main()
